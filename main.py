import random
#copy code and run in repl.it if needed
#keys are the rooms, values are the doors
roomLayout = {}
gameOver = False
numLives = 3;
#initalizes floor plan and selects starting room
def floorPlan():
    global roomLayout
    totalRooms = random.randint(1, 10)
    roomLayout = {roomNum: [] for roomNum in range(1, totalRooms + 1)}
    #populates rooms and doors
    for key in roomLayout:
        for value in range(totalRooms + 1):
            roomLayout[key].append(value)
    #starts player in random room
    startingRoom = random.choice(list(roomLayout))
    #ensures starting room is not the final room
    while(startingRoom == len(roomLayout)):
      startingRoom = random.choice(list(roomLayout))
    print('There are ', totalRooms, 'rooms in the House. Can you escape?')
    return startingRoom
#returns the current Room
def roomManager(currentRoom, doorSelected):
    global gameOver
    global numLives
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
              #deductes life and allows user to repeat the room
              numLives = numLives - 1
              currentRoom = int(nextRoom) - int(doorSelected)
              return currentRoom


        #sets the next room to the current room
        else:
          currentRoom = nextRoom
          nextRoom = 0
          return currentRoom
def main():
    currentRoom = floorPlan()
    while (not gameOver and numLives >= 0):
        print("You are in currently in Room ", currentRoom)
        print("Total Lives:", numLives)
        doorSelected = input("What Door: ")
        currentRoom = roomManager(currentRoom, doorSelected)
main()
