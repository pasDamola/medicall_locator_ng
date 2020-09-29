# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        facility = tracker.get_slot("facility_type")
        address = "Zone b, Apo Resettlement"

        dispatcher.utter_message("Here is the address of the {}:{}".format(facility, search))

        return [SlotSet("address",address)]



class ActionServiceSearch(Action):

    def name(self) -> Text:
        return "action_service_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        service = tracker.get_slot("service_type")

        dispatcher.utter_message("Yes they do have {} services:".format(service))

        return [SlotSet("service",service)]
