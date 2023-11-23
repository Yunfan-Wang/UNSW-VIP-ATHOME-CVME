# File to setup the environment

# init environment
from NurseryHome import NurseryHome, Room
from Robot import Robot

# initialise nursing home
home = NurseryHome(True)
bathroom = Room("bathroom")
livingRoom = Room("livingroom")
diningRoom = Room("diningroom")
kitchen = Room("kitchen")
bedroom = Room("bedroom")
balcony = Room("balcony")

home.createRoom(bathroom)
home.createRoom(livingRoom)
home.createRoom(diningRoom)
home.createRoom(kitchen)
home.createRoom(bedroom)
home.createRoom(balcony)

# Initialise links - cirlce structure
# bathroom -> livingroom -> diningroom -> kitchen -> bedroom -> balcony
#    ^ ------------------------------------------------------------

home.addEdge(bathroom, livingRoom)
home.addEdge(livingRoom, diningRoom)
home.addEdge(diningRoom, kitchen)
home.addEdge(kitchen, bedroom)
home.addEdge(bedroom, balcony)
home.addEdge(balcony, bathroom)

# Initialise object positions
home.addObject("bathroom", "medication")
home.addObject("kitchen", "lighter")
home.addObject("kitchen", "knife")
home.addObject("kitchen", "scissors")
home.addObject("diningroom", "nuts")
home.addObject("diningroom", "shrimp")
home.addObject("diningroom", "bread")
home.addObject("diningroom", "wine")
home.addObject("bedroom", "key")
home.addObject("bedroom", "shirt")
home.addObject("bedroom", "pants")
home.addObject("bedroom", "dress")
home.addObject("livingroom", "extinguisher")

# initialise entity / people
home.addEntity("bedroom", "Bob")
home.addEntity("balcony", "Tom")
home.addEntity("livingroom", "Abby")

home.showAll()

# Testing
home.getPathToObj(bathroom, "scissors")
print("\n")
home.getPathToObj(livingRoom, "nuts")
print("\n")
home.getPathToObj(livingRoom, "medication")
print("\n")
home.getPathToEntity(livingRoom, "Bob")

# Test moving entities
home.moveEntity("Tom", "diningroom")
home.moveEntity("Bob", "kitchen")
home.showAll()
print("\n")
home.getPathToEntity(livingRoom, "Bob")


# Initialise robot

robot = Robot(home, livingRoom)
robot.showDetails()

robot.move_to(bathroom)
robot.showDetails()
home.showAll()

# Test robot picks up the lighter and brings it to Tom
# should go to the kitchen, then to the balcony
robot.retrieveObject("lighter")
home.showAll()
robot.showDetails()

robot.goToEntity("Tom")
robot.showDetails()

robot.drop("lighter")
home.showAll()
robot.showDetails()