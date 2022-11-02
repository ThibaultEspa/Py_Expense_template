from PyInquirer import prompt
import csv
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User -  Name: ",
    },
]
nom_colonnes =['name']
def add_user(*args):
    infos = prompt(user_questions)
    fichier = open('users.csv','a')
    with fichier:    
        obj = csv.DictWriter(fichier, fieldnames=nom_colonnes)
        obj.writerow(infos)
    print("User Added !")
    return True