## Nur mal Hallo sagen
* greeting
  - utter_greet

## Gleich verabschieden
* goodbye
  - utter_goodbye

## Nach Ferien fragen 1
* get_holidays
  - utter_ask_for_holidays

## Nach Ferien fragen 2
* get_holidays
  - kalender_info

## Generated Story 5861345622935495920
* greeting
    - utter_greet
* get_holidays{"holidays": "Sommerferien"}
    - slot{"holidays": "Sommerferien"}
    - kalender_info
## Generated Story 3351337165015667728
* greeting
    - utter_greet
* get_holidays{"ferien": "ferien"}
    - utter_ask_for_holidays
* get_holidays{"holidays": "Sommerferien"}
    - slot{"holidays": "Sommerferien"}
    - kalender_info
    - slot{"holidays": "Sommerferien"}
* goodbye
    - utter_goodbye
    - action_restart
