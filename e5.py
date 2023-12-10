import time

def focus_timer(minutes):
    seconds = minutes * 60
    while True:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
        print("Time's up!")
        
        # 重置计时器
        seconds = minutes * 60

# 设置初始专注时长为25分钟
focus_timer(25)
