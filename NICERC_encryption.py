import os


def enigma():
    forward = [
        [2, 2, 2, -3, -3, 1, 2, -2, -1, 2, -1, 1, 2, -3, 3, -2, 3, 3, -3, -3, 2, -3, -1, 2, -1, -1],
        [1, -1, 1, 1, 1, -3, 2, -1, -1, 2, 2, -2, -2, 1, -1, 1, 1, -2, 2, -1, -1, 3, 3, -2, -2, -2],
        [3, -1, -1, 3, 3, -3, -2, -2, 1, -1, 1, -1, 3, -1, -1, -1, 2, 2, -2, -2, 3, 3, 3, -3, -3, -3]
    ]

    reverse = [
        [3, 3, -2, -2, -2, 2, -1, 1, -2, 1, 3, -2, -1, 2, -2, 3, 3, -3, 3, -3, -3, 1, -2, 1, 1, -2],
        [1, -1, 3, -1, -1, -1, 1, 1, -2, 2, 2, -2, -2, 1, -1, 2, -1, -1, 1, 1, -2, 2, 2, 2, -3, -3],
        [1, 1, 3, -3, 2, 2, -3, -3, 1, -1, 1, -1, 1, 1, 1, -3, 2, 2, -2, -2, 3, 3, 3, -3, -3, -3]
    ]

    next_inq = 'y'
    while next_inq == 'y':

        reflector = [4, 2, 5, -2, -4, 3, 5, -5, -3, 3, 4, -5, -3, 5, -4, 2, 4, -2, -5, 3, -4, 3, -3, 2, -3, -2]

        count = 0


        class Rotor:

            def __init__(self, f, b):
                self.f = f
                self.b = b

            def rotate(self, times):
                for i in range (times):
                    self.f.append(self.f[0])
                    self.f.pop(0)
                    self.b.append(self.b[0])
                    self.b.pop(0)


        def who_rotates(rotors, count):
            conditions = []
            who = []
            for i in range(rotors):
                conditions.append(26**i)
            conditions.reverse()
            for i in range(rotors):
                if count % conditions[i] == 0:
                    who.append(conditions.index(conditions[i]))
            return who


        def rotate(x,y):
            for i in range(y):
                x.append(x[0])
                x.pop(0)
            return x

        def value(x):
            v = list(x)
            v = [((ord(y)%32)-1) for y in v]
            return v


        selected = []
        quantity = int(input("How many rotors are in this Enigma? "))

        for i in range(quantity):
            selected.append(int(input('What rotor would you like at position ' + str(i + 1) + ' [ 1 , 2 , 3 ]  ')))

        chosen = []

        for i in selected:
            chosen.append(Rotor(list(forward[i-1]),list(reverse[i-1])))

        password = input('What is the ' + str(quantity + 2) + ' character key?  ')
        translate = input('what is hte message to encrypt / decrypt?  ')

        start_i = (ord(password[0]) % 32) - 1

        x = 0
        translation = ""

        for i in range(quantity):
            chosen[i].rotate(((value(password)[i+1]) + 26 - start_i) % 26)

        rotate(reflector, ((value(password)[-1]) + 26 - start_i) % 26)


        for a in range( len(translate)):
            if translate[a].isspace():
                translation = translation + ' '
            else:
                x = ((value(translate)[a]) + 26) % 26
                for b in range(quantity):
                    x = ((x + chosen[b].f[x]) + 26) % 26
                x = ((x + reflector[x]) + 26) % 26
                for c in range(quantity-1,-1,-1):
                    x = ((x + chosen[c].b[x]) + 26) % 26
                translation = translation + chr(x + 97)
                count += 1
                current_rotation = []
                current_rotation = who_rotates(quantity, count)

                for d in range(len(current_rotation)):
                    chosen[current_rotation[d]].rotate(1)

        print('\n', translation)

        next_inq = input('\nWould you like to start over? y / n   ')
    print('\nThank you')


def cesar():
    next_inq = "y"

    while next_inq == "y":

        translation = ""

        first = ord(input("Base letter? "))%32
        second = ord(input("\nShift to? "))%32
        shift = (second - first+26)%26

        phrase = input("What is the message to encrypt / decrypt? ")

        for a in range(0, len(phrase)):
            if phrase[a].isspace():
                translation = translation + " "

            else:
                if chr(((ord(phrase[a]))%32 + shift)%26+96) == "`":
                    translation = translation+"z"
                else:
                    translation = translation + chr(((ord(phrase[a]))%32 + shift)%26+96)

        print(translation)

        next_inq = input("\nWould you like to start over? y / n   ")
    print("\nThank you")


def morse_code():
    morse = [
        "-----",
        ".----",
        "..---",
        "...--",
        "....-",
        ".....",
        "-....",
        "--...",
        "---..",
        "----.",
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--.."
    ]
    next_inq = "y"
    while next_inq == "y":
        translation = ""
        msg = input("What would you like to convert? (with no punctuation)   ").lower()
        for i in range(len(msg)):
            if ord(msg[i]) >= 48 and ord(msg[i]) <= 57:
                translation += morse[ord(msg[i]) - 48]
            if msg[i] == " ":
                translation += "/"
            else:
                translation += morse[(ord(msg[i]) % 32) + 9]
            translation += "   "
        print(translation)
        next_inq = input("\nWould you like to start over? y/n   ")
    print("\nThank you")


def vigenere():
    next_inq = "y"

    while next_inq == "y":

        phrase = input("what is the phrase? ")

        key = input("\nWhat is the key? ")
        list1 = []
        list2 = []
        list3 = []
        translation = ""
        skip = 0

        decide = input("Would you like to encrypt or decrypt? ")

        if decide == "encrypt":

            for a in range(0, len(phrase)):
                list1.append(ord(phrase[a]) - 96)
            # print(list1)
            for a in range(0, len(key)):
                list2.append(ord(key[a]) - 96)
            # print(list2)

            list3 = list2 * (len(list1) // len(list2) + 1)
            # print(list1)
            # print(list2)
            # print(list3)

            for a in range(0, len(list1)):
                if list1[a] == -64:
                    translation = translation + " "
                    skip += 1
                else:
                    translation = translation + chr(((list1[a] + list3[a - skip] + 26) % 26) + 96)

            print(translation)

        if decide == "decrypt":

            for a in range(0, len(phrase)):
                list1.append(ord(phrase[a]) - 96)
            # print(list1)
            for a in range(0, len(key)):
                list2.append(ord(key[a]) - 96)
            # print(list2)
            list3 = list2 * (len(list1) // len(list2) + 1)
            for a in range(0, len(list1)):
                if list1[a] == -64:
                    translation = translation + " "
                    skip += 1
                else:
                    translation = translation + chr(((list1[a] - list3[a - skip] + 26) % 26) + 96)

            print(translation)

        next_inq = input("\nWould you like to start over? y / n   ")
    print("\nThank you")


active = True

while active == True:
    os.system('cls')
    option = input("\n[1] Enigma \n"
                   "[2] Cesar Cipher \n"
                   "[3] Vigenere Cipher \n"
                   "[4] Morse Code \n"
                   "[5] Exit \n \n"
                   "    Which Encryption method would you like to use?  ")
    if option == '1':
        os.system('cls')
        enigma()
    elif option == '2':
        os.system('cls')
        cesar()
    elif option == '3':
        os.system('cls')
        vigenere()
    elif option == '4':
        os.system('cls')
        morse_code()
    elif option == '5':
        active = False
    else:
        pass

print('\n Have a nice day.')