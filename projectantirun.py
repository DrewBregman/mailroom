import pandas as pd
import fileinput
import yagmail
list = '0123456789/-X'
place = ''
size = ''
pobox = ''
def remove_run():
    place = ''
    size = ''
    pobox = ''
    id = input('Enter ID: ')
    for line in fileinput.input('packagelist.txt', inplace=True):
        if len(line) > 7 and line[0:6] == id:
            commacount = 0
            l = 0
            while l<len(line):
                if line[l] == ',':
                    commacount += 1
                elif commacount == 1:
                    pobox = pobox + line[l]
                elif commacount == 2:
                    place = place + line[l]
                elif commacount == 3:
                    size = size + line[l]
                l += 1
        else:
            print(line, end='')
    if place == '':
        print('no package found')
    else:
        print(place)
        print(pobox)
    for line in fileinput.input('Storage.txt', inplace=True):
        c = 0
        row = ''
        while c < len(line) and line[c] in list:
            row += line[c]
            c += 1
        if(len(row) > 6 and row[0:6] == place):
            row = row[0:len(row) - int(size)]
            print(row + '\n', end='')
        else:
            print(row + '\n', end='')

remove_run()



