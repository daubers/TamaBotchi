from slackclient import SlackClient
import time

from Responses.BasicResponses import BasicResponses

token = ""


class TamaBotchi:
    def __init__(self):
        self.channels = []
        self.sc = SlackClient(token)
        self.id = self.sc.server.login_data
        self.registered_mods = []
        print(self.id)

    def check_channels(self):
        for channel in self.sc.server.channels:
            if self.id in channel.members and channel not in self.channels:
                self.channels.append(channel.id)
            elif channel.id in self.channels:
                self.channels.remove(channel.id)

    def message_received(self, message):
        print(self.registered_mods)
        for mod in self.registered_mods:
            print(mod.listen_for_what())
            for thing in mod.listen_for_what():
                print(thing)
                if thing.lower() in message['text'].lower():
                    print(thing.lower())
                    mod.process_message(message)
        print(message)

    def status_received(self, status):
        pass

    def mainloop(self):
        if self.sc.rtm_connect():
            self.id = self.sc.server.users.find("tamabotchi").id

            self.registered_mods.append(BasicResponses(connection=self.sc))

            while True:
                self.check_channels()
                msg_received = self.sc.rtm_read()
                if msg_received:
                    for msg in msg_received:
                        if 'type' in msg.keys() and 'text' in msg.keys():
                            if msg['type'] == "message":
                                self.message_received(msg)
                            elif msg['type'] == "user_typing":
                                self.status_received(msg)
                                
                        else:
                            print("Unknown message string {0}".format(msg))
                time.sleep(1)
        else:
            print("Connection Failed, invalid token?")

pet = TamaBotchi()
pet.mainloop()