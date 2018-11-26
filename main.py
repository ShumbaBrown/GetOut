import random
from collections import defaultdict
#copy code and run in repl.it if needed

#keys are the rooms, values are the doors
roomLayout = {}
gameOver = False
numLives = 3
teleporter = 0
totalRooms = 0
roomSequence = []
doorSequence = []

# program to check if there is exist a path between two vertices
# of a graph
#This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

     # Use BFS to check path between s and d
    def isReachable(self, s, d):
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
        visited.append(False)

        # Create a queue for BFS
        queue=[]

        #stores path
        path = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            #Dequeue a vertex from queue
            n = queue.pop(0)
            path.append(n)

            # If this adjacent node is the destination node,
            # then return true
            if n == d:
              # print(*path, sep = ", ")
              return True

            #  Else, continue to do BFS
            #print(n)
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        # If BFS is complete without visited d
        return False

def calculateGraph(currentRoom):
  global numLives
  g = Graph(len(roomLayout))
  count = 1

  while(count < len(roomLayout)):
      for door in roomLayout[count]:
        numLives = 3
        teleporterExists = teleporterManager(count)
        if(teleporterExists):
          g.addEdge(count, teleporterRoomManager(count))

        elif(roomManager(count, door) == "Escaped"):
            escaped = len(roomLayout)
            g.addEdge(count, escaped)

        else:
            g.addEdge(count, roomManager(count, door))

      count = count + 1

  u = currentRoom
  v = len(roomLayout)

  if g.isReachable(u, v):
    # print("There is a path from %d to %d" % (u,v))
    return True
  else :
    # print("There is no path from %d to %d" % (u,v))
    return False

#initalizes floor plan and selects starting room
def floorPlan():
    global roomLayout
    global teleporter
    global totalRooms
    totalRooms = random.randint(1, 10)
    roomLayout = {roomNum: [] for roomNum in range(1, totalRooms + 1)}

    #populates rooms and doors
    for key in roomLayout:
      #sets the number of doors per room to 3
        while(len(roomLayout[key]) < 3):
            door = random.randint(1, totalRooms)
            #makes sure doors are unique
            if(door not in roomLayout[key]):
              if(key == totalRooms):
                roomLayout[key].append(0)
              else:
                 roomLayout[key].append(door)
        # print(roomLayout[key])

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

    return startingRoom

#checks if door selected is within the room
def checkColorInput(doorColorInput, doors, currentRoom, doorSelected):
  if (doorColorInput not in doors):
        doorSequence.remove(doorColorInput)
        print("This door does not exist. Please attempt again")
        return currentRoom

  else:
    currentRoom = roomManager(currentRoom, doorSelected)
    displayManager(doorColorInput, currentRoom)
    return currentRoom

#returns the current Room
def roomManager(currentRoom, doorSelected):
    global gameOver
    global numLives
    global totalRooms
    global roomLayout
    global roomSequence
    global doorSequence

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
      return currentRoom

    else:
        #checks if a door selected leads to a room not in the House and all lives have been reduced
        if(int(nextRoom) > len(roomLayout)):
            if(numLives == 0):
              gameOver = True
              currentRoom = "Sunken Place"
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

#determines if teleporter exists
def teleporterManager(currentRoom):
  #teleport if epsilon is in the room and room is odd
  if(teleporter in roomLayout[currentRoom]and currentRoom % 2 != 0):
    return True
  return False

#displays room sequence
def displayRoomSequence():
  global roomSequence
  print("You entered the following rooms:" , str(roomSequence).strip('[]'))

#displays door sequence
def displayDoorSequence():
  global doorSequence
  print("You went through the following doors:" , ', '.join(doorSequence))

#maps door to a color based on index
def mapDoorsToColors(roomLayout,currentRoom):
  roomColors = []
  for door in roomLayout[currentRoom]:
    if (door == roomLayout[currentRoom][0]):
        door = "red"
        roomColors.append(door)

    elif (door == roomLayout[currentRoom][1]):
        door = "green"
        roomColors.append(door)

    else:
        door = "blue"
        roomColors.append(door)

  return roomColors

#maps color back to number
def ColorstoNumber(doorColorInput, currentRoom):
  if (doorColorInput == "red"):
    return roomLayout[currentRoom][0]

  elif (doorColorInput == "green"):
    return roomLayout[currentRoom][1]

  else:
    return roomLayout[currentRoom][2]

#retrieves teleporter color
def retrieveTeleporterColor(teleporter, currentRoom):
  if (teleporter == roomLayout[currentRoom][0]):
    return "red"

  elif (teleporter == roomLayout[currentRoom][1]):
    return "green"

  else:
    return "blue"

def teleporterRoomManager(currentRoom):
  currentRoom = int(currentRoom/2)

  if(currentRoom == 0):
    currentRoom = int(len(roomLayout)/2)
    return currentRoom

  else:
    return currentRoom

def displayManager(doorColorInput, currentRoom):
  if(currentRoom == "Escaped"):
    print("You have", currentRoom)
    roomSequence.append(len(roomLayout))
    displayRoomSequence()
    displayDoorSequence()

  elif(currentRoom == "Sunken Place"):
    print("You have entered in the", currentRoom)
    displayRoomSequence()
    displayDoorSequence()

def main():
    global roomSequence
    global doorSequence
    global gameOver
    global numLives
    escapePathExists = False
    doors = []

    while (not escapePathExists):
      currentRoom = floorPlan()
      escapePathExists = calculateGraph(currentRoom)

    gameOver = False
    numLives = 3

    print('There are', totalRooms, 'rooms in the House. Can you escape? \n')
    while (not gameOver and numLives >= 0):
        print("You are in currently in Room", currentRoom)
        roomSequence.append(currentRoom)
        doors = mapDoorsToColors(roomLayout, currentRoom)
        print("The doors are", ', '.join(doors))
        print("Total Lives:", numLives)
        # print("The Teleporter is", teleporter)
        teleporterExists = teleporterManager(currentRoom)

        if (teleporterExists):
          teleporterColor = retrieveTeleporterColor(teleporter, currentRoom)
          print("You are being teleported through the", teleporterColor, "door ")
          print("\n")
          doorSequence.append(teleporterColor)
          currentRoom = teleporterRoomManager(currentRoom)

        else:
          doorColorInput = input("What Door: ")
          print("\n")
          doorSequence.append(doorColorInput)
          doorSelected = ColorstoNumber(doorColorInput, currentRoom)
          currentRoom = checkColorInput(doorColorInput, doors,currentRoom, doorSelected)

main()
