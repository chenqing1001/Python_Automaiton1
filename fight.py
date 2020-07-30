"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

def fight():  # 定义一个函数
    my_hp = 1000 # 我的初始血量是1000
    my_power = 200 # 我的攻击力是200
    your_hp = 900 # 敌人的初始血量是1000
    your_power = 200 # 敌人的攻击力是200

    while(True): #  只要没有break，就一直循环
        my_hp = my_hp - your_power # 每次循环，我的剩余血量=我的初始血量-敌人的攻击力
        your_hp = your_hp - my_power# 每次循环，敌人的剩余血量=敌人的初始血量-我的攻击力
        if(my_hp <= 0 ): # 如果我的剩余血量小于等于0
            print("敌人赢了") # 打印敌人赢了
            print(f"我的剩余血量是:{my_hp}") # 打印我的剩余血量
            print(f"敌人的剩余血量是:{your_hp}") # 打印敌人的剩余血量
            break  # 并且跳出循环，不再执行循环中的语句
        elif(your_hp<= 0 ): # 如果敌人的剩余血量小于等于0
            print("我赢了") # 打印我赢了
            print(f"我的剩余血量是:{my_hp}")  # 打印我的剩余血量
            print(f"敌人的剩余血量是:{your_hp}") # 打印敌人的剩余血量
            break

fight() # 调用函数