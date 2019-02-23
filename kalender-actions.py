from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class KalenderInfo(Action):
    def name(self):
        return 'kalender_info'

    def run(self, dispatcher, tracker, domain):

        hol = tracker.get_slot('holidays')

        # replace with API call ...

        # switch (hol):
        #   case 'Herbstferien':
        #       response = 'Im Herbst'
        #       break
        #   ...

        # ... until here!

        response = 'Ich weiss nix von ' + hol
        dispatcher.utter_message(response)
        return [SlotSet('holidays', hol)]
