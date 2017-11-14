# level 1 terrain : write column by column, ex: [ [0,1,0], [2,1,0] ] is a 2x3 terrain
height = [[0,2,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0], [0,2,1,0]]

isBlue = [ [True,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,True] ]

isOn = [ [False,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,True] ]





#start by initializing the lightbot status variables
x = 0 # x position x-coordinate
y = 0 # y position y-coordinate
yon = 0 # which way lbot is facing 
direction = {0:'north', 1:'east', 2:'south', 3:'west'}

maxX = len(height)-1 # max possible value of the x coordinate
maxY = len(height[0])-1 # max possible value of the y coordinate

def heightDifferenceForward(x,y):
    if yon == 0 and y < maxY:
        return height[x][y+1] - height[x][y]
    elif yon == 2 and y < maxY:
        return height[x][y-1] - height[x][y]
    elif yon == 1 and x < maxX:
        return height [x+1][y] - height [x][y]
    elif yon == 3 and x < maxX:
        return height [x-1][y] - height [x][y]
    
        return 0
    

komut = ""
while komut != "q": # repeat  as long as we don't get the quid command 
    print("Enter a command")
    komut = input()

    if komut==">":
      print("I am turning right")
      yon = (yon+1)%4

    elif komut=="<":
      print("I am turning left")
      yon = (yon-1)%4

    elif komut =="^":    
      print("I am moving forward")
      if yon == 0:
          if y < maxY:
              y = y + 1
      elif yon == 2:
        if y == 0:
            print("I can not move forward")
            y = y
        elif y < maxY:
              y = y - 1
      elif yon == 1:
          if x < maxX:
              x = x + 1
      elif yon == 3:
        if x == 0:
            print("I can not move forward")
            x = x
        elif x < maxX:
              x = x - 1
 
    elif komut=="@":
      if( isBlue[x][y] == True ):
         print("I am switching on or off")
         # isOn[x][y] = not isOn[x][y]
         if ( isOn[x][y] == True ):
              isOn[x][y] = False
         else:
          isOn[x][y] = True
        
      else:
          print("You are trying to light up a gray box. I can't do it")
        

    elif komut != "q":
      print("This command is not known")

print("As I exit now, my orientation is",direction[yon])
print("My position is", height[x][y])
