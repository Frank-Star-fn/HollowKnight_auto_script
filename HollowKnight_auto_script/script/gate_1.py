import time
from pykeyboard import PyKeyboard
import pyautogui

# 全自动通关神居一门
# 护符：深聚、快聚、虫歌、编织者、荆棘
# 非常适用的boss：
# 反击蝇、格鲁兹、假骑士、苔藓、
# 大黄蜂、戈布、芬达哥、毛里克

# 适用的boss：灵魂战士

# 比较适用的boss：奥罗马托(二阶段有概率失败)

k = PyKeyboard()

def attack():
    k.press_key('J')  # 按下
    time.sleep(0.04)         
    k.release_key('J')  # 释放
    time.sleep(0.04)  

def attack2():
    k.press_key('J')  # 按下
    time.sleep(0.04)         
    k.release_key('J')  # 释放

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

def jump():
    k.press_key('K')  # 按下
    time.sleep(0.3)         
    k.release_key('K')  # 释放

def dash():
    k.press_key('L')  # 按下
    time.sleep(0.2)         
    k.release_key('L')  # 释放

def observe_fake_knight():
    is_fake_knight = pyautogui.locateOnScreen('./locator/fake_knight.png',
                                           confidence=0.8)        
    is_fake_knight2 = pyautogui.locateOnScreen('./locator/fake_knight_2.png',
                                           confidence=0.8)       
        
    if is_fake_knight or is_fake_knight2: # 识别到假骑士
        return True
    return False

def observe_fake_knight_lie_to_left():
    is_lie = pyautogui.locateOnScreen('./locator/fake_knight_lie.png',
                                           confidence=0.8)  
    is_lie2 = pyautogui.locateOnScreen('./locator/fake_knight_lie_2.png',
                                           confidence=0.8)        
    if is_lie or is_lie2: # 识别到假骑士被击倒
        return True
    return False

def observe_moss():
    is_moss = pyautogui.locateOnScreen('./locator/moss.png',
                                           confidence=0.8) 
    is_moss2 = pyautogui.locateOnScreen('./locator/moss_2.png',
                                           confidence=0.8) 
    if is_moss or is_moss2: # 识别到大型苔藓冲锋者
        return True
    return False

def observe_soul_warrior():
    is_soul_warrior = pyautogui.locateOnScreen('./locator/soul_warrior.png',
                                           confidence=0.8)
    is_soul_warrior2 = pyautogui.locateOnScreen('./locator/soul_warrior_2.png',
                                           confidence=0.8)
    
    if is_soul_warrior or is_soul_warrior2: # 识别到灵魂战士
        return True
    return False

def observe_mawlek():
    is_mawlek = pyautogui.locateOnScreen('./locator/mawlek.png',
                                           confidence=0.8)   
    is_mawlek_2 = pyautogui.locateOnScreen('./locator/mawlek_2.png',
                                           confidence=0.8)  
    if is_mawlek or is_mawlek_2: # 识别到毛里克
        return True
    return False

def observe_end_gate():
    is_end = pyautogui.locateOnScreen('./locator/gate_1_outside.png',
                                           confidence=0.85)       
    if is_end: # 识别战斗结束
        return True
    return False


def _find_window():
        """
        find the location of Hollow Knight window

        :return: return the monitor location for screenshot
        """
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

def enter_gate():
    k.press_key('W')  # 按下
    time.sleep(0.2)         
    k.release_key('W')  # 释放
    time.sleep(1)
    k.press_key('W')  # 按下
    time.sleep(0.2)         
    k.release_key('W')  # 释放
    time.sleep(0.8)
    k.press_key('K')  # 按下
    time.sleep(0.1)         
    k.release_key('K')  # 释放

def enter_single_boss():
    k.press_key('W')  # 按下
    time.sleep(0.1)         
    k.release_key('W')  # 释放
    time.sleep(0.6)
    k.press_key('K')  # 按下
    time.sleep(0.1)         
    k.release_key('K')  # 释放

def main():    
    loc = _find_window()

    # 进入游戏
    enter_gate()
    # enter_single_boss()

    num = 5000 # 循环次数，足够大
    for i in range(num):
        if observe_fake_knight():
            break
        print("i =",i) # 
        attack2()
        fast_deep_heal() # 回血
    

    #
    print("打假骑士")
    num = 5000 # 循环次数，足够大
    num2= 70
    for i in range(num):
        if observe_moss():
            break
        if observe_fake_knight_lie_to_left():
            keep_right() # 一直往右
            for j in range(num2):
                print("j =",j) # 
                attack()
            move_right()
        
        print("i =",i) # 
        attack2()
        fast_deep_heal() # 回血
        move_left() # 往左
        dash()
        

    #
    print("打大型苔藓冲锋者")
    num = 10000 # 循环次数，足够大
    for i in range(num):
        if observe_soul_warrior():
            break
        print("i =",i) # 
        attack2()
        fast_deep_heal() # 回血

    #
    print("打灵魂战士")
    keep_right() # 一直往右
    num = 2000 # 循环次数
    for i in range(num):
        if observe_mawlek(): # 进入毛里克
            break
        print("i =",i) # 
        jump()
        time.sleep(0.1)
    # 释放右键
    move_right()
    
    # 打毛里克和奥罗马托
    print("打毛里克")
    num = 10000 # 循环次数，足够大
    for i in range(num):
        if observe_end_gate():
            break
        print("i =",i) # 
        attack2()
        fast_deep_heal() # 回血

    #
    print("end")

if __name__ == '__main__':
    main()


