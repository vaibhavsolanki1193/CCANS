
import socket
from pprint import pprint
import json
import ast
from FilterMessage import FilterMessage


class Server():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip,self.port))
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
                # print(data_received)
                # print(type(data_received))
                print("#######################")
                mod_string = ast.literal_eval(data_received.split('Connection: close')[1].strip())
                # json_data = json.loads(mod_string)
                pprint(mod_string)
                filterObject = FilterMessage()
                filterObject.main_filter(mod_string)
                # print(type(mod_string))
                # conn.send(data_received.encode())    # if sending the data to a different client  

        conn.close()

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    server1 = Server("127.0.0.1", 5050)
    server1.start_server()
