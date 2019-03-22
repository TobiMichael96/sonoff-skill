import paho.mqtt.publish as publish

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill


class SonoffToggle(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        toggle_intent = IntentBuilder("mymqttIntent").require("CommandKeyword").require("ModuleKeyword").optionally("ActionKeyword").build()
        self.register_intent(toggle_intent, self.handle_toggle_sonoff)


    def handle_toggle_sonoff(self, message):
        dev_name = message.data.get("ModuleKeyword").replace(' ', '_')
        if  message.data.get("ActionKeyword"):
                act_name = message.data.get("ActionKeyword")
        else:
                act_name = "toggle"

        publish.single("cmnd/" + dev_name + "/power", act_name, hostname="127.0.0.1")
        self.speak_dialog('toggle.sonoff')


def create_skill():
    return SonoffToggle()

