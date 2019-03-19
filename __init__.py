from mycroft import MycroftSkill, intent_file_handler


class SonoffToggle(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('toggle.sonoff.intent')
    def handle_toggle_sonoff(self, message):
        self.speak_dialog('toggle.sonoff')


def create_skill():
    return SonoffToggle()

