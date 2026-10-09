dict1={'张三':600,'李四':587,'王五':529}
print(dict1)
print(type(dict1))
print(dict1['李四'])

#增加
dict1['刘流']=234
print(dict1)

dict1['张三']=478
print(dict1)

#查询
print(dict1.get('张三'))
print(dict1['张三'])

print(dict1.keys())
print(dict1.values())
print(dict1.items())

#删除
score1=dict1.pop('刘流')
print(score1)
print(dict1)

del dict1['李四']
print(dict1)

for key in dict1.keys():
    print(key)


