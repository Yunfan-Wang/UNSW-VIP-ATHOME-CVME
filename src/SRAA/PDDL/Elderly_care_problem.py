# pddl_generator_for_elderly.py pseudo code

def generate_pddl_domain():
    domain_template = """
    (define (domain elderly_care)
        (:types person - object
                location - object)
        (:predicates 
            (at ?person - person ?location - location)
            (needs_medication ?person - person))
        (:action remind_medication
            :parameters (?person - person)
            :precondition (needs_medication ?person)
            :effect (not (needs_medication ?person))))
    """
    return domain_template

def generate_pddl_problem(person_name, initial_location):
    problem_template = f"""
    (define (problem elderly_care_{person_name})
        (:domain elderly_care)
        (:objects
            {person_name} - person
            home - location)
        (:init
            (at {person_name} {initial_location})
            (needs_medication {person_name}))
        (:goal
            (not (needs_medication {person_name}))))
    """
    return problem_template

def main():
    domain = generate_pddl_domain()
    problem = generate_pddl_problem("John", "home")

    with open("elderly_care_domain.pddl", "w") as domain_file:
        domain_file.write(domain)

    with open("elderly_care_problem.pddl", "w") as problem_file:
        problem_file.write(problem)

    print("PDDL files generated successfully.")

if __name__ == "__main__":
    main()