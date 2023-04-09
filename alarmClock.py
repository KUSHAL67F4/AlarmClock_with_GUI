# importing the required modules  
from tkinter import *  
import datetime as dt  
import time  
import winsound as ws

# defining the function for the alarm clock  
def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:  
            print("Time's up. Wake up!!")
            freq=1500
            duration=800
            '''for i in range(7):
                for j in range(2):
                    ws.Beep(freq,duration)'''
            for i in range(5):
                ws.PlaySound("SystemHand",ws.SND_ASYNC)
                time.sleep(2)
            '''ws.PlaySound("SystemHand",ws.SND_ASYNC)
            time.sleep(3)
            ws.PlaySound("SystemHand",ws.SND_ASYNC)
            time.sleep(3)
            ws.PlaySound("SystemHand",ws.SND_ASYNC)
            time.sleep(3)
            ws.PlaySound("SystemHand",ws.SND_ASYNC)'''
            print("\n \nSet Another Alarm")  
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime)  



# creating the GUI for the application  
guiWindow = Tk()  
guiWindow.title("Alarm Clock")  
guiWindow.geometry("500x200")  
guiWindow.config(bg = "#87BDD8")  
guiWindow.resizable(width = False, height = False)  
   
timeFormat = Label(  
    guiWindow,  
    text = "Remember to set time in 24-hour format!",  
    fg = "black",  
    bg = "#36486B",  
    font = ("Times", 15, "bold italic underline")  
    ).place(  
        x = 75,  
        y = 170  
        )  
   
add_time = Label(  
    guiWindow,  
    text = "Hour          Minute        Second",  
    font = 60,  
    fg = "white",  
    bg = "#87BDD8"  
    ).place(  
        x = 240,  
        y = 20  
        )  
  
setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#034F84",  
    relief = "solid",  
    font = ("Courier", 12)  
    ).place(  
        x = 5,  
        y = 55  
        )  
   
hour = StringVar()  
minute = StringVar()  
second = StringVar()  
   
hourTime = Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(  
        x = 230,  
        y = 53  
        )  
minuteTime = Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(  
        x = 310,  
        y = 53  
        )  
secondTime = Entry(  
    guiWindow,  
    textvariable = second,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(  
        x = 390,  
        y = 53  
        )  
   
submit = Button(  
    guiWindow,  
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#82B74B",  
    width = 15,  
    command = getAlarmTime,  
    font = (25)  
    ).place(  
        x = 220,  
        y = 100  
        )  
   
guiWindow.mainloop()  