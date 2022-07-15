import random
"""
name = input("name: ")
if (name == "神里绫华") or (name == "胡桃"):
    print("老婆！")
# elif name == "胡桃":
#    print("老婆！")
else:
    print("你谁！")
"""
# 猜拳
flag = -1
table = ["剪刀", "石头", "布"]

while flag != 1:
    player = input("请出拳：")
    index = random.randint(0, 2)
    computer = table[index]
    print(f"电脑：{computer}")

    if ((player == "剪刀") and (computer == "剪刀")) or ((player == "石头") and (computer == "石头")) or ((player == "布") and (computer == "布")):
        flag = -1
        print("平局！")
    elif(player == "剪刀") and (computer == "石头") or ((player == "石头") and (computer == "布")) or ((player == "布") and (computer == "剪刀")):
        flag = 0
        print("你输了！")
    elif (player == "剪刀") and (computer == "布") or ((player == "石头") and (computer == "剪刀")) or ((player == "布") and (computer == "石头")):
        flag = 1
        print("你赢了！")
