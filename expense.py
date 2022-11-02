from PyInquirer import prompt, Separator
import csv
file = open('users.csv', "r")
lines = file.readlines()
file.close()
user_choice = []
for line in lines:
    user_choice.append({'name': line[0:len(line)-1]})
# modif = {k: if k == expense_questions.spender.answer: } 

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
    {
        "type":"checkbox",
        "name":"user",
        "message":"for who ?",
        "choices": user_choice,
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 | answer[''] else True
    }
]


nom_colonnes =['amount','label','spender', 'user']
def new_expense(*args):
    infos = prompt(expense_questions)
    fichier = open('expense_report.csv','a')
    with fichier:    
        obj = csv.DictWriter(fichier, fieldnames=nom_colonnes)
        obj.writerow(infos)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯

    # fichier = open('expense_report.csv','w')
    # obj = csv.writer(fichier)
    # obj.writerow(infos['amount'] + , + infos['label'] + , + infos['spender'])
    fichier.close()
    print("Expense Added !")
    return True


