import pandas as pd
import fileinput
import yagmail
import string
df = pd.read_csv('maillist.csv')
po = df.POBOX
email = df.Email
list = '0123456789/-X'
lower = str.upper('abcdefghijklmnopqrstuvwxyz')
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
def uniquenum():
    a = open('packagelist.txt', 'r')
    num = ''
    for row in a:
        if len(row) > 5:
            if row[5] in '0123456789':
                num = row[0:7]

    if len(num) >= 5:
        if num[5] != '9':
            z = int(num[5]) + 1
            if num[5] == '0':
                z = 1
            num = num[0:5] + str(z)
            return num
        elif num[4] != '9':
            z = int(num[4:6])
            z = z + 1
            if num[4] == '0':
                z = 10
            num = num[0:4] + str(z)
            return num
        elif num[3] != '9':
            z = int(num[3:6]) + 1
            if num[3] == '0':
                z = 100
            num = num[0:3] + str(z)
            return num
        elif num[2] != 'Z':
            q = 0
            while q < len(lower):
                if(row[2] == lower[q]):
                    break
                q += 1
            num = num[0:2] + lower[q + 1] + '000'
            return num
        elif num[1] != 'Z':
            q = 0
            while q < len(lower):
                if(row[1] == lower[q]):
                    break
                q += 1
            num = num[0:1] + lower[q + 1] + 'A' + '000'
            return num
        elif num[0] != 'Z':
            q = 0
            while q < len(lower):
                if(row[0] == lower[q]):
                    break
                q += 1
            num = lower[q + 1] + 'A' + 'A' + '000'
            return num
        else:
            return 'AAA000'
    else:
        return 'AAA000'
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
        if(len(line)+value <= maxvalue + 1 and q == 0 and row != ''):
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
        f = open('packagelist.txt', 'a')
        f.write('\n' + str(uniquenum()) + ',' + boxnum + ',' + place + ',' + str(value) + ',0')
        n = 0
        while n < len(po):
            if int(po[n]) == int(boxnum):
                send(str(email[n]))
            n += 1

static_run()
n = 999999999999
k = 0
#while k < n:
#    f = open('packagelist.txt', 'a')
 #   f.write('\n' + str(uniquenum()))


