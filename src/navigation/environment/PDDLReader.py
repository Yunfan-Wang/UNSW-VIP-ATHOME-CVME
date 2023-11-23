class PDDLReader:
    def __init__(self, robot):
        self.robot = robot

    def parse_action(self, action_line):
        parts = action_line.strip().split()
        action_name = parts[0]
        params = parts[1:]
        return action_name, params

    def execute_action(self, action_name, params):
        # TODO fill with pddl actions
        return

    def read_plan(self, file_path):
        # TODO fill in with file reading method
        return