FILENAME_IN = 'tetris.gb'
FILENAME_OUT = 'hack.gb'

ADDRESSES = (
        0x0403,
        0x0bd2,
        0x0d70,
        0x0d7a,
        0x0e61,
        0x0e6b,
        0x11ae,
        0x134d,
        0x1521,
        0x187b,
        0x1e21,
        0x1f25,
        0x2413,
        0x64f1,
        0x6513,
        )

with open(FILENAME_IN, 'rb') as inf:
    rom = bytearray(inf.read())

for addr in ADDRESSES:
    assert(rom[addr:addr+3] == b'\xea\xe8\xdf')
    for i in range(3):
        rom[addr+i] = 0

with open(FILENAME_OUT, 'wb') as outf:
    outf.write(rom)
