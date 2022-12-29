from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionOrienterSerieS(Action):

    def name(self) -> Text:
        return "orienter_serie_scientifique"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        serie_generale = next(tracker.get_latest_entity_values("serie_generale"), None)
        serie_precise = next(tracker.get_latest_entity_values("serie_precise"), None)

        if serie_precise in ["S1", "S2", "S3"]:

            dispatcher.utter_message(text=f"Vous avez suivit la serie {serie_generale},plus precisement la serie {serie_precise}\nVoici les diffrents domaines dont vous pourrez vous interesser avec la serie {serie_precise}:\n1. Mathématiques\n2. Physique/Chimie\n3. Informatique\n4. Médecine\n5. Biologie\n6. Economie et Gestion\n7. Droit\n8. Philosophie\n9. Langues (Anglais, Espagnol, Allemend etc...)\n10. Géographie\n11. Histoire\n")
            dispatcher.utter_message(text=f"Ne soyez pas surpris de la liste des possibilités.\n Avec le BAC {serie_precise}, vous pouvez presque tout faire !\nSurtout n'hésitez pas à me poser des questions sur ces differents domaines que je viens de lister avant de passer à la suite.")

        else:
            dispatcher.utter_message(text=f"Vous avec donc le bac Technologie {serie_generale}\nVoici les diffrents domaines dont vous pourrez vous interesser avec la serie {serie_generale}:\n1. Mathématiques\n2. Physique/Chimie\n3. Informatique\n4. Economie et Gestion\n7. Droit\n8. Philosophie\n9. Langues (Anglais, Espagnol, Allemend etc...)")
            dispatcher.utter_message(text=f"Surtout n'hésitez pas à me poser des questions sur ces differents domaines que je viens de lister avant de passer à la suite.")

        return []

