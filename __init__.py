from mycroft import MycroftSkill, intent_file_handler


class Ativa(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ativa.intent')
    def handle_ativa(self, message):
        self.speak_dialog('ativa')


def create_skill():
    return Ativa()

