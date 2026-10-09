# -*- coding: utf-8 -*-
"""
=========================================================
 流程控制练习 参考答案
=========================================================

说明：
  1. 为了让整个文件能"直接运行看结果"，每题都用的是固定数据。
     想真的从键盘输入，把  n = 7  这种改写成
         n = int(input("请输入一个整数:"))
     就可以了。
  2. 答案不唯一，写法跟你不一样但结果对，那你的就对。
  3. 需要键盘交互的两道题（题15、题16）写成了函数，
     想玩的话把文件最后一行的注释去掉即可。
"""

print("=" * 50)
print("题1 奇偶判断")
n = 7                                  # 改成 n = int(input("请输入一个整数:"))
if n % 2 == 0:
    print(f"{n} 是偶数")
else:
    print(f"{n} 是奇数")


print("=" * 50)
print("题2 成绩等级")
score = 85                             # 改成 score = int(input("请输入分数:"))
if score < 0 or score > 100:
    print("分数不合法")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")
# 为什么 elif score >= 80 不用写 80 <= score < 90？
# 因为前面已经判断过 score >= 90 不成立，能走到这里就说明 score < 90 了。


print("=" * 50)
print("题3 闰年判断")
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} 是闰年")
else:
    print(f"{year} 是平年")


print("=" * 50)
print("题4 三个数里找最大")

a, b, c = 12, 45, 33

# 写法一：两两比较 + elif
if a >= b and a >= c:
    big = a
elif b >= c:
    big = b
else:
    big = c
print("写法一 最大值:", big)

# 写法二（更推荐，思路更顺）：先假设 a 最大，再让 b、c 来挑战
big = a
if b > big:
    big = b
if c > big:
    big = c
print("写法二 最大值:", big)


print("=" * 50)
print("题5 1~100 求和")

total = 0
for i in range(1, 101):
    total += i
print("for 求和结果: ", total)

total = 0
i = 1
while i <= 100:
    total += i
    i += 1                             # 这行千万别忘，忘了就是死循环
print("while 求和结果:", total)


print("=" * 50)
print("题6 1~100 的偶数和")

s = 0
for i in range(1, 101):
    if i % 2 == 0:
        s += i
print("写法一（for + if）:  ", s)

s = 0
for i in range(2, 101, 2):             # 第三个参数是步长，每次 +2
    s += i
print("写法二（range 步长）:", s)


print("=" * 50)
print("题7 求阶乘")

n = 5
result = 1                             # 累乘的初始值是 1
for i in range(1, n + 1):
    result *= i
print(f"for 版本:   {n}! = {result}")

n = 5
result = 1
i = 1
while i <= n:
    result *= i
    i += 1
print(f"while 版本: {n}! = {result}")


print("=" * 50)
print("题8 九九乘法表")

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i * j}", end="\t")
    print()                            # 内层循环结束后换行


print("=" * 50)
print("题9 能被 3 或 5 整除的数")

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")
print()


print("=" * 50)
print("题10 判断素数")

n = 97
if n <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break                      # 已经证明不是素数，剩下的不用试了
print(f"{n} " + ("是素数" if is_prime else "不是素数"))
# 只要试到根号 n：因为如果 n = a × b，a 和 b 里必有一个 <= 根号 n。


print("=" * 50)
print("题11 跳过数字（continue）")

for i in range(1, 101):
    if i % 7 == 0 or '7' in str(i):
        continue                       # 这一轮不要了，直接进入下一轮
    print(i, end=" ")
print()


print("=" * 50)
print("题12 斐波那契数列前 20 项")

a, b = 1, 1
for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b
print()
# a, b = b, a + b 会先把右边的 b 和 a+b 都算好，再一起赋值给左边，
# 所以不会出现"a 已经变了导致算错"的问题。


print("=" * 50)
print("题13 水仙花数")

for i in range(100, 1000):
    bai = i // 100                     # 整除 100 得到百位
    shi = i // 10 % 10                 # 先去掉个位，再取个位 = 十位
    ge = i % 10                        # 对 10 取余得到个位
    if bai ** 3 + shi ** 3 + ge ** 3 == i:
        print(i, end=" ")
print()
# 答案：153 370 371 407


print("=" * 50)
print("题14 统计字符类型")

text = "Hello 2026, 你好 Python!"
letters = digits = spaces = others = 0
for ch in text:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        others += 1                    # 中文、标点都算"其他"
print(f"字母 {letters} 个，数字 {digits} 个，空格 {spaces} 个，其他 {others} 个")
# 注意：如果用 ch.isalpha()，"你好"里的中文字也会被算成字母，
# 所以这里老老实实用 'a' <= ch <= 'z' 这种区间判断。


print("=" * 50)
print("题15 猜数字游戏 —— 见函数 guess_number()")
print("题16 求平均分 —— 见函数 average_scores()")


def guess_number():
    """猜数字游戏：需要键盘输入，想玩就在文件末尾调用它。"""
    import random

    target = random.randint(1, 100)
    count = 0
    while True:
        guess = int(input("请输入你猜的数字(1~100):"))
        count += 1
        if guess > target:
            print("太大了")
        elif guess < target:
            print("太小了")
        else:
            print(f"猜对了！你一共猜了 {count} 次")
            break
        if count >= 7:                 # 7 次还没中，直接公布答案
            print(f"已经猜了 7 次了，正确答案是 {target}")
            break


def average_scores():
    """反复输入成绩，输入 0 结束，然后算总分和平均分。"""
    total = 0
    count = 0
    while True:
        score = float(input("请输入成绩（输入 0 结束）:"))
        if score == 0:
            break
        total += score
        count += 1
    if count == 0:
        print("你一个成绩都没输入，没法算平均分")   # 防止除以 0 报错
    else:
        print(f"共输入 {count} 个成绩，总分 {total}，平均分 {total / count:.2f}")


print("=" * 50)
print("题17 鸡兔同笼")

heads, feet = 35, 94
found = False
for chicken in range(heads + 1):       # 穷举鸡的只数，从 0 试到 heads
    rabbit = heads - chicken
    if 2 * chicken + 4 * rabbit == feet:
        print(f"鸡 {chicken} 只，兔 {rabbit} 只")
        found = True
if not found:
    print("无解")
# 这道题其实用数学一步就能算出来，但用循环穷举的思路
# 在编程里非常重要（很多题想不出公式时，穷举是最稳的解法）。


print("=" * 50)
print("题18 打印图形")

n = 5
print("(a) 直角三角形：")
for i in range(1, n + 1):
    print("*" * i)

print("(b) 等腰三角形：")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("(c) 菱形：")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):          # 下半部分倒着来，步长是 -1
    print(" " * (n - i) + "*" * (2 * i - 1))


print("=" * 50)
print("全部答案演示完毕。")

# 想玩需要键盘输入的两道题，把下面任意一行的注释去掉再运行：
# guess_number()
# average_scores()
