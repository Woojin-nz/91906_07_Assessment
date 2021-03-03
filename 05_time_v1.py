import time

t=30

def countdown(t):
    while t:
        secs = t
        timer="{:02d}".format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print(t)
    print("Time Over!")


countdown(t)