import os, ctypes
from pyautogui import *
from time import sleep
from datetime import datetime
import webbrowser as wb


class SleepInhibitor:
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001

    def __init__(self):
        pass

    def inhibit(self):
        ctypes.windll.kernel32.SetThreadExecutionState(
            SleepInhibitor.ES_CONTINUOUS | \
            SleepInhibitor.ES_SYSTEM_REQUIRED)

    def uninhibit(self):
        ctypes.windll.kernel32.SetThreadExecutionState(
            SleepInhibitor.ES_CONTINUOUS)


def msg_send():
    wb.open("https://web.whatsapp.com/") #Whatsapp web, pre logged in
    sleep(10)
    click(190, 256) #Search Box
    sleep(1)
    typewrite("Friends") #Name/Number/Grp name
    sleep(1)
    press('enter')
    sleep(1)
    typewrite("Happy Birthday ") #Type message
    typewrite("@john doe", interval=0.25)# @mention
    click(800, 896) #click for @mention
    sleep(1) #Send message
    press('enter')
    sleep(1)
    click(654, 968) #Emoji/Sticker button
    sleep(1)
    click(810, 968) #Sticker button
    sleep(1)
    click(1320, 665) #Sticker-4
    sleep(2)
    click(706, 968) #Emoji button
    sleep(1)
    click(815, 557) #Emoji category-1(Smileys)
    sleep(1)
    click(1315, 784) #Emoji-34
    sleep(1)
    press('enter') #Send emoji
    sleep(10)
    click(1891, 18) #Close Browser


#prevent Windows from going to sleep
osSleep = None
if os.name == 'nt':
    osSleep = SleepInhibitor()
    osSleep.inhibit()

#Timer
x = datetime.now()
y = x.replace(hour=23, minute=59, second=0)
time = y - x
sec = time.seconds + 1
sleep(sec)
#Send Message
msg_send()

#Windows sleep settings back to normal
if osSleep:
    osSleep.uninhibit()
