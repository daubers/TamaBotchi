
class Base:
    """
    The base class for all Tamabotchi modules
    """
    def __init__(self, connection):
        """
        :param connection: slack RTM connection
        :return:
        """
        self.listen_for = ["*", ]   # just listen for everything by default
        self.sc = connection

    def listen_for_what(self):
        return self.listen_for

    def process_message(self, message):
        """
        Handle a message
        :param message: message recieved through the slack API
        :return: None
        """
        print("{0} {1}".format(self, message))
