from BaseModule import Base
import json
import os


class BasicResponses(Base.Base):
    """
        Class to handle the basic responses from people talking to Tamabotchi
    """
    def __init__(self, connection):
        """
        :param connection: slack RTM connection
        :return:
        """
        self.sc = connection
        Base.Base.__init__(self, self.sc)
        self.id = self.sc.server.users.find("tamabotchi").id
        self.listen_for = ["*", "<@{0}>".format(self.id)]   # just listen for everything by default
        self.responses = []
        self.load_responses()

    def load_responses(self):
        path = os.path.dirname(__file__)
        response_file = open(os.path.join(path, "responses.json"))
        self.responses = json.load(response_file)
        response_file.close()
        print(self.responses)

    def process_message(self, message):
        """
        Handle a message
        :param message: message recieved through the slack API
        :return: None
        """
        print("Processing message")
        for response in self.responses:
            if response['call'] in message['text'].lower():
                self.sc.rtm_send_message(channel=message['channel'], message=response['response'])
