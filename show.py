from PyInquirer import prompt, Separator
import csv
    # users.append({line[0:len(line)-1] : 0})

def show():
    file = open('users.csv', "r")
    lines = file.readlines()
    file.close()
    users = {}
    for line in lines:
        users[line[0:len(line)-1]] = int(0)
    with open('expense_report.csv') as f:
        DictReader_obj = csv.DictReader(f)
        for item in DictReader_obj:
            users[item['spender']] += float(item['amount'])
            for us in item['users'][0:len(item['users'])-1].split(','):
                print(users[us[2:len(us)-1]])
                users[us[2:len(us)-1]] = users[us[2:len(us)-1]] - float(item['amount']) / len(item['users'].split(','))
            # print(item)
    print('Balance : ',users)
    return True