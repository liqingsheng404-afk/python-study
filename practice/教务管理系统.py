# -*- coding: utf-8 -*-
"""
教务管理系统 —— 学员成绩信息维护与管理

需求（7 项功能）：
  1. 添加学生信息（姓名 + 语文 / 数学 / 英语）
  2. 修改学生信息（按姓名找到学生，重新录入三科成绩）
  3. 删除学生信息（按姓名删除）
  4. 查询学生信息（按姓名查询并输出）
  5. 列出所有学生
  6. 统计班级成绩（三科的最高分 / 最低分 / 平均分，以及最高分和最低分的学员姓名）
  7. 退出系统

数据结构（列表 + 字典 + 函数）：
    students = [
        {"name": "张三", "chinese": 88.0, "math": 95.0, "english": 79.0},
        {"name": "李四", "chinese": 92.0, "math": 60.0, "english": 100.0},
    ]
    —— 列表装所有学生，每个学生是一个字典
    —— 字典的键 = 字段名，值 = 具体数据，正好对应「姓名 -> 成绩」的映射关系

说明：本文件不保存到硬盘，程序关掉数据就没了（这叫"内存存储"）。
     等课程学到「面向对象」以后，可以改写成 Student / StudentManager 两个类。
"""


# ========================= 数据存放区 =========================

students = []          # 所有学生都放在这个列表里

# 科目配置：(显示用的名字, 字典里的键名)
SUBJECTS = (
    ("语文", "chinese"),
    ("数学", "math"),
    ("英语", "english"),
)


# ========================= 通用工具函数 =========================

def print_line():
    """打印一条分隔线，让输出更整齐"""
    print("-" * 46)


def input_name(tip="请输入学生姓名："):
    """录入姓名：不允许为空"""
    while True:
        name = input(tip).strip()
        if name == "":
            print("  [提示] 姓名不能为空，请重新输入")
            continue
        return name


def input_score(subject):
    """录入一科成绩：必须是 0~100 之间的数字"""
    while True:
        text = input(f"  请输入{subject}成绩：").strip()
        if text == "":
            print("  [提示] 不能为空，请重新输入")
            continue
        try:
            score = float(text)
        except ValueError:
            print("  [提示] 成绩必须是数字，请重新输入")
            continue
        if score < 0 or score > 100:
            print("  [提示] 成绩应在 0~100 之间，请重新输入")
            continue
        return score


def input_all_scores(stu):
    """依次录入三科成绩，存进学生字典里"""
    for subject, key in SUBJECTS:
        stu[key] = input_score(subject)


def find_index(name):
    """按姓名查找学生，返回它在列表里的下标；找不到返回 -1"""
    for i, stu in enumerate(students):
        if stu["name"] == name:
            return i
    return -1


def find_student(name):
    """按姓名查找学生，找到返回那个字典；找不到返回 None"""
    i = find_index(name)
    if i == -1:
        return None
    return students[i]


def short_info(stu):
    """把一个学生的三科成绩拼成一行短文本"""
    return (f"语文={stu['chinese']:g}  "
            f"数学={stu['math']:g}  "
            f"英语={stu['english']:g}")


# ========================= 7 个功能 =========================

def add_student():
    """1. 添加学生信息"""
    print_line()
    print("[功能 1] 添加学生信息")
    name = input_name()

    # 姓名是查找/删除的依据，所以不允许重名
    if find_student(name) is not None:
        print(f"  [提示] 学生「{name}」已存在，无法重复添加")
        print("         如果要改成绩，请用功能 2")
        return

    stu = {"name": name}
    input_all_scores(stu)
    students.append(stu)
    print(f"  [成功] 已添加学生「{name}」：{short_info(stu)}")


def modify_student():
    """2. 修改学生信息"""
    print_line()
    print("[功能 2] 修改学生信息")
    if not students:
        print("  [提示] 系统里还没有学生信息")
        return

    name = input_name("请输入要修改的学生姓名：")
    stu = find_student(name)
    if stu is None:
        print(f"  [提示] 没有找到学生「{name}」")
        return

    print(f"  该学生当前成绩：{short_info(stu)}")
    print("  请重新录入三科成绩：")
    input_all_scores(stu)
    print(f"  [成功] 已修改学生「{name}」：{short_info(stu)}")


def delete_student():
    """3. 删除学生信息"""
    print_line()
    print("[功能 3] 删除学生信息")
    if not students:
        print("  [提示] 系统里还没有学生信息")
        return

    name = input_name("请输入要删除的学生姓名：")
    i = find_index(name)
    if i == -1:
        print(f"  [提示] 没有找到学生「{name}」")
        return

    students.pop(i)          # 按下标删除，最精确
    print(f"  [成功] 已删除学生「{name}」")


def query_student():
    """4. 查询学生信息"""
    print_line()
    print("[功能 4] 查询学生信息")
    if not students:
        print("  [提示] 系统里还没有学生信息")
        return

    name = input_name("请输入要查询的学生姓名：")
    stu = find_student(name)
    if stu is None:
        print(f"  [提示] 没有找到学生「{name}」")
        return

    total = stu["chinese"] + stu["math"] + stu["english"]
    print(f"  姓名：{stu['name']}")
    for subject, key in SUBJECTS:
        print(f"  {subject}：{stu[key]:g}")
    print(f"  总分：{total:g}    平均分：{total / 3:.2f}")


def list_students():
    """5. 列出所有学生"""
    print_line()
    print("[功能 5] 列出所有学生")
    if not students:
        print("  [提示] 系统里还没有学生信息")
        return

    print(f"  共 {len(students)} 名学生：")
    for i, stu in enumerate(students, start=1):
        print(f"  {i}. {stu['name']}  {short_info(stu)}")


def statistics():
    """6. 统计班级成绩"""
    print_line()
    print("[功能 6] 统计班级成绩")
    if not students:
        print("  [提示] 系统里还没有学生信息，无法统计")
        return

    print(f"  班级人数：{len(students)}")
    for subject, key in SUBJECTS:
        # 把这一科所有人的成绩取出来，组成一个列表
        scores = [stu[key] for stu in students]

        top = max(scores)
        low = min(scores)
        avg = sum(scores) / len(scores)

        # 最高/最低分可能有好几个人并列，所以用列表推导式把所有同名次的人都找出来
        top_names = [stu["name"] for stu in students if stu[key] == top]
        low_names = [stu["name"] for stu in students if stu[key] == low]

        print(f"  【{subject}】"
              f"最高分 {top:g}（{'、'.join(top_names)}）   "
              f"最低分 {low:g}（{'、'.join(low_names)}）   "
              f"平均分 {avg:.2f}")


# ========================= 主程序 =========================

MENU = """
================ 教务管理系统 ================
   1. 添加学生信息        2. 修改学生信息
   3. 删除学生信息        4. 查询学生信息
   5. 列出所有学生        6. 统计班级成绩
   7. 退出系统
=============================================="""


def main():
    """程序入口：循环显示菜单，等用户选择功能"""
    print("欢迎使用教务管理系统")

    while True:
        print(MENU)
        choice = input("请输入功能编号（1-7）：").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            modify_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            query_student()
        elif choice == "5":
            list_students()
        elif choice == "6":
            statistics()
        elif choice == "7":
            print("感谢使用，再见！")
            break
        else:
            print("  [提示] 输入无效，请输入 1~7 之间的数字")


# 只有「直接运行本文件」时才启动主程序
# （如果这个文件被别的文件 import，下面的 main() 不会自动执行）
if __name__ == "__main__":
    main()
