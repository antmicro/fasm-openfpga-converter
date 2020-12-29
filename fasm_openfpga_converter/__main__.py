#!/usr/bin/env python3

from .fasm2openfpga import fasm2openfpga
from .openfpga2fasm import openfpga2fasm

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--fasm2openfpga', action='store_const', const=True,
                            help='When set fasm is treated as input, and bustream is produced. If not set, bitstream is read and fasm is produced')
    parser.add_argument('--fasm', type=str, help='Path to SDF file', required=True)
    parser.add_argument('--bitstream', type=str, help='Path to JSON file', required=True)
    parser.add_argument('--device-independent', action='store_const', const=True,
                            help='Process device independent bitstream')

    args = parser.parse_args()
    if args.fasm2openfpga:
        with open(args.fasm) as fasm_file:
            fasm = fasm_file.readlines()
            xml = fasm2openfpga(fasm)
            xml.write(open(args.bitstream, 'wb'), encoding='utf-8', pretty_print=True)

    else:

        fasm = openfpga2fasm(args.bitstream)
        with open(args.fasm, 'w') as fd:
            print('\n'.join(fasm), file=fd)


if '__name__' == '__main__':
    main()
