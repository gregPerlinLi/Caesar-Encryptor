def selectMode():
    while 1:
        print("Caesar Encryptor")
        print('Please select a mode：')
        print('Encrypt mode: 1')
        print('Decrypt mode: 2')
        mode = input()
        if mode in "1 2".split(' ',1):
            return mode
        else:
            print("Please input again：")


def inputMessage():
    if mode == 1:
        print('Please enter the message you want to encrypt: ')
    else:
        print('Please enter the message you want to decrypt: ')
    return input()


def inputKey():
    print("Please enter your key: ")
    getIn = input()
    #key = int(input())
    if getIn == "":
        key = 3
    else:
        key = int(getIn)
    return key


def encrypt(mode, message, key):
    if mode == '2':
        key = -key
    d = { }
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+key) % 26 + c)
    print("Result:")
    print("".join([d.get(c, c) for c in message]))


mode = selectMode()
message = inputMessage()
key = inputKey()
encrypt(mode, message, key)