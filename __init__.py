import paho.mqtt.publish as publish

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class SonoffToggle(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.__build_single_command()

    def __build_single_command(self):
        intent = IntentBuilder("mymqttIntent").require("CommandKeyword").require("ModuleKeyword").require("ActionKeyword").build()
        self.register_intent(intent, self.handle_toggle_sonoff)

    def handle_toggle_sonoff(self, message):
        dev_name = message.data.get("ModuleKeyword").replace(' ', '_')
        act_name = message.data.get("ActionKeyword").replace(' ', '_')

        publish.single("cmnd/" + dev_name + "/power", act_name, hostname="127.0.0.1")

        self.speak_dialog('toggle.sonoff')


def create_skill():
    return SonoffToggle()

