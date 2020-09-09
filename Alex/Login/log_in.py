import psycopg2
import hashlib
from getpass import getpass

def check_logs():
    user_name = (input("Nom d'utilisateur : "),) # On prend l'user
    user_password = getpass("Mot de passe : ") # On prend le password en xxxx
    user_password = user_password.encode() #On encode en UTF8
    user_password = (hashlib.sha1(user_password).hexdigest(),) #On le hash en hexa
    connexion = psycopg2.connect("dbname=Testprojet2 user=postgres password=group12")
    cursor = connexion.cursor()
    cursor.execute(f'SELECT * FROM user_infos WHERE name = %s AND password = %s', (user_name, user_password))
    connexion.commit()
    result = cursor.fetchone()
    if result: #A Si le user et le password sont bons
        print("YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEES")
    else : #A Sinon...
        print("Nooooooooooooooooooooooooooooooooooooooooooooooooooo")








