# coding:utf-8

import socket
import marshal
import pickle

from play import Variables as var

# Le client envoi des informations



host, port = ('localhost', 5566)
# instancier socket (famille qu'on va utiliser, type de socket)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    socket.connect((host, port))
    var.server_open = True
    print("Vous êtes connecté au serveur")
except :
    print('Le serveur est fermé')
    

def execute_client(data_client):
    
    
    try:
        # connecter le client au serveur
        data = pickle.dumps(data_client)

        # encoder avant envoi
        # data = data.encode("utf-8")

        # envoyer la donnée
        socket.sendall(data)
        # recupérer les données du server
        received = socket.recv(1024)
        if len(received) != 0 :
            received = pickle.loads(received)
            var.list_players = received
    except ConnectionRefusedError:
        print("Connexion échoué") 

    # finally : 
    #     # fermer le socket
    #     print("Connexion fermé")
    #     socket.close()

