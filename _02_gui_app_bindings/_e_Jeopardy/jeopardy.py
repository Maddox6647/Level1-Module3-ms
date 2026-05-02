"""
 Create a _e_Jeopardy trivia game!
"""
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk


class Jeopardy(tk.Tk):

    def __init__(self, categories):
        super().__init__()

        button_width, button_height, num_buttons = self.setup_buttons(categories)

        # TODO: Create a member variable for the list of categories
        self.categories = categories
        # TODO: Create a member variable for the score/money
        self.score = 0
        self.score_label = tk.Label(self, text="Score: $0", font=("Arial", 16))
        self.score_label.pack(side="")
        for i in range(num_buttons):
            row_num = int(i / len(categories))
            col_num = int(i % len(categories))
            row_y = row_num * button_height
            col_x = col_num * button_width
            category = self.categories[col_num]

            # Create the category header and buttons where
            # row 0 is the category title
            if row_num == 0:

                # TODO: To get the category name, use the categories member variable and column num
                label = tk.Label(self, text=category.name, bg="blue", fg="white")
                # TODO: Place the Label using the 'col_x', 'row_y', 'button_width',
                #  and 'button_height' variables
                label.place(x=col_x, y=row_y, width=button_width, height=button_height)
            elif len(category.questions) > row_num - 1:
                question_obj = category.questions[row_num - 1]

                # TODO: Create a tk.Button with the questions' value on the button
                button = tk.Button(self, text=f"${question_obj.value}")
                button.question = question_obj
                # TODO: Place the Button using the 'col_x', 'row_y', 'button_width',
                #  and 'button_height' variables
                button.place(x=col_x, y=row_y, width=button_width, height=button_height)
                # TODO: Call the button's bind() method so the
                #  on_button_press() method is called when a mouse button is pressed
                #  example: self.joke_button.bind('<ButtonPress>', self.on_button_press)
                button.bind('<ButtonPress>', self.on_button_press)
                # TODO: Add the button to the category's list of buttons
                category.buttons.append(button)

    def on_button_press(self, event):
        button_pressed = event.widget
        print('button ' + repr(button_pressed) + ' clicked!')
        # TODO: Call the ask_question() method with button_pressed as an input
        self.ask_question(button_pressed)
    def ask_question(self, button_pressed):


                        # TODO: At this point the question corresponding to the button is found
                        #  Use the 'question', 'answer', and 'value' variables to ask the user
                        #  the question and get their response. If their response is correct,
                        #  increase the score member variable by the value. Otherwise, subtract
                        #  value from the score

        if not hasattr(button_pressed, "question"):
            return
        question_obj = button_pressed.question


        question_obj.has_been_asked = True

        user_answer = simpledialog.askstring(
            "Question",
            question_obj.question
        )

        if user_answer is None:
            return

        if user_answer.strip().lower() == question_obj.answer.lower():
            self.score += question_obj.value
            messagebox.showinfo("Correct!", f"+${question_obj.value}")
        else:
            self.score -= question_obj.value
            messagebox.showerror(
                "Incorrect",
                f"Correct answer: {question_obj.answer}\n-${question_obj.value}"
            )

        button_pressed.config(state="disabled", text="---")

        self.score_label.config(text=f"Score: ${self.score}")

    def setup_buttons(self, categories):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('800x600')
        self.update_idletasks()

        # Get category with the max num of questions to determine the
        # total number of buttons to create
        questions_per_category = 0
        for category in categories:
            if len(category.questions) > questions_per_category:
                questions_per_category = len(category.questions)

        # +1 for the category title
        num_rows = questions_per_category + 1
        num_buttons = len(categories) * num_rows

        button_width = int(self.winfo_width() / len(categories))
        button_height = int(self.winfo_height() / num_rows)

        return button_width, button_height, num_buttons


class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.questions = list()
        self.buttons = list()

    def add_question(self, question, answer, value):
        new_question = Category.Question(question, answer, value)
        self.questions.append(new_question)

    class Question:
        def __init__(self, question, answer, value):
            self.has_been_asked = False
            self.question = question
            self.answer = answer
            self.value = value


if __name__ == '__main__':
    j_categories = list()

    # TODO: Use the Category class above to create at least 3 question categories
    #  for your _e_Jeopardy game
    math_category = Category("Math")
    math_category.add_question("What is 2 + 2?", "4", 100)
    math_category.add_question("What is 5 * 6?", "30", 200)
    math_category.add_question("What is 12 / 3?", "4", 300)

    # Category 2
    science_category = Category("Science")
    science_category.add_question("What planet is known as the Red Planet?", "Mars", 100)
    science_category.add_question("What gas do plants breathe in?", "Carbon dioxide", 200)
    science_category.add_question("What is H2O?", "Water", 300)

    # Category 3
    history_category = Category("History")
    history_category.add_question("Who was the first president of the USA?", "George Washington", 100)
    history_category.add_question("What year did WW2 end?", "1945", 200)
    history_category.add_question("What empire built the Colosseum?", "Roman", 300)

    j_categories.extend([math_category, science_category, history_category])
    # TODO: For each Category, use  the add_question method to add a question, answer, and
    #  a value for each question

    game = Jeopardy(j_categories)
    game.title('_e_Jeopardy')
    game.mainloop()
