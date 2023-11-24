from pyparsing import Word, alphas, alphanums, Suppress, Group, OneOrMore, Optional, delimitedList

# Define the basic structure of a PDDL file
lparen = Suppress("(")
rparen = Suppress(")")
identifier = Word(alphanums + "_-")
typed_list = Group(delimitedList(identifier) + Optional(Suppress("-") + identifier))

# Define PDDL components
domain_name = lparen + ":domain" + identifier("domain") + rparen
object_declaration = lparen + ":objects" + typed_list("objects") + rparen
action_name = lparen + ":action" + identifier("action_name") + rparen
predicate = Group(lparen + identifier + Optional(typed_list) + rparen)
predicates_declaration = lparen + ":predicates" + Group(OneOrMore(predicate))("predicates") + rparen
action_declaration = lparen + ":action" + identifier("action_name") + Group(OneOrMore(predicate))("action_body") + rparen
problem_declaration = lparen + "problem" + identifier("problem") + rparen
domain_declaration = lparen + ":domain" + identifier("domain") + rparen
init_state = lparen + ":init" + Group(OneOrMore(predicate))("init_state") + rparen
goal_state = lparen + ":goal" + Group(OneOrMore(predicate))("goal_state") + rparen

# Main PDDL parser
pddl_parser = OneOrMore(
    domain_name |
    object_declaration |
    action_name |
    predicates_declaration |
    action_declaration |
    problem_declaration |
    domain_declaration |
    init_state |
    goal_state
)

# Function to parse PDDL file
def parse_pddl(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return pddl_parser.parseString(content)

# Example usage
#domain_file = 'path_to_domain_file.pddl'
#problem_file = 'path_to_problem_file.pddl'

#domain_data = parse_pddl(domain_file)

#problem_data = parse_pddl(problem_file)

#print("Domain:", domain_data.domain)
#print("Predicates:", domain_data.predicates)
#print("Actions:", domain_data.action_name)
#print("Problem:", problem_data.problem)
#print("Objects:", problem_data.objects)
#print("Initial State:", problem_data.init_state)
#print("Goal State:", problem_data.goal_state)