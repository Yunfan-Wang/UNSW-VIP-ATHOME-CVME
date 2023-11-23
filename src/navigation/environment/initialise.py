# File to setup the environment
# Returns a now active robot and PDDLReader

# init environment
from NurseryHome import NurseryHome, Room
from PDDLReader import PDDLReader
from Robot import Robot

class Initialise:
    def __init__(self):
        self.home = NurseryHome(True)

    def setup(self):
        # initialise nursing home
        bathroom = Room("bathroom")
        livingRoom = Room("livingroom")
        diningRoom = Room("diningroom")
        kitchen = Room("kitchen")
        bedroom = Room("bedroom")
        balcony = Room("balcony")

        self.home.createRoom(bathroom)
        self.home.createRoom(livingRoom)
        self.home.createRoom(diningRoom)
        self.home.createRoom(kitchen)
        self.home.createRoom(bedroom)
        self.home.createRoom(balcony)

        # Initialise links - cirlce structure
        # bathroom -> livingroom -> diningroom -> kitchen -> bedroom -> balcony
        #    ^ ------------------------------------------------------------

        self.home.addEdge(bathroom, livingRoom)
        self.home.addEdge(livingRoom, diningRoom)
        self.home.addEdge(diningRoom, kitchen)
        self.home.addEdge(kitchen, bedroom)
        self.home.addEdge(bedroom, balcony)
        self.home.addEdge(balcony, bathroom)

        # Initialise object positions
        self.home.addObject("bathroom", "medication")
        self.home.addObject("kitchen", "lighter")
        self.home.addObject("kitchen", "knife")
        self.home.addObject("kitchen", "scissors")
        self.home.addObject("diningroom", "nuts")
        self.home.addObject("diningroom", "shrimp")
        self.home.addObject("diningroom", "bread")
        self.home.addObject("diningroom", "wine")
        self.home.addObject("bedroom", "key")
        self.home.addObject("bedroom", "shirt")
        self.home.addObject("bedroom", "pants")
        self.home.addObject("bedroom", "dress")
        self.home.addObject("livingroom", "extinguisher")

        # initialise entity / people
        self.home.addEntity("bedroom", "Bob")
        self.home.addEntity("balcony", "Tom")
        self.home.addEntity("livingroom", "Abby")
        
        print("\nhome initialising.....\n")
        self.home.showAll()
        
        # Initialise the robot
        print("\ninitialising robot...\n")
        
        robot = Robot(self.home, bedroom)
        pddlReader = PDDLReader(robot)
        
        return robot, pddlReader
        
        



# # Testing
# home.getPathToObj(bathroom, "scissors")
# print("\n")
# home.getPathToObj(livingRoom, "nuts")
# print("\n")
# home.getPathToObj(livingRoom, "medication")
# print("\n")
# home.getPathToEntity(livingRoom, "Bob")

# # Test moving entities
# home.moveEntity("Tom", "diningroom")
# home.moveEntity("Bob", "kitchen")
# home.showAll()
# print("\n")
# home.getPathToEntity(livingRoom, "Bob")

# robot.showDetails()

# robot.move_to(bathroom)
# robot.showDetails()
# home.showAll()

# # Test robot picks up the lighter and brings it to Tom
# # should go to the kitchen, then to the balcony
# robot.retrieveObject("lighter")
# home.showAll()
# robot.showDetails()

# robot.goToEntity("Tom")
# robot.showDetails()

# robot.drop("lighter")
# home.showAll()
# robot.showDetails()