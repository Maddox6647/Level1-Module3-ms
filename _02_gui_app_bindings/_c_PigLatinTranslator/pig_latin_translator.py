"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize an Entry (tk.Entry) for the input text
        self.input_entry = tk.Entry(self, width=40)
        self.input_entry.pack(pady=10)
        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed.
        self.translate_button = tk.Button(
            self,
            text="Translate",
            command=self.on_key_press
        )
        self.translate_button.pack(pady=5)
        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text
        self.output_label = tk.Label(self, text="", width=40)
        self.output_label.pack(pady=10)


        # TODO: Look at the example image () and place all the
        #  components in the same order
        self.input_entry.pack(pady=10)
        self.translate_button.pack(pady=5)
        self.output_label.pack(pady=10)
        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released
        self.input_entry.bind("<KeyRelease>", self.on_key_press)


    def on_key_press(self, event):
        print('button pressed!')

        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry
        text = self.input_entry.get()
        translated = PigLatinConverter.translate(text)
        self.output_label.config(text=translated)

if __name__ == '__main__':
    pass
    # TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
    #  Remember to call mainloop() at the end
    app = PigLatinTranslator()
    app.title("Pig Latin Translator")
    app.geometry("400x200")
    app.mainloop()
