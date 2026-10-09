# -*- coding: utf-8 -*-
"""
教务管理系统（零函数版）

和上一版《教务管理系统.py》功能完全一样，但只使用你目前学过的知识：

  ✅ 用了：变量、流程控制（if / while / for / break / continue）
          数据容器（列表 / 字典 / 元组）、字符串方法、输入输出
  ❌ 没用：def（函数）、class（类）、try/except（异常）、文件操作

成绩校验用的是字符串方法 text.isdigit()，所以只接受「0~100 的整数」；
输入 abc、88.5、-5 都会提示重新输入。
（等课程学到第 86 集「异常处理」，可以换成更严谨的 try/except 写法）

数据结构：
    students = [
        {"name": "张三", "chinese": 88, "math": 95, "english": 79},
        {"name": "李四", "chinese": 92, "math": 60, "english": 100},
    ]
    列表装所有学生，每个学生是一个字典
"""

students = []          # 存放所有学生

# 科目配置：(显示用的名字, 字典里的键名)  —— 这是个元组，里面套元组
SUBJECTS = (
    ("语文", "chinese"),
    ("数学", "math"),
    ("英语", "english"),
)

MENU = """
================ 教务管理系统 ================
   1. 添加学生信息        2. 修改学生信息
   3. 删除学生信息        4. 查询学生信息
   5. 列出所有学生        6. 统计班级成绩
   7. 退出系统
=============================================="""


print("欢迎使用教务管理系统")

# ==========================================================
#  主循环：显示菜单 -> 等用户输入编号 -> 执行对应功能
#  说明：循环里的 continue 表示「本功能不做了，回到菜单」
# ==========================================================
while True:
    print(MENU)
    choice = input("请输入功能编号（1-7）：").strip()

    # ------------------------------------------------------
    # 功能 1：添加学生信息
    # ------------------------------------------------------
    if choice == "1":
        print("-" * 46)
        print("[功能 1] 添加学生信息")

        # 第 1 步：录入姓名，不允许为空
        while True:
            name = input("请输入学生姓名：").strip()
            if name == "":
                print("  [提示] 姓名不能为空，请重新输入")
                continue
            break

        # 第 2 步：检查是否重名（姓名是查找依据，重名会删错人）
        existed = False
        for stu in students:
            if stu["name"] == name:
                existed = True
                break
        if existed:
            print(f"  [提示] 学生「{name}」已存在，无法重复添加")
            print("         如果要改成绩，请用功能 2")
            continue

        # 第 3 步：录入三科成绩
        stu = {"name": name}          # 先建好字典，只放了姓名
        for subject, key in SUBJECTS:
            while True:
                text = input(f"  请输入{subject}成绩：").strip()
                if not text.isdigit():
                    print("  [提示] 成绩必须是 0~100 的整数，请重新输入")
                    continue
                score = int(text)
                if score > 100:
                    print("  [提示] 成绩不能大于 100，请重新输入")
                    continue
                stu[key] = score      # 校验通过，存进字典
                break

        students.append(stu)          # 把学生字典放进列表
        print(f"  [成功] 已添加学生「{name}」："
              f"语文={stu['chinese']}  数学={stu['math']}  英语={stu['english']}")

    # ------------------------------------------------------
    # 功能 2：修改学生信息
    # ------------------------------------------------------
    elif choice == "2":
        print("-" * 46)
        print("[功能 2] 修改学生信息")

        if not students:
            print("  [提示] 系统里还没有学生信息")
            continue

        name = input("请输入要修改的学生姓名：").strip()

        # 按姓名查找：找到就把那个字典存进 target，找不到 target 还是 None
        # 注意：下面这段「遍历查找」的代码，功能 3 和功能 4 里又各写了一遍
        #       —— 这就是「重复代码」，等你学了函数，就能只写一次、三处调用
        target = None
        for stu in students:
            if stu["name"] == name:
                target = stu
                break
        if target is None:
            print(f"  [提示] 没有找到学生「{name}」")
            continue

        print(f"  该学生当前成绩：语文={target['chinese']}  "
              f"数学={target['math']}  英语={target['english']}")
        print("  请重新录入三科成绩：")

        # 这段录入成绩的代码，和功能 1 里的几乎一模一样（同样是重复代码）
        for subject, key in SUBJECTS:
            while True:
                text = input(f"  请输入{subject}成绩：").strip()
                if not text.isdigit():
                    print("  [提示] 成绩必须是 0~100 的整数，请重新输入")
                    continue
                score = int(text)
                if score > 100:
                    print("  [提示] 成绩不能大于 100，请重新输入")
                    continue
                target[key] = score
                break

        print(f"  [成功] 已修改学生「{name}」："
              f"语文={target['chinese']}  数学={target['math']}  英语={target['english']}")

    # ------------------------------------------------------
    # 功能 3：删除学生信息
    # ------------------------------------------------------
    elif choice == "3":
        print("-" * 46)
        print("[功能 3] 删除学生信息")

        if not students:
            print("  [提示] 系统里还没有学生信息")
            continue

        name = input("请输入要删除的学生姓名：").strip()

        # 这次要找的是「下标」，因为列表的 pop() 按下标删除最精确
        index = -1
        i = 0
        for stu in students:
            if stu["name"] == name:
                index = i
                break
            i += 1

        if index == -1:
            print(f"  [提示] 没有找到学生「{name}」")
            continue

        students.pop(index)
        print(f"  [成功] 已删除学生「{name}」")

    # ------------------------------------------------------
    # 功能 4：查询学生信息
    # ------------------------------------------------------
    elif choice == "4":
        print("-" * 46)
        print("[功能 4] 查询学生信息")

        if not students:
            print("  [提示] 系统里还没有学生信息")
            continue

        name = input("请输入要查询的学生姓名：").strip()

        target = None
        for stu in students:
            if stu["name"] == name:
                target = stu
                break
        if target is None:
            print(f"  [提示] 没有找到学生「{name}」")
            continue

        total = target["chinese"] + target["math"] + target["english"]
        print(f"  姓名：{target['name']}")
        for subject, key in SUBJECTS:
            print(f"  {subject}：{target[key]}")
        print(f"  总分：{total}    平均分：{total / 3:.2f}")

    # ------------------------------------------------------
    # 功能 5：列出所有学生
    # ------------------------------------------------------
    elif choice == "5":
        print("-" * 46)
        print("[功能 5] 列出所有学生")

        if not students:
            print("  [提示] 系统里还没有学生信息")
            continue

        print(f"  共 {len(students)} 名学生：")
        i = 1                     # 用计数器给每个学生编号
        for stu in students:
            print(f"  {i}. {stu['name']}  "
                  f"语文={stu['chinese']}  数学={stu['math']}  英语={stu['english']}")
            i += 1

    # ------------------------------------------------------
    # 功能 6：统计班级成绩
    # ------------------------------------------------------
    elif choice == "6":
        print("-" * 46)
        print("[功能 6] 统计班级成绩")

        if not students:
            print("  [提示] 系统里还没有学生信息，无法统计")
            continue

        print(f"  班级人数：{len(students)}")

        for subject, key in SUBJECTS:
            # 列表推导式（第 42 集）：把这一科所有人的成绩收集成一个列表
            # 如果不熟，可以改写成：scores = []; 然后 for 循环 append
            scores = [stu[key] for stu in students]

            top = max(scores)                  # 最高分
            low = min(scores)                  # 最低分
            avg = sum(scores) / len(scores)    # 平均分

            # 最高/最低分可能好几个人并列，所以把同分的人都找出来
            top_names = [stu["name"] for stu in students if stu[key] == top]
            low_names = [stu["name"] for stu in students if stu[key] == low]

            print(f"  【{subject}】"
                  f"最高分 {top}（{'、'.join(top_names)}）   "
                  f"最低分 {low}（{'、'.join(low_names)}）   "
                  f"平均分 {avg:.2f}")

    # ------------------------------------------------------
    # 功能 7：退出系统
    # ------------------------------------------------------
    elif choice == "7":
        print("感谢使用，再见！")
        break

    # ------------------------------------------------------
    # 其他：输入了 1~7 以外的内容
    # ------------------------------------------------------
    else:
        print("  [提示] 输入无效，请输入 1~7 之间的数字")
