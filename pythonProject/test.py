import random
import string
import tkinter
from tkinter import messagebox


class KeyMB(tkinter.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Создание ключа")
        self.geometry("300x160")
        self.resizable(False, False)
        self.key = tkinter.StringVar()
        self.createInterface()
        self.grab_set()

    def keyButton(self):
        self.parent.key = self.key.get()
        self.destroy()

    def createInterface(self):
        self.label_text_crypto = tkinter.Label(self, text="Введите ключ, если хотите создать свой ключ")
        self.label_text_crypto.grid(row=0, column=0, padx=15, pady=15)

        self.entry_key = tkinter.Entry(self, textvariable=self.key)
        self.entry_key.grid(row=1, column=0, padx=15, pady=15)

        self.btn_key = tkinter.Button(self, text="OK", command=self.keyButton)
        self.btn_key.grid(row=2, column=0, padx=15, pady=15)


class CryptoApplication():
    def __init__(self):
        self.window = tkinter.Tk()

        self.window.resizable(False, False)  # MAkeBySAA
        self.window.title("Калькулятор")
        self.window.geometry("420x350")

        self.text_input_crypto = tkinter.StringVar()
        self.text_input_uncrypto = tkinter.StringVar()
        self.key_input = tkinter.StringVar()

        self.createInterface()

        self.max_unicode = 65536

        self.window.mainloop()

    def crypto(self):
        text = self.text_input_crypto.get()
        key = KeyMB(self.window)
        key.wait_window()
        key = key.key.get()
        if key == "":
            key = "".join(random.choice(string.digits) for _ in range(8))
        final_text = ""
        for i in range(len(text)):
            final_text += chr((ord(text[i]) + ord(key[i % len(key)])) % self.max_unicode)
        print(final_text)
        print(f"Key: {key}")

        answer = messagebox.askyesno("Зашифрованный текст",
                                     f"Зашифрованный текст: \n{final_text}\n"
                                     f"Ключ: {key}. Сохранить результат в файл?")
        if answer:
            with open("result.txt", "w", encoding="utf-8") as file:
                file.write(final_text)

    def uncrypto(self):
        text = self.text_input_uncrypto.get()
        key = self.key_input.get()
        if key == "":
            final_text = text
        else:
            final_text = ""
            for i in range(len(text)):
                final_text += chr((ord(text[i]) - ord(key[i % len(key)])) % self.max_unicode)
        print(final_text)
        answer = messagebox.askyesno("Расшифрованный текст",
                                     f"Расшифрованный текст: \n{final_text}\n"
                                     f"Сохранить результат в файл?")
        if answer:
            with open("result.txt", "w", encoding="utf-8") as file:
                file.write(final_text)

    def createInterface(self):
        tkinter.Label(self.window, text="Введите текст для шифрования").grid(column=0, row=0, padx=10, pady=10)
        tkinter.Entry(self.window, textvariable=self.text_input_crypto).grid(column=0, row=1, padx=15, pady=15)
        tkinter.Button(self.window, text="Шифровать", command=self.crypto).grid(column=0, row=2, padx=15, pady=15)
        tkinter.Label(self.window, text="Введите текст для дешифрования").grid(column=1, row=0, padx=10, pady=10)
        tkinter.Entry(self.window, textvariable=self.text_input_uncrypto).grid(column=1, row=1, padx=15, pady=15)
        tkinter.Label(self.window, text="Введите ключ").grid(column=1, row=2, padx=10, pady=10)
        tkinter.Entry(self.window, textvariable=self.key_input).grid(column=1, row=3, padx=15, pady=15)
        tkinter.Button(self.window, text="Дешифровать", command=self.uncrypto).grid(column=1, row=4, padx=15, pady=15)


if __name__ == "__main__":
    app = CryptoApplication()
