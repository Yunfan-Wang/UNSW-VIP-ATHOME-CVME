from collections import deque

# Class definition of a single room inside the nursery home
class Room:
    def __init__(self, name):
        self.name = name
        self.objects = []  # List to store objects in the room
        self.entities = [] # List to store people / living things in rooms

    # Adds an object to the room
    def addObject(self, object_name):
        self.objects.append(object_name)

    # removes an object from the room
    def removeObject(self, object_name):
        if object_name in self.objects:
            self.objects.remove(object_name)
            
    # adds an entity / person to the room
    def addEntity(self, entity):
        self.entities.append(entity)

    # removes an entity / person from the room
    def removeEntity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            
    # lists the objects in the room
    def listObjects(self):
        return self.objects
    
    # lists the entities in the room
    def listEntities(self):
        return self.entities
    
    # for visualising
    def show(self):
        print("Room: " + self.name + "\nObjects: " + str(self.objects) + "\nEntities: " + str(self.entities))
    
    

# Class to store graphical representation of nursery home environment
class NurseryHome:
    def __init__(self, directed):
        self.links = {} # map between roomNames and a list of roomNames the room is adjacent to
        self.rooms = [] # List of rooms class instancesin the environment
        self.directed = directed    # boolean to indicate whether this is a directed environment
            
    def createRoom(self, room):
        self.links[room.name] = []
        self.rooms.append(room)
        
    def addEdge(self, room1, room2):
        self.links[room1.name].append(room2.name)
        
        if not self.directed:
            self.links[room2.name].append(room1.name)
    
    def numRoom(self):
        return len(self.rooms)
    
    def addObject(self, roomName, objName):
        for room in self.rooms:
            if room.name == roomName:
                room.addObject(objName)
    
    def addEntity(self, roomName, entity):
        for room in self.rooms:
            if room.name == roomName:
                room.addEntity(entity)
                
    def findRoomFromName(self, roomName):
        for room in self.rooms:
            if room.name == roomName:
                return room
        
        # If room does not exist
        print("Room does not exist\n")
        return None
    
    def findRoomFromIndex(self, index):
        try:
            return self.rooms[index]
        # If room does not exist
        except Exception:
            print("Room does not exist\n")
            return None
    
    def moveEntity(self, entity: str, dest: str):
        for room in self.rooms:
            if entity in room.entities:
                room.removeEntity(entity)
        
        self.findRoomFromName(dest).addEntity(entity)
        
    def getPathToRoom(self, start, dest):
        # Use BFS to find the closest path to the given room
        # Returns a list of Rooms
        queue = deque([(start.name, [])])

        visited = set()

        while queue:
            current_room, path = queue.popleft()

            visited.add(current_room)

            if current_room == dest:
                # for room in path: print(room.name)
                return path

            for adjacent_room in self.links[current_room]:
                if adjacent_room not in visited:
                    queue.append((adjacent_room, path + [self.findRoomFromName(adjacent_room)]))
        
        # If the object is not in any room, return empty list
        return []
                
    def getPathToObject(self, room, obj):
        # Use BFS to find the closest path to the obj
        # Returns a list of Rooms
        queue = deque([(room.name, [])])

        visited = set()

        while queue:
            current_room, path = queue.popleft()

            visited.add(current_room)

            if obj in self.findRoomFromName(current_room).listObjects():
                # for room in path: print(room.name)
                return path

            for adjacent_room in self.links[current_room]:
                if adjacent_room not in visited:
                    queue.append((adjacent_room, path + [self.findRoomFromName(adjacent_room)]))
        
        # If the object is not in any room, return empty list
        return []
    
    def getPathToEntity(self, room, entity):
        # Use BFS to find the closest path to the entity
        # Returns a list of Rooms
        queue = deque([(room.name, [])])

        visited = set()

        while queue:
            current_room, path = queue.popleft()

            visited.add(current_room)

            if entity in self.findRoomFromName(current_room).listEntities():
                # for room in path: print(room.name)
                return path

            for adjacent_room in self.links[current_room]:
                if adjacent_room not in visited:
                    queue.append((adjacent_room, path + [self.findRoomFromName(adjacent_room)]))
        
        # If the entity is not in any room, return empty list
        return []
    
    def showAll(self):
        print("\nNurseryHome:\n")
        for room in self.rooms:
            room.show()
            print("Links: ")
            for adj in self.links[room.name]: print(adj)
            print("\n")