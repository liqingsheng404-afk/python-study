#stu_info={'name':  {'ch':ch_score  ,  'math':math_score  ,  'english':english_score}  }
manu="""
欢迎登入教务系统~
请选择操作：
1.添加学生信息
2.查询学生信息
3.删除学生信息
4.修改学生信息
5.列出所有学生
6.统计成绩(语 数 英分别的最高 最低 平均分并列出最高最低学生姓名)
7.退出
"""
stu_info={}
while True:
    print(manu)
    choice=input("请输入操作编号：")
    match choice:
        case '1':#添加
            name=input("请输入学生姓名：")
            ch_score=input("请输入语文成绩：")
            math_score=input("请输入数学成绩：")
            english_score=input("请输入英语成绩：")
            stu_info[name]={'ch':ch_score,'math':math_score,'english':english_score}
            print("添加成功")
        case '2':#修改
            name=input("请输入学生姓名：")
            if name in stu_info:
                ch_score=input("请输入语文成绩：")
                math_score=input("请输入数学成绩：")
                english_score=input("请输入英语成绩：")
                stu_info[name]={'ch':ch_score,'math':math_score,'english':english_score}
                print("修改成功")
            else:
                print("该学生不存在教务系统中")
        case '3':#删除
            name=input("请输入学生姓名：")
            if name in stu_info:
                del stu_info[name]
                print("删除成功")
            else:
                print("该学生不存在教务系统中")
        case '4':#查询
            name=input("请输入学生姓名：")
            if name in stu_info:
                for stu_name , info in stu_info:
                    print(f"姓名：{stu_name}  语文成绩：{info['ch']}  数学成绩：{info['math']}  英语成绩：{info['english']}")
            else:
                print("该学生不存在教务系统中")
        case '5':#列出所有学生
            print('所有学生信息如下：')
            print('姓名\t语文成绩\t数学成绩\t英语成绩')
            for stu_name , info in stu_info.items():
                print(f"{stu_name}\t{info['ch']}\t{info['math']}\t{info['english']}")
        case '6':#统计成绩(语 数 英分别的最高 最低 平均分并列出最高最低学生姓名)
            chi=[]
            math=[]
            eng=[]
            for stu_name , info in stu_info.items():
                chi.append(info['ch'])
                math.append(info['math'])
                eng.append(info['english'])
            print(f"语文最高分：{max(chi)}  最低分：{min(chi)}  平均分：{sum(chi)/len(chi)}")
            print(f"数学最高分：{max(math)}  最低分：{min(math)}  平均分：{sum(math)/len(math)}")
            print(f"英语最高分：{max(eng)}  最低分：{min(eng)}  平均分：{sum(eng)/len(eng)}")
            chitop_name=[stu_name for stu_name , info in stu_info.items() if info['ch']==max(chi)]
            print(f"语文最高分学生姓名：{chitop_name}")
            mathitop_name=[stu_name for stu_name , info in stu_info.items() if info['math']==max(math)]
            print(f"数学最高分学生姓名：{mathitop_name}")   
            engtop_name=[stu_name for stu_name , info in stu_info.items() if info['english']==max(eng)]
            print(f"英语最高分学生姓名：{engtop_name}")
            chibottom_name=[stu_name for stu_name , info in stu_info.items() if info['ch']==min(chi)]
            print(f"语文最低分学生姓名：{chibottom_name}")
            mathbottom_name=[stu_name for stu_name , info in stu_info.items() if info['math']==min(math)]
            print(f"数学最低分学生姓名：{mathbottom_name}")
            engbottom_name=[stu_name for stu_name , info in stu_info.items() if info['english']==min(eng)]
            print(f"英语最低分学生姓名：{engbottom_name}")
        case '7':#退出
            break
        case _:
            print("输入有误，请重新输入")
