#!/usr/bin/env python3
# coding: utf-8
#
# Copyright (C) 2020  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

import os
import lxml.etree as etree
from fasm_openfpga_converter import fasm2openfpga
from fasm_openfpga_converter import openfpga2fasm

fasm_path = 'tests/data/fasm'
golden_bitstream_path = 'tests/data/'
parsed_bitstream = list()
golden_bitstream = list()


def test_parse():
    files = sorted(os.listdir(golden_bitstream_path))
    for f in files:
        if f.endswith('.xml'):
            golden_bitfile = golden_bitstream_path + f
            parsed_bitstream.append(generate_parsed(golden_bitfile))
            golden_bitstream.append(etree.parse(golden_bitfile))


def generate_parsed(golden):
    fasm = openfpga2fasm.openfpga2fasm(golden)
    xml = fasm2openfpga.fasm2openfpga(fasm)
    return xml


def test_format_bit_compare():
    for i in range(len(golden_bitstream)):
        golden = golden_bitstream[i]
        parsed = parsed_bitstream[i]
        for gtag, ptag in zip(golden.iter(), parsed.iter()):
            assert gtag.tag == ptag.tag, \
                  "gtag: {}, ptag: {}".format(gtag.tag, ptag.tag)
            for attr in gtag.attrib:
                gval = gtag.get(attr)
                pval = ptag.get(attr)
                assert gval == pval, \
                    "attr: {}, gval: {}, pval: {}".format(attr, gval, pval)
