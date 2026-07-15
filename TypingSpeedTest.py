import tkinter as tk

import time



text_to_type = "You are doing great, keep shining!."



class TypingApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Typing Speed Test")



        self.start_time = None



        # Show text

        self.label = tk.Label(root, text=text_to_type, font=("Arial", 14))

        self.label.pack(pady=20)



        # Entry box

        self.entry = tk.Entry(root, width=50, font=("Arial", 14))

        self.entry.pack(pady=10)

        self.entry.bind("<FocusIn>", self.start_timer)



        # Button

        self.button = tk.Button(root, text="Done", command=self.check_speed)

        self.button.pack(pady=10)



        # Result

        self.result = tk.Label(root, text="", font=("Arial", 12))

        self.result.pack(pady=20)



    def start_timer(self, event):

        if self.start_time is None:

            self.start_time = time.time()



    def check_speed(self):

        end_time = time.time()

        typed_text = self.entry.get()



        # Calculate WPM

        time_taken = (end_time - self.start_time) / 60  # minutes

        word_count = len(typed_text.split())

        wpm = word_count / time_taken if time_taken > 0 else 0



        self.result.config(text=f"Your speed: {wpm:.2f} WPM")



# Run app

root = tk.Tk()

app = TypingApp(root)

root.mainloop()