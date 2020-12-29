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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fasm_openfpga_converter",
    version="0.0.1",
    author="SymbiFlow Authors",
    author_email="symbiflow@lists.librecores.org",
    description="Tool for converting openFPGA bitstreams \
                to FASM and vice versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antmicro/fasm-openfpga-converter",
    packages=setuptools.find_packages(),
    install_requires=['lxml'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts':
        ['fasm_openfpga_converter=fasm_openfpga_converter.__main__:main'],
    },
)
