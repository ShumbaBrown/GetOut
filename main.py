import random
import unittest

def GenerateNFA(num_states):
  # Accept the number of states to include in the nfa and returns a dictionary
  # containing an adjacency list. It also includes indexes current and final.
  nfa = {}

  for i in range(num_states):
    transitions = []
    for j in range(random.randint(1, num_states)):
      random_num = random.randint(1, num_states)
      if random_num not in transitions:
        transitions.append(random_num)
    nfa[i] = transitions

  nfa["final"] = random.randint(1, num_states - 1)
  nfa["current"] = 0

  return nfa

def GetDoorChoices(nfa):
  # Accepts an nfa and returns a list of possible door choices.
  return nfa[nfa["current"]]

def OpenDoor(nfa, choice):
  # Accepts an nfa and a door choice and return the nfa after transitioning
  # to the choice. Returns None if there is an error.

  if choice in nfa:
    nfa["current"] = choice;
    return nfa
  else: 
    return None



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




# Tests

class TestStringMethods(unittest.TestCase):


    def test_OpenDoor(self):
        test_nfa = {0: [1, 2, 3], 1: [2, 4], 2: [5], 3: [5], 4: [5], 5: [], "current": 0, "final": 5}
        expected_nfa = {0: [1, 2, 3], 1: [2, 4], 2: [5], 3: [5], 4: [5], 5: [], "current": 3, "final": 5}
        self.assertEqual(OpenDoor(test_nfa, 3), expected_nfa)

    def test_GetDoorChoices(self):
        test_nfa = {0: [1, 2, 3], 1: [2, 4], 2: [5], 3: [5], 4: [5], 5: [], "current": 0, "final": 5}
        expected_doors = [1, 2, 3]
        self.assertEqual(GetDoorChoices(test_nfa), expected_doors)

# End of tests.

def main():

    # Uncomment the line below to run unit tests.
    # unittest.main()

    currentRoom = floorPlan()
    while (not gameOver and numLives >= 0):
        print("You are in currently in Room ", currentRoom)
        print("Total Lives:", numLives)
        doorSelected = input("What Door: ")
        currentRoom = roomManager(currentRoom, doorSelected)



main()
