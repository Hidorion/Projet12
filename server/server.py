# coding:utf-8

# Port de communication
import socket
import threading
import pickle

class ThreadForClient(threading.Thread) :
    def __init__(self, conn, number, socket, send_back):
        self.socket = socket
        threading.Thread.__init__(self)
        self.conn = conn
        self.send_back = send_back
        self.number_player = number

    def run(self):
        while True:
            # Recupérer les informations du client
            result = self.conn.recv(1024)
            if len(result) != 0 :
                data = pickle.loads(result)
                self.send_back.send_back([self.number_player, data], self.conn)
                if data == "disconnect" :
                    break

        self.conn.close()
        


class Send_back():

    def __init__(self) :

        self.list_players = []
        self.number_player = []

    def append_list(self, received) :
        if len(self.list_players) != 0 and received[0] in self.number_player:
            for index, player in enumerate(self.list_players) :
                if player[0] == received[0] :
                    if received[1] == "disconnect" :
                        del self.list_players[index]
                    else :
                        self.list_players[index] = received
        else : 
            self.number_player.append(received[0])
            self.list_players.append(received)
    
    def send_back(self, received, conn):
        self.append_list(received)
        print(self.list_players)
        send = pickle.dumps(self.list_players)
        conn.sendall(send)



#-----------------------------------------------------------------------------

def accept_client():
    # mettre le serveur en ecoute
    socket.listen()
    print("En écoute")
    # Accepter les connexion -> initialiser les connexion
    conn, address = socket.accept()
    return conn
    
        
# instancier socket (famille qu'on va utiliser, type de socket)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Associer socket a une adresse
socket.bind(('192.168.1.18', 5566))
number_player = 1
send_back = Send_back()

while True :
    conn = accept_client()
    my_thread = ThreadForClient(conn, number_player, socket, send_back)
    my_thread.start()
    number_player += 1
    
    

    

# Fermer la connexion et le serveur

socket.close()