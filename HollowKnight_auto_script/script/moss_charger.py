import time
from pykeyboard import PyKeyboard

# 护符：力量、快劈、修长、挽歌

k = PyKeyboard()

def attack():
    k.press_key('J')  # 按下
    time.sleep(0.04)         
    k.release_key('J')  # 释放
    time.sleep(0.04)  

def move_right():
    k.press_key('D')  # 按下
    time.sleep(0.02)         
    k.release_key('D')  # 释放
    # time.sleep(0.02)

def move_left():
    k.press_key('A')  # 按下
    time.sleep(0.02)         
    k.release_key('A')  # 释放
    # time.sleep(0.02)     

def main():    
    # 进入游戏
    time.sleep(1) #
    k.press_key('W')  # 按下
    time.sleep(0.05)         
    k.release_key('W')  # 释放
    time.sleep(0.5)
    k.press_key('K')  # 按下
    time.sleep(0.05)         
    k.release_key('K')  # 释放

    num = 400 # 挥刀次数
    for i in range(num):
        attack()
        

if __name__ == '__main__':
    main()




