

## 📝 Spell Checker Tool

A simple **Spell Checker and Text Correction** web application developed using **Python**, **Streamlit**, **NLTK**, and **TextBlob**. The application helps users identify spelling mistakes, receive word suggestions, correct complete sentences, and experiment with text correction through an easy-to-use web interface.

---

# 📌 Project Overview

The Spell Checker Tool is a Natural Language Processing (NLP) application that automatically detects spelling mistakes and suggests corrected words. It also provides complete sentence correction using the TextBlob library. The application includes an interface where users can enter individual words, complete sentences, or upload files for testing.

This project demonstrates how NLP techniques can be integrated into a Streamlit web application to improve text quality.

---

# ✨ Features

* 🔤 Single word spell checking
* ✍️ Complete sentence correction
* 📄 CSV file upload support
* ⚡ Instant correction results
* 🖥 Interactive Streamlit interface
* 📚 NLP-based text processing

---

# 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NLTK
* TextBlob

---

# 📂 Project Structure

```text
Spell-Checker-Tool/
│── app.py
│── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Spell-Checker-Tool.git
```

Move into the project folder:

```bash
cd Spell-Checker-Tool
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Download the required NLP resources:

```python
import nltk
nltk.download('punkt')
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

After running the command, Streamlit will open the application in your default web browser.

---

# 📖 How It Works

1. Enter a single word.
2. The application suggests the most likely correct spelling.
3. Enter a complete sentence.
4. TextBlob analyzes the sentence and automatically corrects spelling mistakes.
5. Users can also upload a CSV file to test text correction functionality.

---

# 📦 Required Files

* app.py
* requirements.txt
* README.md

---

# 🚀 Future Improvements

* DOCX file correction support
* PDF text extraction
* Grammar checking
* Multiple language support
* Download corrected text
* Better user interface
* AI-powered spell suggestions

---

# 📸 Output

The application displays:

* Suggested spelling for a word
* Corrected sentence
* Corrected text from uploaded content

---

# 👨‍💻 Author

Developed using **Python**, **Natural Language Processing (NLP)**, **TextBlob**, and **Streamlit** for educational and learning purposes.

---

# 📄 License

This project is released under the MIT License. Feel free to use, modify, and improve it for educational or personal projects.
