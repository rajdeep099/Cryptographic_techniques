import random
import math
import numpy as np
import tkHyperlinkManager
from sympy import Matrix
from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import messagebox as mb
from tkinter.ttk import *
import webbrowser
import time
import sys
import mysql.connector
import smtplib


class Email:
    def sendEncryptedMail():
        to = input("Enter receivers Email Address: ")
        content = ' \n'
        temporaryStore = [i for i in array[3].split(',')]
        for ele in range(len(array)):
            if ele < 2:
                if ele == 0:
                    content += 'Text = '
                elif ele == 1:
                    content += 'Key = '
                content += str(array[ele])
                content += ', '
        for ele in temporaryStore:
            content += str(ele)
            content += ' '
        # print(content)
        try:
            sender_email = "--PUT SENDER's EMAIL ADDRESS HERE--"
            password = input(str("Enter your password: "))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.ehlo()
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, to, content)
            mb.showinfo("SENT", "E-Mail Sent")
        except Exception as e:
            e = str(e)
            if 'getaddrinfo failed' in e:
                mb.showerror("ERROR", "Please check your INTERNET CONNECTION")
            else:
                mb.showerror("ERROR", 'INVALD LOGIN CREDENTIALS')
        # server.close()

    def sendDecryptedMail():
        # correct it using decrypting_array 
        to = input("Enter receivers Email Address: ")
        content = ' '.join([str(elem) for elem in array])
        print(content)
        sender_email = "--put senders email address here--"
        password = input(str("Enter your password: "))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        print("Log in successful")
        server.sendmail(sender_email, to, content)
        print("Email sent")


class changeThemes:
    def alt(self):
        root.set_theme("alt")

    def aquativo(self):
        root.set_theme("aquativo")

    def clearlooks(self):
        root.set_theme("clearlooks")

    def default(self):
        root.set_theme("default")

    def itft1(self):
        root.set_theme("itft1")

    def plastik(self):
        root.set_theme("plastik")

    def scidblue(self):
        root.set_theme("scidblue")

    def scidgreen(self):
        root.set_theme("scidgreen")

    def scidgrey(self):
        root.set_theme("scidgrey")

    def scidmint(self):
        root.set_theme("scidmint")

    def kroc(self):
        root.set_theme("kroc")

    def blue(self):
        root.set_theme("blue")

    def scidsand(self):
        root.set_theme("scidsand")

    def smog(self):
        root.set_theme("smog")

    def vista(self):
        root.set_theme("vista")

    def winnative(self):
        root.set_theme("winnative")

    def winxpblue(self):
        root.set_theme("winxpblue")

    def black(self):
        root.set_theme("black")


class writeHistory:
    def encrypt(self, tech):
        query = "INSERT INTO <table name> VALUES (%s, %s, %s, %s, %s, %s)"
        tech = tech.split(',')
        inserted_values = (tech[0], tech[1], array[2], array[1], array[0], time.ctime())
        mycursor.execute(query, inserted_values)
        myDb.commit()

    def decrypt(self, tech):
        query = "INSERT INTO <table name> VALUES (%s, %s, %s, %s, %s, %s)"
        tech = tech.split(',')
        inserted_values = (
            tech[0], tech[1], decryption_array[0], decryption_array[1], decryption_array[2], time.ctime())
        mycursor.execute(query, inserted_values)
        myDb.commit()


def deleteHistory():
    mycursor.execute("DELETE FROM <table name> WHERE e_d = 'E'")
    myDb.commit()
    mycursor.execute("DELETE FROM <table name> WHERE e_d = 'D'")
    myDb.commit()
    historyClicked()


def adjustClicked():
    global adjustFrame
    if destroyFrameArr[1] == 0:
        pass
    if destroyFrameArr[0] == 1:
        adjustFrame.destroy()
        destroyFrameArr[0] = 0
    elif destroyFrameArr[1] == 1:
        historyFrame.destroy()
        destroyFrameArr[1] = 0
    destroyFrameArr[0] = 1
    adjustFrame = Frame(height=290, width=880, relief=SUNKEN)
    adjustFrame.pack(side=RIGHT, padx=5, pady=5)

    ch = changeThemes()
    themeStore = PhotoImage(file="img//themeStore.png")
    l = Label(adjustFrame, image=themeStore, relief=RIDGE)
    l.image = themeStore
    l.place(x=405, y=40)

    ALT = Button(adjustFrame, text="alt", command=ch.alt)
    ALT.place(x=10, y=10)
    AQUATIVO = Button(adjustFrame, text="aquativo", command=ch.aquativo)
    AQUATIVO.place(x=130, y=10)
    CLEARLOOKS = Button(adjustFrame, text="clearlooks", command=ch.clearlooks)
    CLEARLOOKS.place(x=270, y=10)
    DEFAULT = Button(adjustFrame, text="default", command=ch.default)
    DEFAULT.place(x=10, y=60)
    ITFT1 = Button(adjustFrame, text="itft1", command=ch.itft1)
    ITFT1.place(x=130, y=60)
    PLASTIK = Button(adjustFrame, text="plastik", command=ch.plastik)
    PLASTIK.place(x=270, y=60)
    SCIDBLUE = Button(adjustFrame, text="scidblue", command=ch.scidblue)
    SCIDBLUE.place(x=10, y=110)
    SCIDGREEN = Button(adjustFrame, text="scidgreen", command=ch.scidgreen)
    SCIDGREEN.place(x=130, y=110)
    SCIDGREY = Button(adjustFrame, text="scidgrey", command=ch.scidgrey)
    SCIDGREY.place(x=270, y=110)
    SCIDMINT = Button(adjustFrame, text="scidgmint", command=ch.scidmint)
    SCIDMINT.place(x=10, y=160)
    KROC = Button(adjustFrame, text="kroc", command=ch.kroc)
    KROC.place(x=130, y=160)
    BLUE = Button(adjustFrame, text="blue", command=ch.blue)
    BLUE.place(x=270, y=160)
    SCIDSAND = Button(adjustFrame, text="scidsand", command=ch.scidsand)
    SCIDSAND.place(x=10, y=210)
    SMOG = Button(adjustFrame, text="smog", command=ch.smog)
    SMOG.place(x=130, y=210)
    VISTA = Button(adjustFrame, text="vista", command=ch.vista)
    VISTA.place(x=270, y=210)
    WINNATIVE = Button(adjustFrame, text="winnative", command=ch.winnative)
    WINNATIVE.place(x=10, y=255)
    WINXPBLUE = Button(adjustFrame, text="winxpblue", command=ch.winxpblue)
    WINXPBLUE.place(x=130, y=255)
    BLACK = Button(adjustFrame, text="black", command=ch.black)
    BLACK.place(x=270, y=255)


def historyClicked():
    global historyFrame
    if destroyFrameArr[0] == 0:
        pass
    if destroyFrameArr[1] == 1:
        historyFrame.destroy()
        destroyFrameArr[1] = 0
    elif destroyFrameArr[0] == 1:
        adjustFrame.destroy()
        destroyFrameArr[0] = 0
    destroyFrameArr[1] = 1

    historyFrame = Frame(height=290, width=880, relief=SUNKEN)
    historyFrame.pack(side=RIGHT, padx=5, pady=5)

    query = "SELECT * FROM <table name>"
    mycursor.execute(query)
    result = mycursor.fetchall()

    if len(result) > 0:

        # prepare a textbox
        deleteHistoryImg = PhotoImage(file="img//delete.png")
        smallImg = deleteHistoryImg.subsample(4, 4)
        deleteHistoryButton = Button(historyFrame, image=smallImg, command=deleteHistory)
        deleteHistoryButton.image = smallImg
        deleteHistoryButton.place(x=830, y=2)
        historyDisplay = Text(historyFrame, wrap=WORD, height=15, width=106)
        scroll = Scrollbar(historyFrame)
        scroll.place(x=860, y=120)
        historyDisplay.place(x=7, y=33)
        scroll.config(command=historyDisplay.yview)
        historyDisplay.config(yscrollcommand=scroll.set)
        historyDisplay.tag_configure('tag_center', justify='left')
        historyDisplay.tag_configure('small', font=('Verdana', 7))

        # labels
        colNames = Label(historyFrame,
                         text="Technique used  |  E / D  |                     Given Text                     |                  Key Used                  |                        Received Text                        |                  Date")
        colNames.place(x=10, y=7)

        for i in result:
            formatted_history = ""
            t_used = i[0]
            EOrD = i[1]
            g_text = i[2]
            k_used = i[3]
            r_text = i[4]
            dateNtime = i[5]
            reqLen = 20 - len(t_used)
            formatted_history += t_used
            formatted_history += " " * reqLen
            formatted_history += "|     "
            formatted_history += EOrD
            formatted_history += "     |"
            reqLen = 62 - len(g_text) * 2
            formatted_history += g_text
            formatted_history += " " * reqLen
            formatted_history += "|"
            reqKLen = 51 - len(k_used) * 2
            formatted_history += k_used
            formatted_history += " " * reqKLen
            formatted_history += "| "
            reqLen = 70 - len(r_text) * 2
            formatted_history += r_text
            formatted_history += " " * reqLen
            formatted_history += "| "
            formatted_history += dateNtime
            formatted_history += "\n"
            historyDisplay.insert(END, formatted_history, 'small')

    elif len(result) == 0:
        noInternet = PhotoImage(file="img//clock.png")
        displayNoInternet = Label(historyFrame, image=noInternet)
        displayNoInternet.image = noInternet
        displayNoInternet.place(x=400, y=100)
        textLabel = Label(historyFrame, text="No history here")
        textLabel.place(x=390, y=170)


def destroy():
    global count
    count = 0
    adjustButton.destroy()
    historyButton.destroy()
    if destroyFrameArr[0] == 1:
        adjustFrame.destroy()
    if destroyFrameArr[1] == 1:
        historyFrame.destroy()
    if destroyFrameArr[2] == 1:
        destroyFrameArr[2] = 0
        backgroundFrame.destroy()


def showAll():
    global count, adjustButton, historyButton, backgroundFrame
    count += 1
    if count % 2 != 0:
        backgroundFrame = Frame(height=236, width=90, relief=SUNKEN)
        backgroundFrame.place(x=5, y=59)
        destroyFrameArr[2] = 1
        adjustButton = Button(root, image=pic2, command=adjustClicked)
        adjustButton.place(x=20, y=74)
        historyButton = Button(root, image=photo4, command=historyClicked)
        historyButton.place(x=20, y=127)
    if count % 2 == 0:
        destroy()
        backgroundFrame.destroy()


class additionalButtonEvents:
    def __init__(self):
        self.img = PhotoImage(file='img//down-arrow.png')

    def callbackFunction1(self):
        string = time.ctime()
        updatedStr = "(E)"

        for i in string:
            if i.isalnum():
                updatedStr += i
            else:
                updatedStr += '_'

        updatedStr += '.txt'

        if mb.askokcancel("", "Continue download?"):
            f = open(updatedStr, '+w')
            f.write("Plain text: " + array[2] + "\nKey used: " + str(array[1]) + "\nCipher text: " + array[0])
            # f = open(updatedStr, 'r')
            mb.showinfo("SAVED", "file is saved as " + updatedStr)
        else:
            pass

    def callbackFunction2(self):
        string = time.ctime()
        updatedStr = "(D)"

        for i in string:
            if i.isalnum():
                updatedStr += i
            else:
                updatedStr += '_'

        updatedStr += '.txt'
        if mb.askokcancel("", "Continue download?"):
            f = open(updatedStr, '+w')
            f.write(
                "Cipher text: " + decryption_array[0] + "\nKey used: " + str(decryption_array[1]) + "\nPlain text: " +
                decryption_array[2])
            # f = open(updatedStr, 'r')
            mb.showinfo("SAVED", "file is saved as " + updatedStr)
        else:
            pass

    def press(self, event):
        self.e.config(image=self.img)

    def release(self, event):
        self.e.config(image=self.img)
        self.callbackFunction()


def additionalButtonEvents_Main(operation):
    obj = additionalButtonEvents()
    img = PhotoImage(file='img//down-arrow.png')
    small_img = img.subsample(2, 2)
    global download1, download2
    if operation == 'displayCipherText':
        download1 = Button(root, image=small_img, command=obj.callbackFunction1)
        download1.place(x=670, y=102)
    if operation == 'displayPlainText':
        download2 = Button(root, image=small_img, command=obj.callbackFunction2)
        download2.place(x=670, y=222)
    e = Label(root, image=img)
    e.bind('<ButtonPress-1>', obj.press)
    e.bind('<ButtonRelease-1>', obj.release)
    root.mainloop()


def getPlainText():
    text = plain_text.get()
    return text


def getKey():
    key = e_key.get()
    return key


def getDecryptionKey():
    key = d_key.get()
    return key


def copyValnKey():
    if variable.get() == "RSA algorithm":
        pos = 0
        encrypted_cipher_text.insert(0, array[0])
        d_key.insert(pos, "PRIME 1:")
        pos += 10
        d_key.insert(pos, array[1])
        pos += len(str(array[1])) + 5
        d_key.insert(pos, ", PRIME 2:")
        pos += 10
        d_key.insert(pos, array[2])
        pos += len(str(array[2])) + 5
        d_key.insert(pos, ", ENCRYPTION KEY:")
        pos += 17
        d_key.insert(pos, array[3])

    # elif variable.get() == "CBC mode":
    #     encrypted_cipher_text.insert(0, array[0])
    #     d_key.insert(0, "Initialisation Vector: ")
    #     d_key.insert(24, int(array[2],2))
    #     l = len(str(int(array[2],2)))
    #     d_key.insert(25+l, " , Key: ")
    #     d_key.insert(31+l, array[1])

    else:
        encrypted_cipher_text.insert(0, array[0])
        d_key.insert(0, array[1])


def getCipherText():
    text = encrypted_cipher_text.get()
    return text


def displayPlainText(plainText):
    operation = 'displayPlainText'
    global plainDisplay
    plainDisplay = Entry(root)
    displayController[1] = 1
    plainDisplay.insert(0, plainText)
    plainDisplay.place(x=600, y=235, anchor=CENTER)
    additionalButtonEvents_Main(operation)


def displayCipherText(cipherText):
    operation = 'displayCipherText'
    global cipherDisplay
    cipherDisplay = Entry(root)
    displayController[0] = 1
    cipherDisplay.insert(1, cipherText)
    cipherDisplay.place(x=600, y=115, anchor=CENTER)
    additionalButtonEvents_Main(operation)


def exceptionHandling(e):
    T.tag_configure('err', font=('Verdana', 8), foreground="red")
    T.insert(END, "\n", 'tag_center')
    T.insert(END, sys.exc_info()[0], 'err')
    T.insert(END, e, 'err')
    T.insert(END, "\n")


def pt_modification(pT):
    reformatted_pT = ""
    for i in pT:
        if i.isupper():
            reformatted_pT += i.lower()
        elif i.isspace():
            reformatted_pT += " "
        elif not i.isalpha():
            raise NameError("Only alphabets and spaces are allowed")
        else:
            reformatted_pT += i
    plainTextArr = [str(i) for i in reformatted_pT]
    return plainTextArr


def caesarCipher():
    ## encryption
    try:
        tech = "caesar cipher,E"
        s = getPlainText()
        main_key = int(getKey())
        key = main_key % 25
        plainTextArr = pt_modification(s)
        for i in range(len(plainTextArr)):
            if plainTextArr[i].isspace():
                pass
            else:
                val = ord(plainTextArr[i]) - key
                if val < 97:
                    val = val + 26
                plainTextArr[i] = chr(val)
        cipherText = ""
        for i in plainTextArr:
            cipherText += i
        array.append(cipherText)
        array.append(main_key)
        array.append(s)
        array.append(tech)
        displayCipherText(cipherText)
        wHis.encrypt(tech)
    except Exception as e:
        exceptionHandling(e)


def caesar_cipher_decryption():
    ## decryption
    try:
        tech = "caesar cipher,D"
        cT = getCipherText()
        cipherTextArr = pt_modification(cT)
        d_Key = getDecryptionKey()
        key = int(d_Key) % 25
        for i in range(len(cipherTextArr)):
            if cipherTextArr[i].isspace():
                pass
            else:
                val = ord(cipherTextArr[i]) + key
                if val > 122:
                    val = val - 122 + 96
                cipherTextArr[i] = chr(val)
        plainText = ""
        for i in cipherTextArr:
            plainText += i
        decryption_array.append(cT)
        decryption_array.append(d_Key)
        decryption_array.append(plainText)
        displayPlainText(plainText)
        wHis.decrypt(tech)
    except Exception as e:
        exceptionHandling(e)


def hillCipher():
    ## encryption
    try:
        tech = "Hill cipher,E"
        pT = getPlainText()
        modified_plain_text = ""
        plainTextArr = []
        for i in pT:
            if i.isspace():
                pass
            else:
                modified_plain_text += i
                plainTextArr.append(i)

        for i in range(len(plainTextArr)):
            if plainTextArr[i].isupper():
                plainTextArr[i] = ord(plainTextArr[i]) % 65
            elif plainTextArr[i].islower():
                plainTextArr[i] = ord(plainTextArr[i]) % 97

        while True:
            flag = 0
            try:
                key = [[random.randint(0, 25) for _ in range(len(plainTextArr))] for _ in range(len(plainTextArr))]
                inverse_key = Matrix(key).inv_mod(26)
                flag = 1
            except Exception as e:
                pass
            if flag == 1:
                break
        keyString = ""
        for i in range(len(key)):
            for j in range(len(key)):
                keyString += chr(key[i][j] + 65)

        ## matrix multiplication
        cipherTextArray = []
        for i in range(len(key)):
            add = 0
            for j in range(len(key)):
                add += key[i][j] * plainTextArr[j]
            cipherTextArray.append(add % 26)
        cT = ""
        for i in range(len(modified_plain_text)):
            cT += chr(cipherTextArray[i] + 97)

        array.append(cT)
        array.append(keyString)
        array.append(pT)
        array.append(tech)
        displayCipherText(cT)
        wHis.encrypt(tech)
    except Exception as e:
        exceptionHandling(e)


def hill_cipher_decryption():
    ## decryption
    try:
        tech = "Hill cipher,D"
        getcT = getCipherText()
        modifiedCT = ""
        for i in getcT:
            if i.isspace():
                pass
            else:
                modifiedCT += i
        cipherTextArray = []
        for i in modifiedCT:
            cipherTextArray.append(ord(i.lower()) - 97)
        getkey = getDecryptionKey()
        key = []
        j = 0
        i = 0
        times = 0
        while i < len(getkey):
            tempArr = []
            for j in range(int(math.sqrt(len(getkey)))):
                tempArr.append(ord(getkey[i + j].lower()) - 97)
            key.append(tempArr)
            i += int(math.sqrt(len(getkey)))

        try:
            inverse_key = Matrix(key).inv_mod(26)
            inverse_key = np.array(inverse_key)  # sympy to numpy
            inverse_key = inverse_key.astype(float)
            decryptedPlainTextArr = []
            for i in range(len(inverse_key)):
                add = 0
                for j in range(len(inverse_key)):
                    add += inverse_key[i][j] * cipherTextArray[j]
                decryptedPlainTextArr.append(add % 26)
            plainText = ""
            for i in range(len(decryptedPlainTextArr)):
                plainText += chr(int(decryptedPlainTextArr[i]) + 97)
            displayPlainText(plainText)

            decryption_array.append(getcT)
            decryption_array.append(getkey)
            decryption_array.append(plainText)
            wHis.decrypt(tech)
        except Exception as e:
            mb.showerror("ERROR", "Key is not accepted")
    except Exception as e:
        exceptionHandling(e)


def vernam_cipher():
    try:
        tech = "Vernam cipher,E"
        pT = getPlainText()
        pTArray = pt_modification(pT)
        plainTextArr = []
        count_chr_in_pT = count_chr_in_key = 0

        for i in pTArray:
            if i == " ":
                plainTextArr.append(-1)
            else:
                plainTextArr.append(ord(i) % 97)
                count_chr_in_pT += 1

        keyString = getKey()
        keyArray = pt_modification(keyString)
        keyArr = []
        for i in keyArray:
            if i == " ":
                pass
            else:
                keyArr.append(ord(i) % 97)
                count_chr_in_key += 1

        ## encryption
        cipherArray = []
        if count_chr_in_pT == count_chr_in_key:
            i = j = 0
            while i < len(plainTextArr):
                if plainTextArr[i] == -1:
                    cipherArray.append(-65)  # (-65 + 97 = 32, which is ascii of "space")
                else:
                    cipherArray.append((plainTextArr[i] + keyArr[j]) % 26)
                    j += 1
                i += 1
        elif count_chr_in_pT != count_chr_in_key:
            raise NameError("Length of key and length of plain text must be same\n")
        cT = ""
        for i in cipherArray:
            cT += chr(i + 97)
        print(cT)
        array.append(cT)
        array.append(keyString)
        array.append(pT)
        array.append(tech)
        displayCipherText(cT)
        wHis.encrypt(tech)
    except Exception as e:
        exceptionHandling(e)


def vernam_cipher_decryption():
    ## decryption
    try:
        tech = "Vernam cipher,D"
        cipherArray = []
        keyArr = []
        cT = getCipherText()
        cTArray = pt_modification(cT)
        count_chr_in_cT = count_chr_in_key = 0

        for i in cTArray:
            if i == " ":
                cipherArray.append(-1)
            else:
                cipherArray.append(ord(i) % 97)
                count_chr_in_cT += 1

        decryption_key = getDecryptionKey()
        keyArray = pt_modification(decryption_key)

        for i in keyArray:
            if i == " ":
                pass
            else:
                keyArr.append(ord(i) % 97)
                count_chr_in_key += 1

        if count_chr_in_cT != count_chr_in_key:
            raise NameError("Length of key and length of cipher text must have to be equal.\n")
        decrypted_cipherText = []
        i = j = 0
        while i < len(cipherArray):
            if cipherArray[i] == -1:
                decrypted_cipherText.append(-65)
            else:
                decrypted_cipherText.append((cipherArray[i] - keyArr[j]) % 26)
                j += 1
            i += 1

        pT = ""
        for i in decrypted_cipherText:
            pT += chr(i + 97)
        decryption_array.append(cT)
        decryption_array.append(decryption_key)
        decryption_array.append(pT[0:])
        displayPlainText(pT[0:])
        wHis.decrypt(tech)
    except Exception as e:
        exceptionHandling(e)


def playfair_cipher():
    try:
        tech = "Play Fair cipher,E"
        plainText = getPlainText()
        pTArray = pt_modification(plainText)
        count_chr_in_pT = 0
        pos_of_spaces = []
        pT = ""
        for i in range(len(pTArray)):
            if pTArray[i] == 'j':
                pT += 'i'
            if pTArray[i] == ' ':
                count_chr_in_pT -= 1  # do not count if the char is a space
                pos_of_spaces.append(i)
            else:
                pT += pTArray[i]
            count_chr_in_pT += 1

        if count_chr_in_pT % 2 != 0:
            pT = pT + 'z'
        print('plain text = ', pT)

        ## key generation
        keyString = getKey()
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                     "v", "w", "x", "y", "z"]
        temp_key = []
        keyArray = pt_modification(keyString)
        for i in keyArray:
            if i == " ":
                pass
            elif i not in temp_key and i != 'j':
                temp_key.append(i)
            elif i == 'j':
                temp_key.append('i')
        for i in alphabets:
            if i not in temp_key:
                temp_key.append(i)
        key = []
        count = 0
        for i in range(5):
            temp = []
            for j in range(5):
                temp.append(temp_key[count])
                count += 1
            key.append(temp)
        print("key:", key)
        ##     forming plain_text subsets
        plainTextArr = []
        temp = []
        for i in pT:
            temp.append(i)
            if len(temp) == 2:
                plainTextArr.append(temp)
                temp = []
        print("plain text arr:", plainTextArr)
        ## encryption
        plainTextPositions = []
        for i in range(len(plainTextArr)):
            useless_temp = []
            for j in range(len(plainTextArr[i])):
                character = plainTextArr[i][j]
                for x in range(5):
                    for y in range(5):
                        if character == key[x][y]:
                            useless_temp.append([x, y])
            plainTextPositions.append(useless_temp)
        print("plain text pos:", plainTextPositions)
        for i in range(len(plainTextPositions)):
            tempArr = []
            if plainTextPositions[i][0][0] == plainTextPositions[i][1][0]:
                ## row
                tempArr.append([plainTextPositions[i][0][0], (plainTextPositions[i][0][1] + 1) % 5])
                tempArr.append([plainTextPositions[i][1][0], (plainTextPositions[i][1][1] + 1) % 5])
                plainTextPositions[i] = tempArr
            elif plainTextPositions[i][0][1] == plainTextPositions[i][1][1]:
                ## col
                tempArr.append([(plainTextPositions[i][0][0] + 1) % 5, plainTextPositions[i][0][1]])
                tempArr.append([(plainTextPositions[i][1][0] + 1) % 5, plainTextPositions[i][1][1]])
                plainTextPositions[i] = tempArr
            else:
                ## diagonal
                tempArr.append([plainTextPositions[i][0][0], plainTextPositions[i][1][1]])
                tempArr.append([plainTextPositions[i][1][0], plainTextPositions[i][0][1]])
                plainTextPositions[i] = tempArr

        cT = ""
        cT_len = i = 0
        while i < len(plainTextPositions):
            j = 0
            while j < len(plainTextPositions[i]):
                if cT_len in pos_of_spaces:
                    cT += " "
                else:
                    cT += key[plainTextPositions[i][j][0]][plainTextPositions[i][j][1]]
                    j += 1
                cT_len += 1
            i += 1
        print("cipher text = ", cT)
        array.append(cT)
        array.append(keyString)
        array.append(plainText)
        array.append(tech)
        displayCipherText(cT)
        wHis.encrypt(tech)
    except Exception as e:
        exceptionHandling(e)


def playfair_cipher_decryption():
    ## decryption
    try:
        tech = "Play Fair cipher,D"
        cT = getCipherText()
        cTArray = pt_modification(cT)
        pos_of_spaces = []
        cipher_text = ""
        for i in range(len(cTArray)):
            if cTArray[i] == " ":
                pos_of_spaces.append(i)
            elif cTArray[i] == "j":
                cipher_text += "i"
            else:
                cipher_text += cTArray[i]

        if len(cipher_text) % 2 != 0:
            cipher_text += "z"

        dKey = getDecryptionKey()
        keyArray = pt_modification(dKey)
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                     "v", "w", "x", "y", "z"]
        temp_key = []
        for i in keyArray:
            if i == " ":
                pass
            elif i not in temp_key and i != "j":
                temp_key.append(i)
            elif i == "j":
                temp_key.append("i")
        for i in alphabets:
            if i not in temp_key:
                temp_key.append(i)
        key = []
        count = 0
        for i in range(5):
            temp = []
            for j in range(5):
                temp.append(temp_key[count])
                count += 1
            key.append(temp)

        cipher_text_pos = []
        for i in cipher_text:
            temp = []
            for j in range(5):
                for k in range(5):
                    if i == key[j][k]:
                        temp.append(j)
                        temp.append(k)
                        cipher_text_pos.append(temp)
                        break

        cipherTextPositions = []
        temp = []
        i = 0
        while i < len(cipher_text_pos):
            temp.append(cipher_text_pos[i])
            i += 1
            if i % 2 == 0:
                cipherTextPositions.append(temp)
                temp = []

        print('key ', key)
        for i in range(len(cipherTextPositions)):
            tempArr = []
            if cipherTextPositions[i][0][0] == cipherTextPositions[i][1][0]:
                ## row
                tempArr.append([cipherTextPositions[i][0][0],
                                (cipherTextPositions[i][0][1] - 1) % 5])  # right shift in row i.e. same row diff col
                tempArr.append([cipherTextPositions[i][1][0], (cipherTextPositions[i][1][1] - 1) % 5])
                cipherTextPositions[i] = tempArr
            elif cipherTextPositions[i][0][1] == cipherTextPositions[i][1][1]:
                ## col
                tempArr.append([(cipherTextPositions[i][0][0] - 1) % 5, cipherTextPositions[i][0][1]])
                tempArr.append([(cipherTextPositions[i][1][0] - 1) % 5, cipherTextPositions[i][1][1]])
                cipherTextPositions[i] = tempArr
            else:
                ## diagonal
                tempArr.append([cipherTextPositions[i][0][0], cipherTextPositions[i][1][1]])
                tempArr.append([cipherTextPositions[i][1][0], cipherTextPositions[i][0][1]])
                cipherTextPositions[i] = tempArr

        decrypted_plain_text = ""
        i = count = 0
        while i < len(cipherTextPositions):
            j = 0
            while j < len(cipherTextPositions[i]):
                if count in pos_of_spaces:
                    decrypted_plain_text += " "
                else:
                    decrypted_plain_text += key[cipherTextPositions[i][j][0]][cipherTextPositions[i][j][1]]
                    j += 1
                count += 1
            i += 1

        print("decrypted text = ", decrypted_plain_text)
        decryption_array.append(cT)
        decryption_array.append(dKey)
        decryption_array.append(decrypted_plain_text)
        displayPlainText(decrypted_plain_text)
        wHis.decrypt(tech)
    except Exception as e:
        exceptionHandling(e)


def ECB_mode():
    tech = "ECB mode cipher,E"
    pT = getPlainText()
    if len(pT) % 8 != 0:
        for i in range(8 - (len(pT) % 8)):
            pT += " "
    plainTextArr = []
    count = 0
    for i in range(int(len(pT) / 8)):
        temp = []
        for j in range(8):
            temp.append(pT[count])
            count += 1
        plainTextArr.append(temp)

        ## convert each block of 8 characters/english alphabet to 64 bits
    for i in range(len(plainTextArr)):
        for j in range(len(plainTextArr[i])):
            decimal_val = ord(plainTextArr[i][j])
            binary_val = bin(decimal_val)[2:]
            binary_val = binary_val.zfill(8)
            plainTextArr[i][j] = [int(i) for i in binary_val]

    for i in range(len(plainTextArr)):
        temp_store = []
        for j in range(len(plainTextArr[i])):
            for k in range(len(plainTextArr[i][j])):
                temp_store.append(plainTextArr[i][j][k])
        plainTextArr[i] = temp_store

    key_string = getKey()
    temp_value = 1
    for i in key_string:
        temp_value *= ord(i)
    binary_key_val = bin(temp_value)[2:]
    binary_key_val = binary_key_val.zfill(64)
    binary_key_val = [int(i) for i in binary_key_val]  # +convert the binary key from string to list

    ## encryption
    # XOR operation
    XOR_array = []
    for i in range(len(plainTextArr)):
        temp_store = []
        for j in range(len(plainTextArr[i])):
            if plainTextArr[i][j] == binary_key_val[j]:
                temp_store.append(0)
            else:
                temp_store.append(1)
        XOR_array.append(temp_store)

    will_use_for_decryption = list.copy(XOR_array)
    for i in range(len(XOR_array)):
        temp_store = []
        count = 0
        for j in range(8):
            temp = ""
            for k in range(8):
                temp += str(XOR_array[i][count])
                count += 1
            temp_store.append(temp)
        XOR_array[i] = temp_store

    cT = ""
    for i in range(len(XOR_array)):
        for j in range(len(XOR_array[i])):
            cT += chr(int(XOR_array[i][j], 2))
    print("cipher text =", cT)
    array.append(cT)
    array.append(key_string)
    array.append(pT)
    array.append(tech)
    displayCipherText(cT)
    wHis.encrypt(tech)


def ECB_mode_decryption():
    ## decryption
    # again perform XOR operation with key
    tech = "ECB mode cipher,D"
    cT = getCipherText()
    dKey = getDecryptionKey()

    if len(cT) % 8 != 0:
        while len(cT) % 8 != 0:
            cT += " "

    cTArray = keyArray = []
    count = 0
    for i in range(len(cT) // 8):
        temp_store = []
        for j in range(8):
            temp_store.append(cT[count])
            count += 1
        cTArray.append(temp_store)

    for i in range(len(cTArray)):
        for j in range(len(cTArray[i])):
            bin_val = bin(ord(cTArray[i][j]))
            cTArray[i][j] = bin_val[2:].zfill(8)

    cipher_64_array = []
    for i in range(len(cTArray)):
        temp_store = []
        for j in range(len(cTArray[i])):
            for k in cTArray[i][j]:
                temp_store.append(int(k))
        cipher_64_array.append(temp_store)

    d_key_product = 1
    for i in dKey:
        d_key_product *= ord(i)

    binary_key_val = [int(i) for i in bin(d_key_product)[2:].zfill(64)]

    will_use_for_decryption = cipher_64_array
    XOR_array = []
    for i in range(len(will_use_for_decryption)):
        temp_store = []
        count = 0
        for j in range(8):
            decrypted_binary = ""
            for k in range(8):
                if will_use_for_decryption[i][count] == binary_key_val[count]:
                    decrypted_binary += "0"
                else:
                    decrypted_binary += "1"
                count += 1
            temp_store.append(decrypted_binary)
        XOR_array.append(temp_store)

    decrypted_plain_text = ""
    for i in range(len(XOR_array)):
        for j in range(len(XOR_array[i])):
            decrypted_plain_text += chr(int(XOR_array[i][j], 2))
    print("decrypted text = ", decrypted_plain_text)
    displayPlainText(decrypted_plain_text)
    decryption_array.append(cT)
    decryption_array.append(dKey)
    decryption_array.append(decrypted_plain_text)
    wHis.decrypt(tech)


def RSA_algorithm():
    plain_text = getPlainText()
    # finding prime numbers
    prime_numbers = []
    for i in range(2, 1000):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            prime_numbers.append(i)

    pos1, pos2 = random.randint(0, len(prime_numbers) - 150), random.randint(0, len(prime_numbers))
    if pos1 < pos2:
        P = prime_numbers[pos1]
        Q = prime_numbers[pos2]
    else:
        P = prime_numbers[pos2]
        Q = prime_numbers[pos1]

    N = P * Q
    fi_N = (P - 1) * (Q - 1)

    # encryption

    # finding private key (e)
    e = None
    element_found = False
    for i in range(2, fi_N):
        flag = 1
        if element_found:
            break
        for j in range(2, i + 1):
            if i % j == 0:
                if N % j == 0 or fi_N % j == 0:
                    flag = 0
                    break
                if flag == 1:
                    e = i
                    element_found = True
                    break

    cipher_text = ""
    for i in plain_text:
        cipher_text += chr((ord(i) ** e) % N)

    array.append(cipher_text)
    array.append(P)
    array.append(Q)
    array.append(e)
    displayCipherText(cipher_text)


def RSA_algorithm_decryption():
    ## decryption
    cipher_text = getCipherText()
    e = array[3]
    P = array[1]
    Q = array[2]

    N = P * Q
    fi_N = (P - 1) * (Q - 1)

    i = 1
    while (i * e) % fi_N != 1:
        i += 1

    d = i
    pT = ""
    for i in cipher_text:
        pT += chr((ord(i) ** d) % N)

    displayPlainText(pT)


def CBC_mode():
    plain_text = getPlainText()
    cipher_text = ""

    IV = random.randint(1, 18446744073709551615)

    IV = bin(IV)[2:].zfill(64)
    IV_64_bit = [int(i) for i in IV]

    if len(plain_text) % 8 != 0:
        plain_text += " " * (8 - (len(plain_text) % 8))

    curr_pos = 0
    block_no = 0

    key = getKey()
    key_product = 1
    for i in key:
        key_product *= ord(i)

    key_64_bit = [int(i) for i in bin(key_product)[2:].zfill(64)]

    while curr_pos < len(plain_text):
        plain_text_block = [bin(ord(plain_text[curr_pos]))[2:].zfill(8) for curr_pos in
                            range(block_no * 8, 8 * (block_no + 1))]
        block_no += 1
        curr_pos += 8

        plain_text_block_64_bit = []
        for i in plain_text_block:
            for j in i:
                plain_text_block_64_bit.append(int(j))

        # XOR plain text block(64 bits) with IV of 64 bits
        XOR_64_bit = []
        for i in range(64):
            if plain_text_block_64_bit[i] == IV_64_bit[i]:
                XOR_64_bit.append(0)
            else:
                XOR_64_bit.append(1)

        # Now use this XOR and ENCRYPT using 64 bit KEY

        XOR_CT_64_bit = []
        for i in range(64):
            if XOR_64_bit[i] == key_64_bit[i]:
                XOR_CT_64_bit.append(0)
            else:
                XOR_CT_64_bit.append(1)

        IV_64_bit = XOR_CT_64_bit  # for next round

        CT_8X8 = []
        count = 0
        for i in range(8):
            temp = ""
            for j in range(8):
                temp += str(XOR_CT_64_bit[count])
                count += 1
            CT_8X8.append(chr(int(temp, 2)))

        for i in CT_8X8:
            cipher_text += i

    array.append(cipher_text)
    array.append(key)
    array.append(IV)
    displayCipherText(cipher_text)


def CBC_mode_decryption():
    IV = array[2]
    decrypted_text = ""
    IV_64_bit = [int(i) for i in IV]
    cipher_text = getCipherText()
    d_key = getDecryptionKey()

    if len(cipher_text) % 8 != 0:
        cipher_text += " " * (8 - (len(cipher_text) % 8))

    curr_pos = 0
    block_no = 0

    Dkey_product = 1
    for i in d_key:
        Dkey_product *= ord(i)

    d_key_64_bit = [int(i) for i in bin(Dkey_product)[2:].zfill(64)]

    while curr_pos < len(cipher_text):
        cipher_text_block = [bin(ord(cipher_text[curr_pos]))[2:].zfill(8) for curr_pos in
                             range(block_no * 8, 8 * (block_no + 1))]
        block_no += 1
        curr_pos += 8

        cipher_text_64_bit = []
        for i in cipher_text_block:
            for j in i:
                cipher_text_64_bit.append(int(j))

        # XOR cipher_text_64_bit with 64 bit key
        XOR_CT_Key = []
        for i in range(64):
            if cipher_text_64_bit[i] == d_key_64_bit[i]:
                XOR_CT_Key.append(0)
            else:
                XOR_CT_Key.append(1)

        XOR_CTxKey_IV = []
        for i in range(64):
            if XOR_CT_Key[i] == IV_64_bit[i]:
                XOR_CTxKey_IV.append(0)
            else:
                XOR_CTxKey_IV.append(1)

        IV_64_bit = cipher_text_64_bit

        PT_8X8 = []
        count = 0
        for i in range(8):
            temp = ""
            for j in range(8):
                temp += str(XOR_CTxKey_IV[count])
                count += 1
            PT_8X8.append(chr(int(temp, 2)))

        for i in PT_8X8:
            decrypted_text += i

    displayPlainText(decrypted_text)


def label1(ch):
    ## labels
    #   -> opening and closing of labels
    label_frames[0] = 1
    if label_frames[1] == 1:
        fr.destroy()
        label_frames[1] = 0

    global fr1
    fr1 = Frame(root, height=235, width=707)
    fr1.place(x=10, y=60)

    # Encryption side
    l1 = Label(fr1, text="ENCRYPTION", font=('Helvertica', 15))
    l1.place(x=50, y=10, anchor=W)
    l2 = Label(fr1, text="PLAIN TEXT")
    l2.place(x=15, y=40, anchor=W)
    l3 = Label(fr1, text="ENTER KEY")
    l3.place(x=15, y=70, anchor=W)
    l4 = Label(fr1, text="CIPHER TEXT")
    l4.place(x=445, y=55, anchor=W)

    # Decryption side
    l5 = Label(fr1, text="DECRYPTION", font=('Helvertica', 15))
    l5.place(x=60, y=130, anchor=W)
    l6 = Label(fr1, text="CIPHER TEXT")
    l6.place(x=10, y=160, anchor=W)
    l7 = Label(fr1, text="ENTER KEY")
    l7.place(x=15, y=190, anchor=W)
    l8 = Label(fr1, text=""" DECRYPTED
PLAIN TEXT""")
    l8.place(x=480, y=175, anchor=CENTER)

    # send mails
    send1 = Button(fr1, text=">>", command=Email.sendEncryptedMail)
    send1.place(x=265, y=10, anchor=W)

    ## taking entries
    # encryption side
    global plain_text
    plain_text = Entry(fr1)
    plain_text.place(x=85, y=40, anchor=W)

    global e_key
    e_key = Entry(fr1)
    e_key.place(x=147, y=70, anchor=CENTER)

    # decryption side
    global encrypted_cipher_text
    encrypted_cipher_text = Entry(fr1)
    encrypted_cipher_text.place(x=85, y=160, anchor=W)

    global d_key
    d_key = Entry(fr1)
    d_key.place(x=147, y=190, anchor=CENTER)

    ## buttons
    if ch == "Caesar cipher":
        button1 = Button(fr1, text="ENCRYPT", command=caesarCipher)
        button1.place(x=265, y=55, anchor=CENTER)

        button4 = Button(fr1, text="DECRYPT", command=caesar_cipher_decryption)
        button4.place(x=335, y=175, anchor=CENTER)

    elif ch == "Vernam cipher":
        button1 = Button(fr1, text="ENCRYPT", command=vernam_cipher)
        button1.place(x=265, y=55, anchor=CENTER)

        button4 = Button(fr1, text="DECRYPT", command=vernam_cipher_decryption)
        button4.place(x=335, y=175, anchor=CENTER)

    elif ch == "Play-fair cipher":
        button1 = Button(fr1, text="ENCRYPT", command=playfair_cipher)
        button1.place(x=265, y=55, anchor=CENTER)

        button4 = Button(fr1, text="DECRYPT", command=playfair_cipher_decryption)
        button4.place(x=335, y=175, anchor=CENTER)

    elif ch == "ECB mode cipher":
        button1 = Button(fr1, text="ENCRYPT", command=ECB_mode)
        button1.place(x=265, y=55, anchor=CENTER)

        button4 = Button(fr1, text="DECRYPT", command=ECB_mode_decryption)
        button4.place(x=335, y=175, anchor=CENTER)

    elif ch == "CBC mode":
        button1 = Button(fr1, text="ENCRYPT", command=CBC_mode)
        button1.place(x=265, y=55, anchor=CENTER)

        button4 = Button(fr1, text="DECRYPT", command=CBC_mode_decryption)
        button4.place(x=335, y=175, anchor=CENTER)

    button2 = Button(root, text="COPY", command=copyValnKey)
    button2.place(x=260, y=235, anchor=CENTER)


def label2(ch):
    ## labels
    #   -> opening and closing of frames
    label_frames[1] = 1
    if label_frames[0] == 1:
        fr1.destroy()
        label_frames[0] = 0

    global fr
    fr = Frame(root, height=233, width=707)
    fr.place(x=10, y=60)

    # Encryption side

    l1 = Label(fr, text="ENCRYPTION", font=('Helvetica', 15))
    l1.place(x=40, y=20, anchor=W)
    l2 = Label(fr, text="PLAIN TEXT")
    l2.place(x=10, y=60, anchor=W)
    l4 = Label(fr, text="CIPHER TEXT")
    l4.place(x=450, y=60, anchor=W)

    # Decryption side
    l5 = Label(fr, text="DECRYPTION", font=('Helvetica', 15))
    l5.place(x=40, y=120, anchor=W)
    l6 = Label(fr, text="CIPHER TEXT")
    l6.place(x=6, y=160, anchor=W)
    l7 = Label(fr, text="RANDOM KEY")
    l7.place(x=2, y=190, anchor=W)
    l8 = Label(fr, text=""" DECRYPTED
PLAIN TEXT""")
    l8.place(x=470, y=175, anchor=CENTER)

    ## taking entries
    # encryption side
    global plain_text
    plain_text = Entry(fr)
    plain_text.place(x=90, y=60, anchor=W)

    # decryption side
    global encrypted_cipher_text
    encrypted_cipher_text = Entry(fr)
    encrypted_cipher_text.place(x=90, y=160, anchor=W)

    global d_key
    d_key = Entry(fr)
    d_key.place(x=152, y=190, anchor=CENTER)

    ## buttons
    if ch == "Hill cipher":
        button1 = Button(fr, text="OK", command=hillCipher)
        button1.place(x=255, y=60, anchor=CENTER)

        button4 = Button(fr, text="PROCEED", command=hill_cipher_decryption)
        button4.place(x=335, y=175, anchor=CENTER)

    elif ch == "RSA algorithm":
        button1 = Button(fr, text="OK", command=RSA_algorithm)
        button1.place(x=255, y=60, anchor=CENTER)

        button4 = Button(fr, text="PROCEED", command=RSA_algorithm_decryption)
        button4.place(x=335, y=175, anchor=CENTER)

    button2 = Button(fr, text="COPY", command=copyValnKey)
    button2.place(x=255, y=175, anchor=CENTER)


def caesarLink():
    link = "www.wikipedia.org/wiki/Caesar_cipher"
    webbrowser.open_new_tab(link)


def hillLink():
    link = "www.geeksforgeeks.org/hill-cipher/"
    webbrowser.open_new_tab(link)


def vernamLink():
    link = "www.geeksforgeeks.org/vernam-cipher-in-cryptography/"
    webbrowser.open_new_tab(link)


def playFairLink():
    link = "www.geeksforgeeks.org/playfair-cipher-with-examples/"
    webbrowser.open_new_tab(link)


def ECB_link():
    link = "www.geeksforgeeks.org/block-cipher-modes-of-operation/"
    webbrowser.open_new_tab(link)


def CBC_link():
    link = "https://searchsecurity.techtarget.com/definition/cipher-block-chaining#:~:text=Cipher%20block%20chaining%20(CBC)%20is,applied%20to%20the%20entire%20block).&text=A%20single%20bit%20error%20in,decryption%20of%20all%20subsequent%20blocks."
    webbrowser.open_new_tab(link)


def RSALink():
    link = "www.geeksforgeeks.org/rsa-algorithm-cryptography/"
    webbrowser.open_new_tab(link)


def print_label(chosen):
    hyperlink = tkHyperlinkManager.HyperlinkManager(T)
    if chosen == "Caesar cipher":
        processNrules = "The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places down the alphabet.\n"
        T.insert(INSERT, processNrules, 'tag_center')
        T.insert(END, "www.wikipedia.org/wiki/Caesar_cipher", hyperlink.add(caesarLink))
        T.tag_configure('big', font=('Verdana', 12, 'bold'))
        T.insert(END, '\n\nRULES', 'big')
        processNrules = "\n1. Please enter the plain text in lowercase.\n2. Please enter the key in numeric form(number).\n3. Plain text must contain characters only between 'a-z'\n"
        T.insert(END, processNrules)

    elif chosen == "Vernam cipher":
        processNrules = "Vernam Cipher is a method of encrypting alphabetic text. It is simply a type of substitution cipher. In this mechanism we assign a number to each character of the Plain-Text, like (a = 0, b = 1, c = 2, … z = 25).\n"
        T.insert(END, processNrules, 'tag_center')
        T.insert(INSERT, "vernam-cipher-in-cryptography", hyperlink.add(vernamLink))
        T.tag_configure('big', font=('Verdana', 12, 'bold'))
        T.insert(END, '\n\nMethod to take key:', 'big')
        processNrules = "\nIn Vernam cipher algorithm, we take a key to encrypt the plain text which length should be equal to the length of the plain text."
        T.insert(END, processNrules)
        T.tag_configure('big', font=('Verdana', 12, 'bold'))
        T.insert(END, '\n\nEncryption Algorithm:', 'big')
        processNrules = "\n1.Assign a number to each character of the plain-text and the key according to alphabetical order.\n2. Add both the number (Corresponding plain-text character number and Key character number).\n3. Subtract the number from 26 if the added number is greater than 26, if it isn’t then leave it.\n"
        T.insert(END, processNrules)
        T.insert(END, '\nExample:', 'big')
        T.tag_configure('small', font=('Verdana', 9, 'bold'))
        T.insert(END, '\n\nPlain text: ', 'small')
        T.insert(END, 'WELCOME\n')
        T.insert(END, 'Key used: ', 'small')
        T.insert(END, 'ANY KEYS\t(note: length of plain-text and key are same)')
        T.insert(END, '\n\n  W     E      L     C     O      M     E', 'small')
        T.insert(END, '\n 22  4   11  2  14   12  4\n +   +   +   +   +   +   +\n')
        T.insert(END, '  A     N      Y      K      E     Y      S', 'small')
        T.insert(END,
                 '\n 0  13   24  10  4  24  18\n ↓   ↓   ↓   ↓   ↓   ↓   ↓\n 22  17  35  12  18  26  22\n        -26         -26\n ↓   ↓   ↓   ↓   ↓   ↓   ↓\n 22  17  9  12  18  10  21\n')
        T.insert(END, '  W     R     J     M     S      K     W', 'small')
        T.insert(END, '\n\nHence encrypted text is: \n')
        T.insert(END, '"WRJMSKW"')

    elif chosen == "Play-fair cipher":
        processNrules = "The technique encrypts pairs of letters (bigrams or digrams), instead of single letters as in the simple substitution cipher.\n\n"
        T.insert(END, processNrules, 'tag_center')
        T.insert(INSERT, "www.geeksforgeeks.org/playfair-cipher-with-examples/", hyperlink.add(playFairLink))
        T.tag_configure('big', font=('Verdana', 12, 'bold'), underline=1)
        T.insert(END, '\n\nEncryption Algorithm:', 'big')
        T.tag_configure('big1', font=('Verdana', 10, 'bold'))
        T.insert(END, '\n\n\tExample:', 'big1')
        T.insert(END, '\nPlain text: ', 'big1')
        T.insert(END, 'instruments', 'tag_center')
        T.insert(END, '\nKey: ', 'big1')
        T.insert(END, 'monarchy', 'tag_center')
        T.insert(END, '\n\nGenerate the key Square(5×5):', 'big1')
        processNrules = """\n• The key square is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext. Each of the 25 alphabets must be unique and one letter of the alphabet (usually J) is omitted from the table (as the table can hold only 25 alphabets). If the plaintext contains J, then it is replaced by I.\n
• The initial alphabets in the key square are the unique alphabets of the key in the order in which they appear followed by the remaining letters of the alphabet in order.\n\n"""
        T.insert(END, processNrules, 'tag_center')
        T.insert(END,
                 '_____________________\n| m | o | n | a | r |\n| c | h | y | b | d |\n| e | f | g | i | k |\n| l | p | q | s | t |\n| u | v | w | x | z |\n---------------------\n',
                 'tag_center')
        T.insert(END, '\nAlgorithm to encrypt plain text: ', 'big1')
        T.insert(END,
                 '\n• The plaintext is split into pairs of two letters (digraphs). If there is an odd number of letters, a "z" is added to the last letter.\n',
                 'tag_center')
        T.tag_configure('big2', font=('Verdana', 8, 'bold'))
        T.insert(END, '\nPlain text: ', 'big2')
        T.insert(END, '"instruments"', 'tag_center')
        T.insert(END, '\nAfter split: ', 'big2')
        T.insert(END, '"in" "st" "ru" "me" "nt" "sz"', 'tag_center')
        T.insert(END, '\n\nRules for encryption', 'big1')
        T.insert(END, '\n • If both the letters are in same column: ', 'big2')
        T.insert(END, 'Take the letter below each one (going back to the top if at the bottom).', 'tag_center')
        T.insert(END, '\n • If both the letters are in same row: ', 'big2')
        T.insert(END,
                 'Take the letter to the right of each one (going back to the leftmost if at the rightmost position).',
                 'tag_center')
        T.insert(END, '\n • If neither of the above rules is true: ', 'big2')
        T.insert(END,
                 'Form a rectangle with the two letters and take the letters on the horizontal opposite corner of the rectangle.',
                 'tag_center')
        T.insert(END, '\n\nCipher text', 'big1')
        T.insert(END,
                 '\n"in" -> "ga" (using case 3)\n"st" -> "tl" (using case 2)\n"ru" -> "mz" (using case 3)\n"me" -> "cl" (using case 1)\n"nt" -> "rq" (using case 1)\n"sz" -> "tx" (using case 3)\n\nHence CIPHER TEXT: \n')
        T.insert(END, '"gatlmzclrqtx"\n', 'big2')

    elif chosen == "ECB mode cipher":
        T.insert(END,
                 'The simplest of the encryption modes is the electronic codebook (ECB) mode (named after conventional physical codebooks). The message is divided into blocks, and each block is encrypted separately.\n',
                 'tag_center')
        T.tag_configure('small', font=('Verdana', 8, 'bold'))
        T.tag_configure('medium', font=('Verdana', 10, 'bold'))
        T.tag_configure('large', font=('Verdana', 12, 'bold'))
        T.insert(END, '\ngeeksforgeeks.org/block-cipher-modes-of-operation/', hyperlink.add(ECB_link))
        T.insert(END, '\n\nDISADVANTAGE: ', 'small')
        T.insert(END,
                 'The disadvantage of this method is a lack of diffusion. Because ECB encrypts identical plaintext blocks into identical ciphertext blocks, it does not hide data patterns well. ECB is not recommended for use in cryptographic protocols.\n',
                 'tag_center')

    elif chosen == "CBC mode":
        T.tag_configure('small', font=('Verdana', 8, 'bold'))
        T.tag_configure('medium', font=('Verdana', 10, 'bold'))
        T.tag_configure('large', font=('Verdana', 12, 'bold'))
        T.insert(END, "Cipher block chaining (CBC) ", 'small')
        T.insert(END,
                 "is a mode of operation for a block cipher (one in which a sequence of bits are encrypted as a single unit or block with a cipher key applied to the entire block).\n1. Cipher block chaining uses what is known as an ",
                 'tag_center')
        T.insert(END, "Initialization Vector (IV)", 'small')
        T.insert(END,
                 " of a certain length.\n2. One of its key characteristics is that it uses a chaining mechanism that causes the decryption of a block of ciphertext to depend on all the preceding ciphertext blocks. As a result, the entire validity of all preceding blocks is contained in the immediately previous ciphertext block.\n3. A single bit error in a ciphertext block affects the decryption of all subsequent blocks.\n4. Rearrangement of the order of the ciphertext blocks causes decryption to become corrupted.",
                 'tag_center')
        T.insert(END,
                 "Basically, in cipher block chaining, each plaintext block is XORed (see XOR) with the immediately previous ciphertext block, and then encrypted.",
                 'tag_configure')
        T.insert(END, '\n\nknow more about CIPHER BLOCK CHAINING MODE\n', hyperlink.add(CBC_link))

    elif chosen == "Hill cipher":
        T.tag_configure('small', font=('Verdana', 8, 'bold'))
        T.tag_configure('medium', font=('Verdana', 10, 'bold'))
        T.tag_configure('large', font=('Verdana', 12, 'bold'))
        T.insert(END, "HILL CIPHER ", 'medium')
        T.insert(END,
                 "is a polygraphic substitution cipher based on linear algebra. Each letter is represented by a number modulo 26. Often the simple scheme A = 0, B = 1, …, Z = 25 is used.\n",
                 'tag_center')
        T.insert(END, '\nknow more about HILL CIPHER\n', hyperlink.add(hillLink))
        T.insert(END, "\n======RULES=======", 'large')
        T.insert(END,
                 "\n\n1. Use ONLY alphabets and spaces as plain text.\n2. KEY is automatically generated- DO NOT change the KEY during DECRYPTION.\n",
                 'tag_center')

    elif chosen == "RSA algorithm":
        T.tag_configure('small', font=('Verdana', 8, 'bold'))
        T.tag_configure('medium', font=('Verdana', 10, 'bold'))
        T.tag_configure('large', font=('Verdana', 12, 'bold'))
        T.insert(END, "RSA algorithm ", 'medium')
        T.insert(END, "(Rivest– Shamir– Adleman) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. ", 'tag_center')
        T.insert(END, "In a ", 'tag_center')
        T.insert(END, "public-key ", 'medium')
        T.insert(END, "cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). ", 'tag_center')
        T.insert(END, "An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. ", 'tag_center')
        T.insert(END, "The prime numbers are kept secret. Messages can be encrypted by anyone, via the public key, but can only be decoded by someone who knows the prime numbers.\n\n", 'tag_center')
        T.insert(END, "Know more about RSA algorithm\n\n", hyperlink.add(RSALink))
        T.insert(END, "RSA is a relatively slow algorithm. Because of this, it is not commonly used to directly encrypt user data. More often, RSA is used to transmit shared keys for symmetric key cryptography, which are then used for bulk encryption-decryption.", 'tag_center')


def chosed_technique():
    array.clear()
    if displayController[0] == 1:
        displayController[0] = 0
        cipherDisplay.destroy()
        download1.destroy()
    if displayController[1] == 1:
        displayController[1] = 0
        plainDisplay.destroy()
        download2.destroy()

    if destroyFrameArr[2] == 1:
        destroy()
    chosen = variable.get()
    T.delete('1.0', END)
    print_label(chosen)
    if chosen == "Caesar cipher" or chosen == "Vernam cipher" or chosen == "Play-fair cipher" or chosen == "ECB mode cipher" or chosen == "CBC mode":
        array.clear()
        decryption_array.clear()
        label1(chosen)
    elif chosen == "Hill cipher" or chosen == "RSA algorithm":
        array.clear()
        decryption_array.clear()
        label2(chosen)


array = []
decryption_array = []
global tech
global historyDisplay
wHis = writeHistory()
myDb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="cryptographicTechniques")
mycursor = myDb.cursor()

if __name__ == '__main__':
    global root
    root = tk.ThemedTk()
    root.set_theme("itft1")

    root.title("Cryptographic Techniques")
    root.geometry("1000x300")
    root.resizable(False, False)

    fr2 = Frame(root, height=50, width=615)
    fr2.place(x=101, y=5)

    techniques = ["Choose", "Caesar cipher", "Hill cipher", "Vernam cipher", "Play-fair cipher", "ECB mode cipher",
                  "CBC mode",
                  "RSA algorithm"]
    variable = StringVar(root)
    variable.set(techniques[0])
    w = OptionMenu(fr2, variable, *techniques)
    w.place(x=295, y=20, anchor=CENTER)

    global displayController
    displayController = [0, 0]

    button0 = Button(fr2, text="PROCEED", command=chosed_technique)
    button0.place(x=410, y=20, anchor=CENTER)

    photo = PhotoImage(file="img//line.png")
    panel = Label(root, image=photo)
    panel.place(x=720, y=10)

    # Scrollbar and text widget on the right hand of the screen
    global S
    global T
    S = Scrollbar(root)
    T = Text(root, wrap=WORD, height=16, width=29)
    S.pack(side=RIGHT, fill=Y)
    T.place(x=730, y=20)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.tag_configure('tag_center', justify='left')

    global count
    count = 0

    # creating tkinter window
    destroyFrameArr = [0, 0, 0]  # used for taking tracks of frames(i.e. open or close)
    label_frames = [0, 0]

    # Creating a photoimage object to use image
    photo1 = PhotoImage(file="img//settings.png")
    photo2 = PhotoImage(file="img//themes.png")
    photo4 = PhotoImage(file="img//history.png")
    pic2 = photo2

    settingsButton = Button(root, image=photo1, command=showAll)
    settingsButton.place(x=20, y=10)

    mainloop()
