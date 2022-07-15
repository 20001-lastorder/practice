age = 17
name1 = "胡桃"
name2 = "空"
character_id = 1
height = 160.52

# %d 有符号整形 %s 字符串 %f 浮点型 %u 无符号整形

# \n 换行 \t 制表
print("欢迎来到\n\r\t提瓦特大陆！")

# 用end="结束符" 输出结束方式
print("-----------\n\r正在载入数据", end="。。。")

# 直接输出 使用 f"{表达书}" 代替 %s 输出
print("载入角色：%s" % name2)
print(f"老婆{name1}，今年{age}岁，身高{height}cm")

# 格式化补零输出 %0x x表示总位数，不足的用0补全，超出原样输出
print("是我的%03d号老婆" % character_id)

# 输出多个数据
print("%s明年%d岁了" % (name1, age + 1))

# 格式化保留小数，%.x x表示小数位数
print("老婆今年%.1fcm" % height)

