#keys are the rooms, values are the doors
rooms = {
               '1' : ['1','2', '3'],
               '2' : ['1','2', '3'],
               '3' : ['1', '2', '3']
             }
gameOver = False
#returns the current Room
def roomManager(currentRoom, doorSelected):
    global gameOver
    #sets the next room the sum of door and the current room
    nextRoom = int(currentRoom) + int(doorSelected)
    #checks if the next room is the last room or the exit
    if(nextRoom == len(rooms)):
      gameOver = True
      currentRoom = "Escaped"
      print("You have", currentRoom)
    #checks if the value of the door equals the room number
    #means the next room is the current room (door leads player in a circle)
    elif(nextRoom - int(currentRoom) == 1):
      nextRoom = 0
      return currentRoom
    else:
      if (nextRoom - int(currentRoom)) > int(currentRoom):
        #checks if a door selected leads to a room not in the dictionary
        if(int(nextRoom) > len(rooms)):
          gameOver = True
          currentRoom = "Sunken Place"
          print("You have entered in the", currentRoom)
          nextRoom = 0
          return currentRoom
        #sets the next room to the current room
        else:
          currentRoom = nextRoom
          nextRoom = 0
          return currentRoom
def main():
  currentRoom = '1'
  while not gameOver:
    print("You are in currently in Room ", currentRoom)
    doorSelected = input("What Door: ")
    currentRoom = roomManager(currentRoom, doorSelected)
main()
