'''
# This is a class as a server, which handles a white list, message sending and receiving, and information display.

class Server:

    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """

    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :return: new whitelist, return False if the address already exists
        """

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :return: new whitelist, return False if the address does not exist
        """

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :return: if successfully received, return the content of the infomation; otherwise, return False
        """

    def send(self, info):
        """
        Send information containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        """

    def show(self, type):
        """
        Returns struct of the specified type
        :return: if type is equal to 'send' or 'receive', return the corresponding struct; otherwise, return False
        """

'''


class Server:

    def __init__(self):
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        if addr in self.white_list:
            return False
        else:
            self.white_list.append(addr)
            return self.white_list

    def del_white_list(self, addr):
        if addr not in self.white_list:
            return False
        else:
            self.white_list.remove(addr)
            return self.white_list

    def recv(self, info):
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return -1
        addr = info["addr"]
        content = info["content"]
        if addr not in self.white_list:
            return False
        else:
            self.receive_struct = {"addr": addr, "content": content}
            return self.receive_struct["content"]

    def send(self, info):
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return "info structure is not correct"
        self.send_struct = {"addr": info["addr"], "content": info["content"]}

    def show(self, type):
        if type == "send":
            return self.send_struct
        elif type == "receive":
            return self.receive_struct
        else:
            return False
