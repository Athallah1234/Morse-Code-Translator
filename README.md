# Morse Code Translator

## Description

Morse Code Translator is a simple Python application built using the Tkinter library. It allows users to translate text to Morse code and vice versa. The application provides an intuitive graphical interface with features such as history tracking, clearing input/output, copying output to the clipboard, and more.

## Features

- **Text to Morse Code Translation**: Enter text in the input field and click "Translate" to get the corresponding Morse code.
- **Morse Code to Text Translation**: Enter Morse code in the input field and click "Translate Morse" to get the corresponding text.
- **History Tracking**: Keep track of your translations with a built-in history feature.
- **Clear Input/Output**: Clear the input or output fields with the "Clear Input" and "Clear Output" buttons.
- **Copy to Clipboard**: Copy the translated output to the clipboard using the "Copy Output" button.

## Usage

1. Enter the text you want to translate into Morse code in the "Enter Text" field.
2. Click the "Translate" button to see the Morse code in the "Morse Code" field.
3. Enter Morse code in the "Enter Morse Code" field.
4. Click the "Translate Morse" button to see the corresponding text in the "Text" field.
5. Use the "Clear Input" and "Clear Output" buttons to reset input and output fields.
6. Copy the translated output to the clipboard using the "Copy Output" button.

## Getting Started

1. Ensure you have Python installed on your machine.
2. Clone the repository: `git clone https://github.com/Athallah1234/Morse-Code-Translator.git`
3. Navigate to the project directory: `cd morse-code-translator`
4. Install required dependencies: `pip install -r requirements.txt`
5. Run the application: `python morse_code_translator.py`

## Dependencies

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI (Graphical User Interface) package.
- [Pyperclip](https://pypi.org/project/pyperclip/) - A cross-platform clipboard module for Python.

## Contributing

We welcome contributions! If you find any issues or have suggestions for improvements, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes: `git checkout -b feature/your-feature` or `git checkout -b bugfix/your-bugfix`.
4. Make your changes and commit them: `git commit -m 'Your descriptive commit message'`.
5. Push your changes to your fork: `git push origin feature/your-feature`.
6. Open a pull request on the original repository.

## FAQ

### Q: How can I contribute to this project?
A: You can contribute by opening issues for bug reports or feature requests, or by creating pull requests with your enhancements.

### Q: Is there a limit to the length of text that can be translated?
A: There is no strict limit, but extremely long text may be truncated in the UI.

### Q: Can I use this code in my own project?
A: Yes, the project is licensed under the MIT License, allowing you to use and modify the code for your purposes.

### Q: How does the history feature work?
A: The history feature records each translation and displays it in the "History of Translations" section.

### Q: Is there a way to customize the Morse Code translation speed?
A: The application currently does not have a customizable speed feature. The translation is instantaneous upon clicking the "Translate" or "Translate Morse" button.

### Q: Can I contribute new features to the application?
A: Absolutely! We encourage contributions. Feel free to open an issue to discuss new features or directly submit a pull request with your enhancements.

### Q: How can I view the complete history of translations?
A: The history section displays the most recent translations. For a complete history, you may need to refer to the application logs or modify the code to store a more extensive history.

### Q: Does the application support international characters?
A: The current implementation primarily focuses on the standard Latin alphabet and Arabic numerals. While some international characters may be supported, full compatibility is not guaranteed.

## History

The project maintains a history of translations for user reference. You can view this history in the "History of Translations" section

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Morse Code Dictionary used in this project: {'A': '.-', 'B': '-...', ...}

## Author

[Athallah1234](https://github.com/Athallah1234)
