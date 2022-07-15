# input得到的数据视作字符串

character = input("名字：")
# print(character)

# 强制类型转换 int（） tuple（） list（）
age = input("年龄：")
print(type(int(age)))

list1 = [10, 20, 30]
print(tuple(list1))

# eval（str）自动识别字符串中的有效python类型，并返回一个对象
str1 = "1"
str2 = "1.1"
str3 = "[1, 2, 3]"
print(type(eval(str3)))
