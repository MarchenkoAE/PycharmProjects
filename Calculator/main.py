from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox


class Application():
    def __init__(self):
        self.window = Tk()
        self.window.title('Calculator')
        self.window.geometry("350x350+10+20")
        self.var1_input = StringVar()
        self.var2_input = StringVar()
        self.operation = StringVar()
        self.init_window()
        self.window.mainloop()

    def init_window(self):
        self.window.btn1 = Button(self.window, text="Calculate", command=self.calculate)
        self.window.btn1.place(x=150, y=300)
        self.window.txtfld1 = Entry(self.window, textvariable=self.var1_input, bg='black', fg='white', bd=10)
        self.window.txtfld1.place(x=20, y=150)
        self.window.txtfld2 = Entry(self.window, textvariable=self.var2_input, bg='black', fg='white', bd=10)
        self.window.txtfld2.place(x=170, y=150)
        self.window.title1 = Label(self.window, text="1st variable")
        self.window.title1.place(x=20, y=100)
        self.window.title2 = Label(self.window, text="2nd variable")
        self.window.title2.place(x=170, y=100)
        self.window.title2 = Label(self.window, text="operation")
        self.window.title2.place(x=20, y=200)
        self.window.combobox1 = Combobox(self.window, textvariable=self.operation,
                                         values=["+", "-", "/", "*"]).grid(column=0, row=1, padx=20, pady=250)

    def calculate(self):
        var1 = int(self.var1_input.get())
        var2 = int(self.var2_input.get())
        operation = self.operation.get()
        result = 0
        if (operation == "+"):
            result = var1 + var2
        if (operation == "-"):
            result = var1 - var2
        if (operation == "/"):
            result = var1 // var2
        if (operation == "*"):
            result = var1 * var2
        bin_ = str(bin(result))
        oct_ = str(oct(result))
        hex_ = str(hex(result))
        mb.showinfo("Result",
                        str(result) + " " +bin_ +" "  + oct_ + " " + hex_)


if __name__ == '__main__':
    app = Application()
