# Class to instantiate information about the robot

from NurseryHome import NurseryHome, Room

class Robot:
    def __init__(self, home: NurseryHome, room: Room):
        self.room = room # Starting position of the robot
        self.home = home
        self.objects = []  # What the robot is holding

    def pickUp(self, objectName: str):
        if objectName in self.room.objects:
            self.room.removeObject(objectName)
            self.objects.append(objectName)

    def drop(self, object_name: str):
        if object_name in self.objects:
            self.objects.remove(object_name)
            self.room.addObject(object_name)
    
    def retrieveObject(self, objectName: str):
        if objectName in self.objects: 
            return
        
        roomPath = self.home.getPathToObject(self.room, objectName)
        for room in roomPath:
            self.moveToAdjacent(room)
        
        self.pickUp(objectName)
        
    def goToEntity(self, entity):
        if entity in self.room.entities:
            return
        
        roomPath = self.home.getPathToEntity(self.room, entity)
        for room in roomPath:
            self.moveToAdjacent(room)
    
    def move_to(self, dest):
        if self.room.name == dest: 
            return
        
        roomPath = self.home.getPathToRoom(self.room, dest)
        for room in roomPath:
            self.moveToAdjacent(room)

    def moveToAdjacent(self, dest: Room):
        # Execute movement until it hits a waypoint, then exit out of the movement functionality
        
        self.room = dest
        print("\nRobot has moved to " + dest.name + "\n")
        return
    
    # just for visualisation purposes
    def showDetails(self):
        print("\nRobot details:\nObjects: " + str(self.objects) + "\nAt Room: " + str(self.room.name) + "\n")