from BaseModule import Base
import json
import os
import datetime


class Emotions(Base.Base):
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
        self.listen_for = ["<@{0}>".format(self.id), "tamabotchi"]   # just listen for everything by default
        self.data = self.load_data("emotion_data.json")
        self.user_data = self.load_data("user_emotion.json")
        self.last_data_save = datetime.datetime.now()

    def load_data(self, filename):
        path = os.path.dirname(__file__)
        response_file = open(os.path.join(path, filename))
        data = json.load(response_file)
        response_file.close()
        return data

    def save_data(self, data, filename):
        path = os.path.dirname(__file__)
        response_file = open(os.path.join(path, filename),"w")
        json.dump(data, response_file)
        response_file.close()
        self.last_data_save = datetime.datetime.now()

    def lookup_

    def process_message(self, message):
        """
        Handle a message
        :param message: message recieved through the slack API
        :return: None
        """
        print("Processing message")

        for item in self.data:
            if item in message['text'].lower():
                # we need to find the user in the data list and then increment/decrement their "likeness" factor
                if message['user'] in [i['user'] for i in self.user_data]:
                    for user in self.user_data:
                        if user['user'] == self.user_data:

        for response in self.responses:
            if response['call'] in message['text'].lower():
                self.sc.rtm_send_message(channel=message['channel'], message=response['response'])
        # check for save
        if self.last_data_save > datetime.datetime.now() - datetime.timedelta(minutes=5):
            self.save_data(self.data, "emotion_data.json")
            self.save_data(self.user_data, "user_emotion.json")