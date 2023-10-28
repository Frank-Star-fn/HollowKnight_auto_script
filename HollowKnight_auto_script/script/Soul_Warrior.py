import time
from pykeyboard import PyKeyboard

# 护符：深聚、快聚、虫歌、编织者、荆棘
# 适用的boss：灵魂战士

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

def move_left(): 
    k.press_key('A')  # 按下
    time.sleep(0.02)         
    k.release_key('A')  # 释放

def keep_right():
    k.press_key('D')  # 按下

def jump():
    k.press_key('K')  # 按下
    time.sleep(0.1)         
    k.release_key('K')  # 释放

def fast_deep_heal(): # 深聚快聚回血
    k.press_key('U')  # 按下
    time.sleep(1.55) # 按住
    k.release_key('U')  # 释放

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

    keep_right() # 一直往右
    num = 1600 # 循环次数
    for i in range(num):
        print("i =",i) # 
        jump()
        time.sleep(0.1)

if __name__ == '__main__':
    main()


