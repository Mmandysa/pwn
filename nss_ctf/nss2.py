from pwn import *

# --- 配置 ---
# 设置目标服务器的地址和端口
HOST = 'node4.anna.nssctf.cn'
PORT = 28161

# 设置日志级别，方便查看脚本交互过程
context.log_level = 'info'

# --- 脚本主逻辑 ---
# 连接到远程服务器
io = remote(HOST, PORT)

# 接收欢迎信息，直到出现第一个问题
io.recvuntil(b'What is ')

# 题目要求完成100道题，所以我们循环100次
for i in range(100):
    try:
        # 读取问题行，例如 "4 + 54?\n"
        question_line = io.recvline()
        
        # 将字节串解码为字符串，并去掉首尾空白
        # 例如: "4 + 54?"
        question_str = question_line.decode().strip()
        
        # 按空格分割字符串，得到数字和运算符
        # 例如: ['4', '+', '54?']
        parts = question_str.split(' ')
        
        # 提取数字和运算符
        num1 = int(parts[0])
        operator = parts[1]
        # 第二个数字末尾带有问号 '?'，需要去掉它
        num2 = int(parts[2][:-1])
        
        # 根据运算符进行计算
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        else:
            log.error(f"未知的运算符: {operator}")
            break
            
        # 打印日志，方便我们跟踪进度
        log.info(f"第 {i+1} 题: {num1} {operator} {num2} = {result}")

        # 将计算结果发送回服务器
        io.sendline(str(result).encode())
        
        # 接收服务器的响应，准备处理下一道题
        # 如果不是最后一道题，服务器会返回 "Correct!\nWhat is "
        if i < 99:
            io.recvuntil(b'What is ')

    except Exception as e:
        log.error(f"在第 {i+1} 题出错了: {e}")
        break

# 循环结束后，接收最后服务器返回的所有信息，其中就包含了flag
log.success("100道题全部完成！正在接收Flag...")
flag = io.recvall(timeout=2).decode()
print("\n" + "="*20)
print("Flag is: ", flag.strip())
print("="*20 + "\n")

# 关闭连接
io.close()