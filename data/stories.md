## search hospital happy path
* greet
 - utter_greet
* search_provider{"facility_type":"hospital", "location":"Abuja"}
 - action_facility_search
* thanks
 - utter_goodbye


## search hospital + location
* greet
 - utter_greet
* search_provider{"facility_type":"hospital"}
 - utter_ask_location
* inform{"location":"Abuja"}
 - action_facility_search
 - slot{"address": "Zone b, Apo Resettlement""}
* thanks
 - utter_goodbye

## search hospital + location + services path 1
* greet
 - utter_greet
* search_provider{"facility_type":"hospital"}
 - utter_ask_location
* inform{"location":"Abuja"}
 - action_facility_search
 - slot{"address": "Zone b, Apo Resettlement""}
* search_services{"service_type": "cardiotherapy"}
 - action_service_search
 - slot{"service": "cardiotherapy"}
* thanks
 - utter_goodbye



## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
