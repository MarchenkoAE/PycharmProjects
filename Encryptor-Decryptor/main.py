from tkinter import *
from tkinter import messagebox as mb


class Application():
    def __init__(self):
        self.window = Tk()
        self.window.title('Encryptor-Decryptor')
        self.window.geometry("350x350+10+20")
        self.text_input = StringVar()
        self.key_input = StringVar()
        self.init_window()
        self.window.mainloop()

    def init_window(self):
        self.window.btn1 = Button(self.window, text="Decrypt", command=self.decrypt)
        self.window.btn1.place(x=175, y=300)
        self.window.btn2 = Button(self.window, text="Encrypt", command=self.encrypt)
        self.window.btn2.place(x=100, y=300)
        self.window.txtfld1 = Entry(self.window, textvariable=self.text_input, bg='black', fg='white', bd=10)
        self.window.txtfld1.place(x=100, y=100)
        self.window.txtfld2 = Entry(self.window, textvariable=self.key_input, bg='black', fg='white', bd=10)
        self.window.txtfld2.place(x=100, y=200)
        self.window.title1 = Label(self.window, text="text")
        self.window.title1.place(x=150, y=50)
        self.window.title2 = Label(self.window, text="key")
        self.window.title2.place(x=150, y=150)

    def encrypt(self):
        result = ""
        encrypt = self.text_input.get()
        key = self.key_input.get()
        total_1 = {}
        total_2 = {}
        for i in encrypt:
            new_i = (ord(i) + ord(key[ord(i) % len(key)]))%65536
            total_1[chr(ord(i))] = ord(str(i))
            total_2[chr(new_i)] = new_i
        for j in total_2:
            result = result + j
        answer = mb.askyesno("Encryption results",
                             result)
        if answer:
            my_file = open("Encrypt.txt", "w+")
            my_file.write(encrypt + " " + result)
            my_file.close()

    def decrypt(self):
        result = ""
        decrypt = self.text_input.get()
        key = self.key_input.get()
        total_1 = {}
        total_2 = {}
        for i in decrypt:
            new_i = (ord(i) - ord(key[ord(i) % len(key)]))%65536
            total_1[chr(ord(i))] = ord(str(i))
            total_2[chr(new_i)] = new_i
        for j in total_2:
            result = result + j
        answer = mb.askyesno("Decryption results",
                             result)
        if answer:
            my_file = open("Decrypt.txt", "w+")
            my_file.write(decrypt + " " + result)
            my_file.close()


if __name__ == '__main__':
    app = Application()
