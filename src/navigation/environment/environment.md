## JetBot environment

This folder was created to solve one important problem - the JetBot needs to keep track of its current position and be able to navigate through to different objectives accordingly.

The environment initialisation consists of 4 different files:

#### initialise.py

The purpose of this file is to automatically create the environment and set up all instances of relevant classes. These would be the robot, and the PDDLReader which will send instructions to the robot based on the actions it reads from a pddl file.

#### NurseryHome.py

This file stores information on the NurseryHome and Room class. The class itself is a graph structure, in which the different 'nodes' represent different rooms. 

This class holds logic for pathfinding through different rooms for different objectives.

#### PDDLReader.py

This file stores the logic for the PDDLReader, which takes in file input and converts them into instructions for the robot. This handles the execution of chosen robot methods.

It is rather simple, as our PDDL output does not have many complicated tasks, namely to navigate between rooms and deliver objects.

#### Robot.py

This file stores logic for the Robot class, which is a class that represents and executes functionality of the robot. 