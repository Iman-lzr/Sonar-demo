# calculator.py - Code avec problèmes critiques

import os
import subprocess

# 1. 🔴 MOT DE PASSE EN CLAIR (Blocker - Vulnérabilité critique)
API_SECRET = "sk_live_123456789"  # JAMAIS faire ça !

# 2. 🔴 INJECTION DE COMMANDES (Blocker - Vulnérabilité critique)
def ping_host():
    host = input("Entrez l'IP à ping: ")
    # L'utilisateur peut entrer: 8.8.8.8; rm -rf /
    os.system("ping -c 1 " + host)  # DANGER!

# 3. 🔴 UTILISATION D'EVAL (Blocker - Vulnérabilité critique)
def calculate():
    expr = input("Calcul: ")
    result = eval(expr)  # L'utilisateur peut exécuter du code!
    print(f"Résultat: {result}")

# 4. 🔴 FONCTION TROP COMPLEXE (Major - Code Smell)
def complex_function(x):
    if x > 0:
        if x < 10:
            if x != 5:
                if x % 2 == 0:
                    for i in range(10):
                        for j in range(5):
                            for k in range(3):
                                print(i, j, k)
                else:
                    print("x est impair mais pas 5")
            else:
                print("x est 5")
        elif x < 20:
            if x > 15:
                if x == 18:
                    print("x est 18")
                elif x == 19:
                    print("x est 19")
                else:
                    print("x est entre 16 et 17")
            else:
                print("x est entre 10 et 15")
    else:
        if x == 0:
            print("x est zéro")
        else:
            print("x est négatif")

# 5. 🔴 XSS VULNÉRABILITÉ (Blocker)
def generate_html():
    user_input = input("Entrez votre nom: ")
    # Injection XSS possible: <script>alert('hack')</script>
    html = f"<html><body>Bonjour {user_input}</body></html>"
    return html

# 6. 🔴 FONCTION INUTILISÉE (Minor - Code Smell)
def unused_function():
    """Cette fonction n'est jamais appelée"""
    a = 1
    b = 2
    c = a + b
    # Code commenté
    # print("Ancienne fonction")
    # return c
    pass

# 7. 🔴 NOMS DE VARIABLES INAPPROPRIÉS (Minor - Code Smell)
a = 10  # Qu'est-ce que c'est?
b = 20  # Pas clair du tout
c = "admin"
d = True
e = [1,2,3]
f = a + b  # Compréhensible?

# 8. 🔴 HARDCODED CREDENTIALS (Blocker)
def connect_database():
    username = "admin"
    password = "password123"  # En clair!
    host = "localhost"
    # Connexion à la base...
    print(f"Connexion à {host} avec {username}")

# 9. 🔴 COMMANDE SUBPROCESS DANGEREUSE (Critical)
def execute_command():
    cmd = input("Commande: ")
    # subprocess avec shell=True est dangereux
    subprocess.run(cmd, shell=True)  # Injection possible!

# 10. 🔴 DUPLICATION DE CODE (Major)
def calculate_area_rectangle(length, width):
    # Cette fonction fait presque la même chose
    result = length * width
    print(f"Surface rectangle: {result}")
    return result

def calculate_area_square(side):
    # Presque identique à calculate_area_rectangle!
    result = side * side
    print(f"Surface carré: {result}")
    return result

# 11. 🔴 FONCTION TROP LONGUE (Major)
def do_everything():
    # Cette fonction fait trop de choses différentes
    print("Début du programme")
    
    # Partie 1: Calculs
    x = 10
    y = 20
    z = x + y
    print(f"z = {z}")
    
    # Partie 2: Entrées utilisateur
    name = input("Nom: ")
    age = input("Âge: ")
    
    # Partie 3: Fichiers
    with open("test.txt", "w") as f:
        f.write(f"{name},{age}")
    
    # Partie 4: Base de données
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (name text, age text)")
    c.execute("INSERT INTO users VALUES (?, ?)", (name, age))
    conn.commit()
    
    # Partie 5: Appel API
    response = requests.get("https://api.example.com")
    
    # Partie 6: Envoi email
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    print("Fin du programme")

# 12. 🔴 EXCEPTION TROP GÉNÉRIQUE (Minor)
def risky_operation():
    try:
        x = 1 / 0  # Division par zéro
    except Exception:  # Trop générique!
        pass  # On ignore l'erreur!

# 13. 🔴 TODO COMMENTÉ (Info)
def incomplete_function():
    # TODO: Implémenter cette fonction plus tard
    # FIXME: Bug à corriger ici
    pass

# 14. 🔴 CODE MORT (Minor)
def dead_code():
    x = 10
    return x
    y = 20  # Cette ligne ne sera jamais exécutée!
    z = 30  # Code mort

# Exécution principale
if __name__ == "__main__":
    print("Calculatrice dangereuse")
    calculate()
    ping_host()
    complex_function(5)
    generate_html()
    execute_command()
    do_everything()