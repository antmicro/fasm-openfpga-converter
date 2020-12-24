import sys
import lxml.etree as ET

def fasm2openfpga(fasm, fabric_independent=False):

    bitstream = ET.Element('fabric_bitstream')
    tree = ET.ElementTree(bitstream)
    id_num = 0
    for line in open(fasm):
        fasm_entry, bit = line.split()
        entry = ET.SubElement(bitstream, 'bit')
        entry.attrib['id'] = str(id_num)
        entry.attrib['value'] = bit
        entry.attrib['path'] = fasm_entry
        entry.text="\n\t"
        id_num = id_num + 1

    return tree

