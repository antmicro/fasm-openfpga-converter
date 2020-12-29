import lxml.etree as ET


def openfpga2fasm(openfpga_bitstream, fabric_independent=False):

    bitstream = ET.parse(openfpga_bitstream).getroot()
    assert bitstream.tag == 'fabric_bitstream', \
           "Expected 'fabric_bitstream' tag as root tag in the file"

    fasm = []
    for bit in bitstream.findall('bit'):
        fasm_entry = bit.attrib['path']
        value = bit.attrib['value']
        fasm.append(f'{fasm_entry} {value}')

    return fasm
