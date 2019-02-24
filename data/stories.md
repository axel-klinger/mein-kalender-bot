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

## Nachfragen wenn Ferien nicht spezifiziert sind
* greeting
    - utter_greet
* get_holidays
    - utter_ask_for_holidays
* get_holidays{"holidays": "Sommerferien"}
    - slot{"holidays": "Sommerferien"}
    - kalender_info
    - slot{"holidays": "Sommerferien"}
* goodbye
    - utter_goodbye
## Antworten wenn Ferien spezifiziert sind
* greeting
    - utter_greet
* get_holidays{"holidays": "Sommerferien"}
    - slot{"holidays": "Sommerferien"}
    - kalender_info
    - slot{"holidays": "Sommerferien"}
* goodbye
    - utter_goodbye
    - action_restart
## Generated Story -8641355004258649617
* greeting
    - utter_greet
* get_holidays
    - utter_ask_for_holidays
* get_holidays{"holidays": "Osterferien"}
    - slot{"holidays": "Osterferien"}
    - kalender_info
    - slot{"holidays": "Osterferien"}
* goodbye
    - utter_goodbye

