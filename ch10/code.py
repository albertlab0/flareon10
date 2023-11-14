import ctypes
import struct
addr = id(check_snake_length)
addr += 0x78
g = (ctypes.c_char*8).from_address(addr)
v,  = struct.unpack("Q", g)
print(f"{v:x}")
