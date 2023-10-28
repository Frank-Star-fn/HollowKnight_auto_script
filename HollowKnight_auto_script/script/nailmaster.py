import time
from pykeyboard import PyKeyboard
import pyautogui

# 护符：深聚、快聚、虫歌、编织者、荆棘
# 非常适用的boss：
# 反击蝇、格鲁兹、假骑士、苔藓、
# 大黄蜂、戈布、芬达哥、毛里克

# 比较适用的boss：奥罗马托(二阶段有概率失败)

# 不适用的boss：灵魂战士

k = PyKeyboard()

def attack2():
    k.press_key('J')  # 按下
    time.sleep(0.04)         
    k.release_key('J')  # 释放
    # time.sleep(0.04) 

def move_right():
    k.press_key('D')  # 按下
    time.sleep(0.02)         
    k.release_key('D')  # 释放

def move_left(): 
    k.press_key('A')  # 按下
    time.sleep(0.02)         
    k.release_key('A')  # 释放
  
def fast_deep_heal(): # 深聚快聚回血
    k.press_key('U')  # 按下
    time.sleep(1.53) # 按住
    k.release_key('U')  # 释放

def keep_right():
    k.press_key('D')  # 按下

def enter_single_boss():
    k.press_key('W')  # 按下
    time.sleep(0.1)         
    k.release_key('W')  # 释放
    time.sleep(0.6)
    k.press_key('K')  # 按下
    time.sleep(0.1)         
    k.release_key('K')  # 释放

def observe_end():
    is_end = pyautogui.locateOnScreen('./locator/Oro_Mato_end.png',
                                           confidence=0.85)  
    is_end2 = pyautogui.locateOnScreen('./locator/Oro_Mato_end_2.png',
                                           confidence=0.85)  
    is_end3 = pyautogui.locateOnScreen('./locator/Oro_Mato_end_3.png',
                                           confidence=0.85)  
    if is_end or is_end2 or is_end3: # 识别战斗结束
        return True
    return False

def _find_window():
        window = pyautogui.getWindowsWithTitle('Hollow Knight')
        assert len(window) == 1, f'found {len(window)} windows called Hollow Knight {window}'
        window = window[0]
        try:
            window.activate()
        except Exception:
            window.minimize()
            window.maximize()
            window.restore()
        window.moveTo(0, 0) # 移到左上角

        geo = None
        conf = 0.96
        while geo is None:
            geo = pyautogui.locateOnScreen('./locator/geo.png',
                                           confidence=conf)
            conf = max(0.92, conf * 0.99)
            time.sleep(0.1)
            #
            print("conf =", conf)
        #
        print("geo =", geo)

        loc = {
            'left': geo.left - 36,
            'top': geo.top - 97,
            'width': 1020,
            'height': 692
        }
        return loc

def main():    
    loc = _find_window()

    # 进入游戏
    time.sleep(1.5) 
    enter_single_boss()
    time.sleep(1.5) 

    # keep_right() # 一直往右
    num = 5000 # 循环次数，足够大
    for i in range(num):
        if observe_end():
            break
        print("i =",i) # 
        attack2()
        fast_deep_heal() # 回血


if __name__ == '__main__':
    main()


