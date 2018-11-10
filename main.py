import random
#copy code and run in repl.it if needed
#keys are the rooms, values are the doors
roomLayout = {}
gameOver = False
numLives = 3
teleporter = 0
#initalizes floor plan and selects starting room
def floorPlan():
    global roomLayout
    global teleporter
    totalRooms = random.randint(1, 10)
    roomLayout = {roomNum: [] for roomNum in range(1, totalRooms + 1)}
    #populates rooms and doors
    for key in roomLayout:
      #sets the number of doors per room to 3
        while(len(roomLayout[key]) < 3):
            door = random.randint(1, totalRooms)
            #makes sure doors are unique
            if(door not in roomLayout[key]):
              roomLayout[key].append(door)
            #print(roomLayout[key])
    #teleporter implements epsilon (transfer to new room without user input)
    teleporter = random.randint(1, totalRooms)
    #ensures user cannot teleport to accept state
    while(teleporter == len(roomLayout)):
      teleporter = random.randint(1, totalRooms)
    #starts player in random room
    startingRoom = random.choice(list(roomLayout))
    #ensures starting room is not the final room and has at least 4 rooms
    while(startingRoom == len(roomLayout) or int(startingRoom) < 4):
      startingRoom = random.choice(list(roomLayout))
    print('There are', totalRooms, 'rooms in the House. Can you escape?')
    return startingRoom
#returns the current Room
def roomManager(currentRoom, doorSelected):
    global gameOver
    global numLives
    global roomLayout
    #checks if door selected is within the room
    if((int(doorSelected)) not in roomLayout[currentRoom]):
      print("This door does not exist. Please attempt again")
      return currentRoom
    else:
      #sets the next room the sum of door and the current room
      nextRoom = int(currentRoom) + int(doorSelected)
      #loops player back to the same room
      if(int(doorSelected) == int(currentRoom)):
        nextRoom = 0
        return currentRoom
      #checks if the next room is the last room or the exit
      elif(nextRoom == len(roomLayout)):
        gameOver = True
        currentRoom = "Escaped"
        print("You have", currentRoom)
      else:
          #checks if a door selected leads to a room not in the House
          #and all lives have been reduced
          if(int(nextRoom) > len(roomLayout)):
              if(numLives == 0):
                gameOver = True
                currentRoom = "Sunken Place"
                print("You have entered in the", currentRoom)
                nextRoom = 0
                return currentRoom
              else:
                #deductes life
                numLives = numLives - 1
                #moves user to new room (value of door selected)
                currentRoom = int(doorSelected)
                #ensures the user isn't taken to the accept state
                if (int(currentRoom) == len(roomLayout)):
                    #moves user back to room 1
                    currentRoom = 1
                return currentRoom
          #sets the next room to the current room
          else:
            currentRoom = nextRoom
            nextRoom = 0
            return currentRoom

def teleporterManager(currentRoom):
  if(teleporter in roomLayout[currentRoom]):
    return True
  return False

def main():
    currentRoom = floorPlan()
    while (not gameOver and numLives >= 0):
        print("You are in currently in Room", currentRoom)
        print("The doors are", str(roomLayout[currentRoom]).strip('[]'))
        print("Total Lives:", numLives)
        print("The Teleporter is", teleporter)
        transporterExists = teleporterManager(currentRoom)
        if (transporterExists):
          currentRoom = int(currentRoom/2)
        else:
          doorSelected = input("What Door: ")
          currentRoom = roomManager(currentRoom, doorSelected)
main()
