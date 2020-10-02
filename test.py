import fileinput

for line in fileinput.input("test.txt", inplace=True):
    if line[0] == '3':
        line = '33'
        print('{}'.format(line + '\n'), end='')
    else:
        print('{} {}'.format(fileinput.filelineno(), line), end='') # for Python 3
    # print "%d: %s" % (fileinput.filelineno(), line), # for Python 2