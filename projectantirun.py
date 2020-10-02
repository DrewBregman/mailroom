import pandas as pd
import fileinput
import yagmail
df = pd.read_csv('maillist.csv')
po = df.POBOX
email = df.Email
list = '0123456789/-X'
def send(e):
    sender_email = 'seth.benson.test.email@gmail.com'
    receiver_email = e
    subject = "PACKAGE"
    sender_password = 'test123test'

    yag = yagmail.SMTP(user=sender_email, password=sender_password)

    contents = [
        "Hi",
        "You have a package",
    ]

    yag.send(receiver_email, subject, contents)
def static_run():
    maxvalue = 0
    boxnum = input('Enter PO #: ')
    value = int(input('Enter Size:'))
    place = ''
    q = 0
    for line in fileinput.input('Storage.txt', inplace=True):
        c = 0
        row = ''
        while c < len(line) and line[c] in list:
            row += line[c]
            c += 1
        if len(row) > 3 and row[0] == '0' and row[1] == '0' and row[2] == '0' and row[3] == '0':
            maxvalue = len(row)
        if(len(line)+value <= maxvalue + 1 and q == 0):
            q = 1
            c = 0
            while c < value:
                row += 'X'
                c += 1
            print(row + '\n', end='')
            place = row[0:6]
        else:
            print(row + '\n', end='')
    if place == '':
        print('no place for the package')
    else:
        print(place)
        n = 0
        while n < len(po):
            if int(po[n]) == int(boxnum):
                send(str(email[n]))
            n += 1

static_run()



