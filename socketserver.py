
import socket
from pprint import pprint
import ast
from mainThread import MainThread


class Server():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def main_filter(self, unfitlered_message):
        try:
            if unfitlered_message['data'].get('markdown') and unfitlered_message['data']['text'].count('data-object-id') == 2:
                print('Tagged Message Received')
                messageType = "TaggedMessage"
            elif unfitlered_message['data'].get('text') == 'Card: Crtitical Case Alert':
                print('Adaptive card detected')
                messageType = "AdaptiveCard"
            elif unfitlered_message['data'].get('markdown') and unfitlered_message['data']['text'].count('data-object-id') == 1:
                print("this in untagged message")
                messageType = "UntaggedMessage"
            elif unfitlered_message['data'].get('roomType') == 'direct':
                print('unicast message')
                messageType = "UnicastMessage"
            elif unfitlered_message['data'].get('type') == 'submit':
                print('Incoming ACK')
                messageType = "IncomingACK"
            else:
                print("No filtered matched")
                messageType = "NoMatch"
            return messageType
        except Exception as e:
            print(e)

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(2)
        # server_socket.listen(2) # number of clients at a time
        connected = True
        while connected:
            # starting server
            conn, address = server_socket.accept()
            print(f"[NEW CONECTION] {conn} {address} connected")
            data_received = conn.recv(2048).decode()
            if len(data_received) == 0:
                continue
            else:
                print("#######################")
                modMessage = ast.literal_eval(data_received.split('Connection: close')[1].strip())
                pprint(modMessage)
                messageType = self.main_filter(modMessage)
                MainThreadObj = MainThread()
                MainThreadObj.run_main_thread(messageType=messageType, inMsg=modMessage)

        conn.close()


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    server1 = Server("127.0.0.1", 5050)
    server1.start_server()
