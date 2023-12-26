import tkinter as tk
from tkinter import ttk
import pyperclip

# Morse Code Dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'}


class MorseCodeTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")

        self.input_label = ttk.Label(root, text="Enter Text:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.input_entry = ttk.Entry(root, width=30)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.output_label = ttk.Label(root, text="Morse Code:")
        self.output_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.output_entry = ttk.Entry(root, width=30, state='readonly')
        self.output_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.morse_label = ttk.Label(root, text="Enter Morse Code:")
        self.morse_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.morse_entry = ttk.Entry(root, width=30)
        self.morse_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.text_label = ttk.Label(root, text="Text:")
        self.text_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.text_entry = ttk.Entry(root, width=30, state='readonly')
        self.text_entry.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

        self.translate_button_morse = ttk.Button(root, text="Translate Morse", command=self.translate_morse_code)
        self.translate_button_morse.grid(row=5, column=0, columnspan=2, pady=10)

        self.clear_input_button = ttk.Button(root, text="Clear Input", command=self.clear_input)
        self.clear_input_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.clear_output_button = ttk.Button(root, text="Clear Output", command=self.clear_output)
        self.clear_output_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.copy_output_button = ttk.Button(root, text="Copy Output", command=self.copy_output)
        self.copy_output_button.grid(row=8, column=0, columnspan=2, pady=10)

        # History feature
        self.history_label = ttk.Label(root, text="History of Translations:")
        self.history_label.grid(row=9, column=0, columnspan=2, pady=10)

        self.history_text = tk.Text(root, height=5, width=50, state='disabled')
        self.history_text.grid(row=10, column=0, columnspan=2, pady=10)

        self.history = []

    def translate_text(self):
        input_text = self.input_entry.get().upper()
        morse_code = self.text_to_morse_code(input_text)
        self.output_entry.config(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, morse_code)
        self.output_entry.config(state='readonly')

        # Add to history
        self.add_to_history(f'Text to Morse: {input_text} -> {morse_code}')

    def text_to_morse_code(self, text):
        morse_code = []
        for char in text:
            if char in MORSE_CODE_DICT:
                morse_code.append(MORSE_CODE_DICT[char])
            else:
                morse_code.append(' ')
        return ' '.join(morse_code)

    def translate_morse_code(self):
        morse_input = self.morse_entry.get()
        text = self.morse_code_to_text(morse_input)
        self.text_entry.config(state='normal')
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(0, text)
        self.text_entry.config(state='readonly')

        # Add to history
        self.add_to_history(f'Morse to Text: {morse_input} -> {text}')

    def morse_code_to_text(self, morse_code):
        morse_code_list = morse_code.split(' ')
        text = ''
        for code in morse_code_list:
            for key, value in MORSE_CODE_DICT.items():
                if code == value:
                    text += key
        return text

    def clear_input(self):
        self.input_entry.delete(0, tk.END)
        self.morse_entry.delete(0, tk.END)

    def clear_output(self):
        self.output_entry.config(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.config(state='readonly')

        self.text_entry.config(state='normal')
        self.text_entry.delete(0, tk.END)
        self.text_entry.config(state='readonly')

    def copy_output(self):
        output_text = self.output_entry.get()
        pyperclip.copy(output_text)

    def add_to_history(self, entry):
        self.history.append(entry)
        self.update_history_text()

    def update_history_text(self):
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        for entry in self.history:
            self.history_text.insert(tk.END, entry + '\n')
        self.history_text.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeTranslator(root)
    root.mainloop()

