# importing the required modules  
import tkinter as tk  
import datetime as dt  
import time  
import winsound as ws

# defining the function for the alarm clock  
def alarm(setAlarmTimer,tick=True):  
    while tick==True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        print_time = "Current Time: " + str(currentTime)  
        print(print_time)  
        if currentTime == setAlarmTimer:  
            print("It's Time To Wake Up!!\n")
            freq=1500
            duration=1000
            for i in range(5):
                ws.Beep(freq,duration)
                print("WAKE UP!!!!!!\n")
                #ws.PlaySound("SystemHand",ws.SND_ASYNC)
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
        elif currentTime >= setAlarmTimer:
            print("You have crossed the time. Please set another alarm!")
            break
            

  
def getAlarmTime():  
    alarmtime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmtime,tick=True)  



# creating the GUI for the application  
guiWindow = tk.Tk()  
guiWindow.title("Alarm Clock")  
guiWindow.geometry("400x200")  
guiWindow.config(bg = "#87BDD8")  
guiWindow.resizable(width = False, height = False)  
   
timeFormat = tk.Label(  
    guiWindow,  
    text = "Remember to set time in 24-hour format!",  
    fg = "White",  
    bg = "#36486B",  
    font = ("Times", 15, "bold italic underline")  
    ).place(  
        x = 45,  
        y = 170  
        )  
   
add_time = tk.Label(  
    guiWindow,  
    text = "  Hour       Minutes   Seconds",  
    font = 10,  
    fg = "white",  
    bg = "#87BDD8"  
    ).place(  
        x = 200,  
        y = 30  
        )  
  
setAlarm = tk.Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#034F84",  
    relief = "solid",  
    font = ("Courier", 11)  
    ).place(  
        x = 5,  
        y = 55  
        )  
   
hour = tk.StringVar()  
minute = tk.StringVar()  
second = tk.StringVar()  
   
hourTime = tk.Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(  
        x = 200,  
        y = 55  
        )  
minuteTime = tk.Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(  
        x = 265,  
        y = 55  
        )  
secondTime = tk.Entry(  
    guiWindow,  
    textvariable = second,  
    bg = "#FEFBD8",  
    width = 6,  
    font = (20)  
    ).place(  
        x = 329,  
        y = 55  
        )  


submit = tk.Button(  
    guiWindow,  
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#82B74B",  
    width = 15,  
    command = getAlarmTime,  
    font = (25)  
    )
submit.place(  
        x = 200,  
        y = 100  
        )
 
guiWindow.mainloop()  
