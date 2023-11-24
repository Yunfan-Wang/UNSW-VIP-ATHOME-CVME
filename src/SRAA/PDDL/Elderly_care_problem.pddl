(define (domain elderly_care)
  (:requirements :strips :typing)
  (:types person medication meal device)

  (:predicates
    (medication_ready ?m - medication)
    (meal_prepared ?meal - meal)
    (is_hungry ?p - person)
    (needs_medication ?p - person)
    (has_mobility_aid ?p - person)
    (assisted ?p - person)
  )

  (:action administer_medication
    :parameters (?p - person ?m - medication)
    :precondition (and (needs_medication ?p) (medication_ready ?m))
    :effect (not (needs_medication ?p))
  )

  (:action prepare_meal
    :parameters (?p - person ?meal - meal)
    :precondition (is_hungry ?p)
    :effect (and (meal_prepared ?meal) (not (is_hungry ?p)))
  )

  (:action assist_movement
    :parameters (?p - person ?d - device)
    :precondition (not (has_mobility_aid ?p))
    :effect (has_mobility_aid ?p)
  )
)