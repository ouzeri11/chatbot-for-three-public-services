# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import UserUtteranceReverted

# public_services = {
#     "first": " eimai to 1o",
# 	"second": " eimai to 2o",
# 	"third": " eimai to 3o",
# }



# class ActionHelloWolrd(Action):
	
# 	def name(self) -> Text:
# 		return "action_greet_user"

# 	def run(self, dispatcher: CollectingDispatcher,
# 			tracker: Tracker,
# 			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
			
# 		dispatcher.utter_message("Γεια σου εγω θα σε πληροφορησω για 3 υπηρεσίες")
		
# 		return [UserUtteranceReverted()]

# class ActionFindAndShowServiceInfo(Action):

#     def name(self) -> Text:
#         return "action_find_and_show_service_info"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         service = tracker.get_slot("service")

#         info = public_services.get(service)

#         if info is None:
#             output = "Could not find the time zone for {}".format(service)
#         else:
#             output = "The time zone for {} is {}".format(service, info)

#         dispatcher.utter_message(text=output)

#         return []
