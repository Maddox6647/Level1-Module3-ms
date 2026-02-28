"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random

from tkinter import messagebox


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        self.buttonjoke = tk.Button(self, text='joke', bg='red',  font=('Bitcount Grid Double', 20, 'normal'), command=self.on_joke)
        self.buttonpunchline = tk.Button(self, text= 'punchline', bg='green', font=('Bitcount Grid Double', 23, 'normal'), command=self.on_punchline)

        # TODO: Place the 2 buttons next to each other (see example image)
        self.buttonjoke.place(relx=0.1, rely=0.1)
        self.buttonpunchline.place(relx=0.6, rely=0.6)
        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        #  example: self.joke_button.bind('<ButtonPress>', self.on_joke)
        #self.buttonjoke.bind('<Button Press>', self.on_joke())
        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed

    def on_joke(self):
        print('Joke button pressed')
        messagebox.showinfo(title='shrek', message='Ur mom wants to kiss shrek')
        # TODO: Write your joke below!

    def on_punchline(self):
        print('Punchline button pressed')
        messagebox.showinfo(title='shrek', message='U like men')
        # TODO: Write a punchline to your joke!


if __name__ == '__main__':
    app = ChuckleClicker()
    app.title('Calculator')
    app.geometry('900x900')
    app.mainloop()
    # TODO: Create a new ChuckleClicker object and set the title and geometry.
    #  Remember to call mainloop() at the end

