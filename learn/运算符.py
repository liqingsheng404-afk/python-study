# x=int(input("请输入x:"))
# y=int(input("请输入y:"))
# print("x+y=%d"%(x+y))
# print("x-y=%d"%(x-y))
# print("x*y=%d"%(x*y))
# print("x/y=%f"%(x/y))
# print("x%%y=%d"%(x%y))
# print("x**y=%d"%(x**y))
# print("x//y=%d"%(x//y))
# == >= <= != > <           比较运算符
# + - * / // % **           算数运算符
# += -= *= /= //= %= **=    赋值运算符
# and or not                逻辑运算符
# num=int(input("请输入一个整数:"))
# print(num<=10 or num>=20)
# i=1
# while i>=1:
#     i+=1
#     print(i)
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