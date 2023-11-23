# File to handle pddl file reading

from Robot import Robot

class PDDLReader:
    def __init__(self, robot: Robot):
        self.robot = robot

    def parse_action(self, line):
        parts = line.lower().strip().split()
        action = parts[0]
        params = parts[2:] # since parts[1] will always be leia - the name of the bot
        return action, params

    def execute(self, action, params):
        # Read in the PDDL actions
        # Actions gotten so far are 'give_items' and 'cross'
        
        if action == "give_items":
            person = params[0]
            item = params[1]
            
            # robot has to find the items first
            self.robot.retrieveObject(item)
            
            # robot goes to the person and drops the item
            self.robot.goToEntity(person)
            self.robot.drop(item)
        
        elif action == "cross":
            room1 = params[0]
            room2 = params[1]
            
            # robot navigates from one room to another
            self.robot.move_to(room2)

    # Reads the lines in from a pddl file and executes them one by one
    def readAndExecute(self, filePath):
        with open(filePath, 'r') as file:
            for line in file:
                action, params = self.parse_action(line)
                self.execute(action, params)
        return