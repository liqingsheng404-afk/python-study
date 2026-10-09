shopping_car={}
manu="""
##########购物车系统##########
#       1.添加购物车         #
#       2.修改购物车         #
#       3.删除购物车         #
#       4.查询购物车         #
#       5.退出购物车         #
##############################
"""
while True:
    print('欢迎使用购物车管理系统!')
    print(manu)
    num=input('请选择操作编号(1-5):')
    match num:
        case '1':#添加
            goods_name= input('请输入商品名称:')
            goods_prise = float(input('请输入商品价格:'))
            goods_num = int(input('请输入商品数量:'))

            if goods_name in shopping_car:
                print('该商品已存在!')
            else:
                shopping_car[goods_name] = {'prise':goods_prise, 'num':goods_num}
                print('商品添加完毕')
        case '2':#修改
            goods_name = input('请输入商品名称:')
            if goods_name not in shopping_car:
                print('该商品不存在,请添加后再查询')
            else:
                goods_prise = float(input('请输入商品价格:'))
                goods_num = int(input('请输入商品数量:'))
                shopping_car[goods_name] = {'prise':goods_prise, 'num':goods_num}
                print('商品已修改')
        case '3':#删除
            goods_name = input('请输入商品名称:')

            if goods_name not in shopping_car:
                print('该商品不存在,无法删除!')
            else:
                del shopping_car[goods_name]
                print('商品已删除')
        case '4':#查询
            for goods_name, goods_info in shopping_car.items():
                print(f'商品名称:{goods_name}\t\t商品价格:{goods_info["prise"]}\t\t商品数量:{goods_info["num"]}')
        case '5':#退出
            print('byb~')
            break
        case _:
            print('请输入正确的编号!')








