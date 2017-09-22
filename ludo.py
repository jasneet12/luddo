#
# ================================================= 
#    Configuration Settings
# =================================================
#
# Width Of All Boxes
S_WIDTH=36



# Height Of All Boxes
S_HEIGHT=36

# Number Of Boxes
AREA = 15


# =================================================
#     Colors Settings
# =================================================
#
# Track Color
C_0_A = "SkyBlue3" # When Active
C_0_D = "SkyBlue2" # when Deactive

# TEAM 
C_1 = "Blue"   # Default
C_1_A = "RoyalBlue2" # When Active
C_1_D = "RoyalBlue1" # When Deactive


C_2 = "red"
C_2_A = "firebrick2" 
C_2_D = "firebrick1"


C_3 = "green"
C_3_A = "green2" 
C_3_D = "green1"


C_4 = "yellow"
C_4_A = "yellow2" 
C_4_D = "yellow1"


# List Of Active Colors
COLOR = [C_1_A, C_2_A, C_3_A, C_4_A]







#
#
# Import Module
from GameConfig import *


# Function For Track Coordinates Calculations
def tracks(s, r):
 return [s.format(i) for i in r]

# Creating Main Track Square Boxes
TRACK = []
TRACK+= tracks("6.{}", range(6))[::-1]
TRACK+= ['7.0']
TRACK+= tracks("8.{}", range(6))
TRACK+= tracks("{}.6", range(9,15))
TRACK+= ['14.7']
TRACK+= tracks("{}.8", range(9,15))[::-1]
TRACK+= tracks("8.{}", range(9,15))
TRACK+= ['7.14']
TRACK+= tracks("6.{}", range(9,15))[::-1]
TRACK+= tracks("{}.8", range(6))[::-1]
TRACK+= ['0.7']
TRACK+= tracks("{}.6", range(6))




# Creating Ending Tracks
F_TRACK=[]
F_TRACK.append(tracks("7.{}", range(1,7)))
F_TRACK.append(tracks("{}.7", range(8,14))[::-1])
F_TRACK.append(tracks("7.{}", range(8,14))[::-1])
F_TRACK.append(tracks("{}.7", range(1,7)))

# Now Creating Roots
TRAIN_1=TRACK[8:]+TRACK[:7]+F_TRACK[0]+['7.6']  # ROOT One
TRAIN_2=TRACK[21:]+TRACK[:20]+F_TRACK[1]+['8.7'] # Root Two
TRAIN_3=TRACK[34:]+TRACK[:33]+F_TRACK[2]+['7.8'] # Root Three
TRAIN_4=TRACK[47:]+TRACK[:46]+F_TRACK[3]+['6.7'] # Root Four

# Station
STATIONS=[]
STATIONS.append(['11.2','12.2','11.3','12.3'])
STATIONS.append(['11.11','12.11','11.12','12.12'])
STATIONS.append(['2.11','3.11','2.12','3.12'])
STATIONS.append(['2.2','3.2','2.3','3.3'])

# TEAM A COINS
TEAM = []
TEAM.append(["C{}".format(i) for i in STATIONS[0]]+["C{}".format(i) for i in STATIONS[3]])
TEAM.append(["C{}".format(i) for i in STATIONS[1]]+["C{}".format(i) for i in STATIONS[2]])
#print TEAM

OVALS = [
(TRAIN_1, STATIONS[0], C_1, "A"),
(TRAIN_2, STATIONS[1], C_2, "B"),
(TRAIN_3, STATIONS[2], C_3, "B"),
(TRAIN_4, STATIONS[3], C_4, "A"),
]



# Stops
STOPS = [
'8.1',
'12.6',
'13.8',
'8.12',
'6.13',
'2.8',
'1.6',
'6.2',
]






# Import Module
try:
 import Tkinter
except:
 import tkinter as Tkinter

from GameConfig import *
from models import *




# Main Class For Canvas Widget
class Board(Tkinter.Canvas):
 def __init__(self, *args, **kwargs):
  Tkinter.Canvas.__init__(self, *args, **kwargs)
  self.create_squares()
  self.highlight()
  self.configure(width=S_WIDTH*AREA, height=S_HEIGHT*AREA)


 # Filling Colors In Boxes
 def highlight(self):

  # Main Tracks
  for c in TRACK:
   self.itemconfigure(c, fill=C_0_D, activewidth=2, activefill=C_0_A, activeoutline="black")

  # Ending Tracks
  for n,k in enumerate(F_TRACK):
   for j in k:
    self.itemconfigure(j, fill=COLOR[n], activewidth=2, activeoutline='black')


  # Stations
  for n,s in enumerate(STATIONS):
   for j,c in enumerate(s):
    self.itemconfigure(c, fill=COLOR[n], activewidth=2)
    coordinates = self.coords(c)
    #store=self.create_oval(*coordinates, fill=COLOR[n], width=3, tag="COIN{}{}".format(n,j))
    #self.tag_bind(store,"<Enter>",self.coin_bind)
#    print n,s,j,c
  
  # Stops
  for s in STOPS:
   self.itemconfigure(s, fill="gray58", activefill="gray70", activewidth=3, activeoutline="gray10")
  return

 # Creating Square Boxes
 def create_squares(self):
  for i in range(AREA):
   for j in range(AREA):
    self.create_rectangle(S_WIDTH*i, S_HEIGHT*j, (S_WIDTH*i)+S_WIDTH,(S_HEIGHT*j)+S_HEIGHT, tag="{}.{}".format(i,j), outline='white', fill="ivory")
#    self.create_text(S_WIDTH*i+20, S_HEIGHT*j+20, text="{}.{}".format(i,j))
  return


# main Trigger
if __name__=="__main__":
 root = Tkinter.Tk()
 c = Board(root, width=S_WIDTH*AREA, height=S_HEIGHT*AREA)
 c.pack(expand=True, fill="both")
 root.mainloop()





 #
#
# Import Module
try:
 import Tkinter
except:
 import tkinter as Tkinter

import random
from views import Board
from models import TRACK, OVALS, TEAM, F_TRACK


# Frame Of Dice Function
class Dice(Tkinter.Frame):
 def __init__(self,root, s):
  Tkinter.Frame.__init__(self,root)
  self.string = s
  self.string.set(6)
  self.create_widget()
 #
 def round(self):
  self.string.set(random.randint(1,6))
  self.button.config(state="disable")
  return

 def create_widget(self):
  store = Tkinter.Label(self, textvariable=self.string,width=20)
  store.pack(fill='both')
  self.button = Tkinter.Button(self, text="Team A", command=self.round)
  self.button.pack(fill='both')
  return




# Frame Of ScoreBoard
class ScoreBoard(Tkinter.LabelFrame):
 def __init__(self, *args, **kwargs):
  Tkinter.LabelFrame.__init__(self, *args, **kwargs)
  self['padx']=20
  self['pady']=20
  self.create_label()

 # Creating Label
 def create_label(self):
  Tkinter.Label(self, text="Team A", bg="RoyalBlue1").grid(row=1, column=1)
  Tkinter.Label(self, text="Team B", bg="yellow2").grid(row=2, column=1)
  self.team_a=Tkinter.Label(self, text="0")
  self.team_a.grid(row=1, column=2)
  self.team_b=Tkinter.Label(self, text="0")
  self.team_b.grid(row=2, column=2)
  return




# Creating Main Engine 
class Engine:
 def __init__(self, canvas):
  self.canvas = canvas
  #self.ovals=[]
  self.create_ovals()
  self.turn = "A"
  self.number = Tkinter.IntVar()
  self.add_dice()
  self.score_board()


 # Add Dice Frame
 def add_dice(self):
  self.dice=Dice(self.canvas.master, self.number)
  self.dice.pack(side='left')
  return


 #Add Score Board
 def score_board(self):
  self.score=ScoreBoard(self.canvas.master, text="Score")
  self.score.pack(side='right')
  return

 # Creating Ovals
 def create_ovals(self):
  self.oval_identity=[]
  for a,b,c,d in OVALS:
   for i in b:
    s=self.canvas.create_oval(*self.getcoordinates(i), fill=c, tag="C{}".format(i), activewidth=3)
    self.oval_identity.append("C{}".format(i))
    self.canvas.tag_bind(s, "<Button-1>", self.oval_triggers)
  
  return

 
 # Oval Binding Handler
 def oval_triggers(self, event):
  tag = self.selected_oval(event)
  if tag and (self.number.get()!=0):
   # Team A
   if self.turn =="A":
    if tag in TEAM[0]:
     
     # TEAM A PLAYERS
     self.team_a_moves(tag)


   # Team B
   else:
    if tag in TEAM[1]:
     
     # TEAM B PLAYERS
     self.team_b_moves(tag)
  return


 # Uplifting Ovals
 def uplifting(self, team):
  for a,b,c,d in OVALS:
   # a = Track
   # b = Station
   # c = Color
   # d = Team
   for s in b:
    tag=str("C"+s)
    if (d==team) and tag:
     # uplift here
     self.canvas.lift(tag)
  return

 # Team A Moves
 def team_a_moves(self, tag):
  for a,b,c,d in OVALS:
   # a = Track
   # b = Station
   # c = Color
   # d = Team
   for s in b:
    if str("C"+s)==tag:
     step=self.number.get()

     # Open
     if (step==1 or step==6) and not self.gettrackbox(tag):
      self.change_place(tag,a[0])
      print "Change Place to Start"
     
     else:
      print "Check"
      # In Track
      
      t = self.gettrackbox(tag)
      if t:
       present_address = a.index(t)
       print t, a[-2]
       if t==a[-2]:
        self.score.team_a.config(text=str(int(self.score.team_a.cget("text"))+1))
        self.canvas.delete(tag)
       try:
        self.change_place(tag,a[present_address+step])
        #self.check_turns()
       except:
        pass
       t = self.gettrackbox(tag)
       if t==a[-2]:
        print "One Coin Clear"
        # One Coin Clear
        self.canvas.delete(tag)
      else:
       self.check_turns()
     return
  return 


 # Team B Moves
 def team_b_moves(self, tag):
  for a,b,c,d in OVALS:
   # a = Track
   # b = Station
   # c = Color
   # d = Team
   for s in b:
    if str("C"+s)==tag:
     step=self.number.get()

     # Open
     if (step==1 or step==6) and not self.gettrackbox(tag):
      self.change_place(tag,a[0])
      print "Change Place to Start"
     
     else:
      print "Check"
      # In Track
      
      t = self.gettrackbox(tag)
      if t:
       present_address = a.index(t)
       print t, a[-2]
       if t==a[-2]:
        self.score.team_b.config(text=str(int(self.score.team_a.cget("text"))+1))
        self.canvas.delete(tag)
       try:
        self.change_place(tag,a[present_address+step])
        #self.check_turns()
       except:
        pass
       t = self.gettrackbox(tag)
       if t==a[-2]:
        print "One Coin Clear"
        # One Coin Clear
        self.canvas.delete(tag)
      else:
       self.check_turns()
    
     return
    else:
     print "not selected"
  return 

 # Shape Movement Handler
 def change_place(self, tag, track):
  a,b,c,d=self.getcoordinates(tag)
  e,f,g,h=self.getcoordinates(track)
  self.canvas.move(tag, g-c, h-d)
  self.check_turns()

  return

 # Get Square Shape Tag on Which Coin Shape Is Lying
 def gettrackbox(self, tag):
  for i in TRACK:
   if self.getcoordinates(i)==self.getcoordinates(tag):
    return i
  for l in F_TRACK:
   for i in l:
    if self.getcoordinates(i)==self.getcoordinates(tag):
     return i
  return 

 # Selected Oval Tag Return
 def selected_oval(self, event=None):
  x , y = event.x, event.y
  for i in self.oval_identity:
   x1,y1,x2,y2 = self.getcoordinates(i)
   if (x1<=x) and (x<=x2) and (y1<=y) and (y<=y2):
    return i

 # Team Turn handlers
 def check_turns(self):
  self.dice.button.config(state="normal")
  self.number.set(0)
  if self.turn == "A":
   self.turn = "B"
   self.dice.button.config(text="Team B")
   self.uplifting("B")
   return 
  else:
   self.turn = "A"
   self.dice.button.config(text="Team A")
   self.uplifting("A")
   return 

 # Get Tag Coordinates In Canvas
 def getcoordinates(self, tags):
  return self.canvas.coords(tags)




# Main Trigger
if __name__=="__main__":
 root=Tkinter.Tk()
 d=Board(root)
 d.pack()
 e=Engine(d)
 root.mainloop()
