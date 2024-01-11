from tkinter import *
import time
from tkinter import messagebox
# "*" represents everything that we need in the tkinter library 
# To make the window
window = Tk()
window.title("              Live Score GUI App")

myLabel1 = Label(window, text = "Enter Team 1 Below").grid(row = 0, column = 0)
myLabel2 = Label(window, text = "Enter Team 2 Below").grid(row = 0, column = 1000)

e_1 = Entry(window, width = 10, borderwidth = 5).grid(row = 1, column = 0)
e_2 = Entry(window, width = 10, borderwidth = 5).grid(row = 1, column = 1000)

#Making timer through making different entry widgets for sec, hrs, min
secs = StringVar()
mins = StringVar()
hrs = StringVar()

secs.set("00")
mins.set("00")
hrs.set("00")

hourTextbox = Entry(window, width = 3, borderwidth = 5, textvariable = hrs)
minuteTextbox = Entry(window, width = 3, borderwidth = 5, textvariable = mins)
secondTextbox = Entry(window, width = 3, borderwidth = 5, textvariable = secs)

hourTextbox.grid(row = 2, column = 1)
minuteTextbox.grid(row = 2, column = 2)
secondTextbox.grid(row = 2, column = 3)

def runTimer():
  try:
    global clockTime
    clockTime = int(hrs.get())*3600 + int(mins.get())*60 + int(secs.get())
  except: 
    print("Incorrect values")

  while clockTime > -1:
    totalMinutes, totalSeconds = divmod(clockTime, 60)
    totalHours = 0 
    if (totalMinutes > 60):
      totalHours, totalMinutes = divmod(totalMinutes, 60)

    hrs.set("{0:2d}".format(totalHours))
    mins.set("{0:2d}".format(totalMinutes))
    secs.set("{0:2d}".format(totalSeconds))

    window.update()
    time.sleep(1)
  
    if clockTime == 0:
      messagebox.showinfo("Time's Up", "Time's Up")
  
    clockTime -= 1
  winner()
#The Button to start the timer
buttonTimer = Button(window, text = "Start Timer", command = runTimer).grid(row = 3, column = 2)

#Label that displays what to do to set the timer
indication_label = Label(window, text = "Set the Timer").grid(row = 0, column = 2)
hrs_label = Label(window, text = "Hours").grid(row = 1, column = 1)
mins_label = Label(window, text = "Minutes").grid(row = 1, column = 2)
secs_label = Label(window, text = "Seconds").grid(row = 1, column = 3)
#This is a function that will help add the goals
score_1 = 1
def myClick_1():
  global score_1
  global label_1
  label_1 = Label(window, text = score_1, font = "Helvetica 12").grid(row = 3, column = 0)
  score_1 += 1

score_2 = 1
def myClick_2():
  global score_2
  global label_2
  label_2 = Label(window, text = score_2, font = "Helvetica 12").grid(row = 3, column = 1000)
  score_2 += 1

def myClick_remove_1():
  global score_1
  global label_1
  label_1 = Label(window, text = score_1, font = "Helvetica 12").grid(row = 3, column = 0)
  if score_1 >= 1:
    score_1 -= 1


def myClick_remove_2():
  global score_2
  global label_2
  label_2 = Label(window, text = score_2, font = "Helvetica 12").grid(row = 3, column = 1000)
  if score_2 >= 1:
    score_2 -= 1
  

def winner():
  if score_1 > score_2:
    team_1Winner = Label(window, text = "Team 1 Wins!", font = "Helvetica 12").grid(row = 4, column = 2)
  elif score_1 < score_2:
    team_2Winner = Label(window, text = "Team 2 Wins!", font = "Helvetica 12").grid(row = 4, column = 2)
  else:
    tieBreaker = Label(window, text = "Tie!", font = "Helvetica 12").grid(row = 4, column = 2)

#These are the buttons to add the goals
btn_1 = Button(window, text = "Goal", bg = "red", fg = "white", padx = 50, pady = 10, command = myClick_1).grid(row = 10, column = 0)
btn_2 = Button(window, text = "Goal", bg = "Blue", fg = "white", padx = 50, pady = 10, command = myClick_2).grid(row = 10, column = 1000)


#Button to remove 
btn_1_removal = Button(window, text = "Remove Goal", bg = "red", fg = "white", padx = 50, pady = 10, command = myClick_remove_1).grid(row = 11, column = 0) 
btn_2_removal = Button(window, text = "Remove Goal", bg = "blue", fg = "white", padx = 50, pady = 10, command = myClick_remove_2).grid(row = 11, column = 1000)

#UI's need loops to keep the window working 
window.mainloop()



