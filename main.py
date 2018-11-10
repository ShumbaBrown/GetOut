import random
#copy code and run in repl.it if needed
#keys are the rooms, values are the doors
roomLayout = {}
gameOver = False
numLives = 3
teleporter = 0
roomSequence = []
doorSequence = []

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
    global roomSequence
    global doorSequence
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
        print("\n")
        print("You have", currentRoom)
        displayRoomSequence()
        displayDoorSequence()
      else:
          #checks if a door selected leads to a room not in the House
          #and all lives have been reduced
          if(int(nextRoom) > len(roomLayout)):
              if(numLives == 0):
                gameOver = True
                currentRoom = "Sunken Place"
                print("\n")
                print("You have entered in the", currentRoom)
                nextRoom = 0
                displayRoomSequence()
                displayDoorSequence()
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

#determines if teleporter exists
def teleporterManager(currentRoom):
  #teleport if epsilon is in the room and room is odd
  if(teleporter in roomLayout[currentRoom] and currentRoom % 2 != 0):
    return True
  return False

#displays room sequence
def displayRoomSequence():
  global roomSequence
  print("You entered the following rooms:" , str(roomSequence).strip('[]'))

#displays door sequence
def displayDoorSequence():
  global doorSequence
  print("You went through the following doors:" , str(doorSequence).strip('[]'))

def main():
    global roomSequence
    global doorSequence
    currentRoom = floorPlan()
    while (not gameOver and numLives >= 0):
        print("You are in currently in Room", currentRoom)
        roomSequence.append(currentRoom)
        print("The doors are", str(roomLayout[currentRoom]).strip('[]'))
        print("Total Lives:", numLives)
        #print("The Teleporter is", teleporter)
        transporterExists = teleporterManager(currentRoom)
        if (transporterExists):
          doorSequence.append(int(teleporter))
          currentRoom = int(currentRoom/2)
          print("\n")
          if(currentRoom == 0):
            currentRoom = int(len(roomLayout)/2)
            print("\n")
        else:
          doorSelected = input("What Door: ")
          doorSequence.append(int(doorSelected))
          currentRoom = roomManager(currentRoom, doorSelected)
          print("\n")
main()
