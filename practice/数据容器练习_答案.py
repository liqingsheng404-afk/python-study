# -*- coding: utf-8 -*-
"""
=========================================================
 数据容器练习 参考答案
=========================================================

说明：
  1. 整份文件可以直接运行，每题都有输出。
  2. 有几题是"故意让你报错"的（题5、14、19、20），这里用 try/except
     把真实的报错信息打印出来，方便你看懂错误长什么样。
  3. 答案不唯一，写法不同但结果对，你的就是对的。
"""

print("=" * 60)
print("题1 列表的取值与切片")

a = [10, 20, 30, 40, 50]
print("第 1 个元素   :", a[0])
print("最后一个元素  :", a[-1])          # -1 就是倒数第一个
print("中间三个      :", a[1:4])         # 含头不含尾：下标 1、2、3


print("=" * 60)
print("题2 列表的增删改")

nums = []
nums.append(10)
nums.append(20)
nums.append(30)
print("追加后  :", nums)
nums[1] = 100                           # 把第 2 个（下标 1）改成 100
print("改完后  :", nums)
nums.pop()                              # 删掉最后一个
print("删末尾后:", nums)


print("=" * 60)
print("题3 遍历求总分 / 最高分 / 平均分")

scores = [88, 92, 79, 95, 61]

total = 0
max_score = scores[0]                   # 打擂台：先假设第一个最大
for x in scores:
    total += x
    if x > max_score:
        max_score = x
print("循环版 : 总分 =", total, " 最高 =", max_score, " 平均 =", round(total / len(scores), 2))

print("内置版 : 总分 =", sum(scores), " 最高 =", max(scores), " 平均 =", round(sum(scores) / len(scores), 2))


print("=" * 60)
print("题4 sort() 和 sorted() 的区别")

c = [3, 1, 4, 1, 5, 9, 2]
ret = c.sort()                          # 原地修改
print("sort() 的返回值:", ret, "（是 None，说明它不返回新列表）")
print("sort() 之后 c  :", c, "（原列表被改了）")

d = [3, 1, 4, 1, 5, 9, 2]
e = sorted(d)                           # 返回新列表
print("sorted() 返回  :", e)
print("sorted() 之后 d:", d, "（原列表没变）")

print("降序           :", sorted(d, reverse=True))
print("反转           :", d[::-1])


print("=" * 60)
print("题5 元组的不可变")

t = (1, 2, 3)
try:
    t[0] = 99                           # 故意报错
except TypeError as err:
    print("改元组报错了 ->", err)

new_t = (99,) + t[1:]                   # 重新拼一个新元组
print("拼接出的新元组:", new_t)

print("(1)  的类型:", type((1)).__name__, " <- 这只是数字，不是元组")
print("(1,) 的类型:", type((1,)).__name__, " <- 单元素元组必须带逗号")


print("=" * 60)
print("题6 元组解包")

info = ("小明", 18, "北京")
name, age, city = info
print("一行解包:", name, age, city)

first, *rest = info
print("first =", first, " rest =", rest, " rest 的类型 =", type(rest).__name__)


print("=" * 60)
print("题7 字符串常用方法")

s = "  Hello Python World  "
print("去首尾空格:", s.strip())
print("全部小写  :", s.strip().lower())
print("空格换横线:", s.strip().replace(" ", "-"))
print("o 出现次数:", s.count("o"))
print("原字符串没变:", repr(s), " <- 方法都是返回新字符串")


print("=" * 60)
print("题8 字符串反转与回文")

for text in ("abcba", "上海自来水来自海上", "python"):
    reverse = text[::-1]
    result = "是回文" if text == reverse else "不是回文"
    print(f"{text} 的反转是 {reverse} -> {result}")


print("=" * 60)
print("题9 集合去重")

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
uniq = list(set(nums))                  # set 去重 -> 转回 list
uniq.sort()                             # 集合无序，所以要自己排序
print("去重并排序后:", uniq)
print("原列表", len(nums), "个元素，去重后", len(uniq), "个")


print("=" * 60)
print("题10 集合运算")

club_a = {"小明", "小红", "小刚"}
club_b = {"小红", "小美"}
print("两个都参加    :", club_a & club_b)
print("只在 a 社     :", club_a - club_b)
print("一共涉及的人  :", club_a | club_b, " 共", len(club_a | club_b), "人")
print("只在其中一个社:", club_a ^ club_b)


print("=" * 60)
print("题11 集合的存不存在判断")

cities = {"北京", "上海", "广州", "深圳"}
for c in ("北京", "上海", "杭州"):
    print(f"{c} 在集合里吗 -> {c in cities}")
# 换成列表写法一样，但集合是哈希查找 O(1)，列表要从头遍历 O(n)


print("=" * 60)
print("题12 空集合陷阱")

empty_set = set()
empty_dict = {}
print("set() 的类型:", type(empty_set).__name__)
print("{} 的类型   :", type(empty_dict).__name__)
print("{1, 2} 的类型:", type({1, 2}).__name__)
# {} 是空字典的字面量，空集合只能写 set()


print("=" * 60)
print("题13 字典基础操作")

student = {"姓名": "小明", "年龄": 18}
print("姓名:", student["姓名"])
student["年龄"] = 19                    # 键存在 -> 修改
student["城市"] = "北京"                # 键不存在 -> 新增
print("改完加完:", student)


print("=" * 60)
print("题14 get() 与直接取值的区别")

try:
    print(student["班级"])              # 故意报错
except KeyError as err:
    print("直接取不存在的键报错了 ->", err)
print("用 get 安全取值:", student.get("班级", "暂无"))
print("get 不写默认值 :", student.get("班级"))


print("=" * 60)
print("题15 遍历字典")

scores = {"语文": 88, "数学": 95, "英语": 79}
print("所有科目名:", list(scores.keys()))
print("所有分数  :", list(scores.values()))
for subject, score in scores.items():
    print(f"    {subject}: {score}")
for k in scores:
    print("for k in d 遍历出来的是键:", k)


print("=" * 60)
print("题16 词频统计")

sentence = "apple banana apple cherry banana apple"

count = {}
for word in sentence.split():
    count[word] = count.get(word, 0) + 1        # 核心套路
print("get 版   :", count)

count2 = {}
for word in sentence.split():                    # 不用 get 的写法
    if word in count2:
        count2[word] += 1
    else:
        count2[word] = 1
print("不用 get :", count2)


print("=" * 60)
print("题17 选型题（结论）")
print("  1. 一周七天的名字，固定不变 -> tuple（不可变，安全又省内存）")
print("  2. 一个班的成绩，可能增删改 -> list（有序、可变）")
print("  3. 一堆数字要去重           -> set（自动去重，查找 O(1)）")
print("  4. 姓名 -> 电话号码         -> dict（键值映射，按名字查号码极快）")
print("  5. 一整篇文章的文本         -> str（文本就是不可变的字符序列）")


print("=" * 60)
print("题18 假复制陷阱")

a1 = [1, 2]
b1 = a1                                 # 只是起了个别名，不是复制！
b1.append(3)
print("b = a  时: a =", a1, " b =", b1, " <- 两个都变了")
print("  它们是同一个对象吗:", id(a1) == id(b1))

a2 = [1, 2]
b2 = a2.copy()                          # 真正复制一份
b2.append(3)
print("copy() 时: a =", a2, " b =", b2, " <- a 没变")
print("  它们是同一个对象吗:", id(a2) == id(b2))
# b = a[:] 也能复制；这个坑几乎所有初学者都踩过


print("=" * 60)
print("题19 unhashable 陷阱")

try:
    {1, [2, 3]}                         # 故意报错
except TypeError as err:
    print("set 里放 list   ->", err)

try:
    {[1]: "x"}                          # 故意报错
except TypeError as err:
    print("list 当字典的键 ->", err)

print("tuple 当字典的键 ->", {(1, 2): "x"}, "（可以，因为 tuple 不可变）")
# 集合的元素、字典的键都必须可哈希；list / set / dict 可变 -> 不行


print("=" * 60)
print("题20 元组的不可变其实不彻底")

t2 = (1, [2, 3])
try:
    t2[0] = 99                          # 故意报错
except TypeError as err:
    print("改元组元素 ->", err)

t2[1].append(4)                         # 但里面的列表能改
print("但里面的列表被改了:", t2)
# 元组保存的是引用：元组本身不能换元素，但它装着的可变对象照样能改


print("=" * 60)
print("题21 列表推导式 + 字典推导式")

squares = [x * x for x in range(1, 21) if x % 3 == 0]
print("1~20 中能被 3 整除的数的平方:", squares)

square_map = {x: x * x for x in range(1, 6)}
print("字典推导:", square_map)


print("=" * 60)
print("全部答案演示完毕。")
