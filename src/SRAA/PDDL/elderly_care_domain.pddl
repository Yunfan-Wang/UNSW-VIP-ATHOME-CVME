(define (problem elderly_care_scenario) (:domain elderly_care)
  (:objects
    john - person
    aspirin - medication
    lunch - meal
    walker - device
  )

  (:init
    (needs_medication john)
    (medication_ready aspirin)
    (is_hungry john)
    (not (has_mobility_aid john))
  )

  (:goal
    (and
      (not (needs_medication john))
      (not (is_hungry john))
      (has_mobility_aid john)
    )
  )
)