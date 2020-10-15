# coding:utf-8

import socket
import marshal
import pickle

from core.play import variables as var

# Le client envoi des informations



host, port = ('localhost', 5566)
# instancier socket (famille qu'on va utiliser, type de socket)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    # Se connecter au serveur
    socket.connect((host, port))
    var.server_open = True
    print("Vous êtes connecté au serveur")
except :
    print('Le serveur est fermé')
    

def execute_client(data_client):
    """
        Envoi et récupère les informations au server
    """
    
    
    try:
        # Transformer la data pour l'envoyer au serveur
        data = pickle.dumps(data_client)

        # envoyer la data
        socket.sendall(data)
        # recupérer la data du server
        received = socket.recv(1024)
        # Vérifier que la data ne soit pas vide
        if len(received) != 0 :
            # télécharger la data
            received = pickle.loads(received)
            var.list_players = received
    except ConnectionRefusedError:
        print("Connexion échoué") 

