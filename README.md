 Toxic Comment Detector



 A Machine Learning project that classifies text comments as \*\*Toxic\*\* or \*\*Non-Toxic\*\* using \*\*Natural Language Processing (NLP)\*\* techniques with \*\*TF-IDF Vectorization\*\* and \*\*Logistic Regression\*\*.







 📖 Overview



Content moderation is an important challenge for online platforms. This project demonstrates a simple NLP pipeline that automatically classifies comments as \*\*Toxic\*\* or \*\*Non-Toxic\*\* using Machine Learning.



The model is trained on a sample dataset using \*\*TF-IDF Vectorization\*\* for feature extraction and \*\*Logistic Regression\*\* for classification. Users can interact with the model through an easy-to-use command-line interface.







 ✨ Features



 🔍 Detects toxic and non-toxic comments

🧠 TF-IDF text vectorization

 🤖 Logistic Regression classifier

 📊 Displays Accuracy and Classification Report

 💬 Interactive command-line prediction

 ⚡ Lightweight implementation for learning NLP fundamentals







 🛠️ Tech Stack



| Category | Technology |

|----------|------------|

| Language | Python |

| Machine Learning | Scikit-learn |

| Data Processing | Pandas |

| NLP | TF-IDF Vectorizer |

| Model | Logistic Regression |







 📂 Project Structure





toxic-comment-detector/

│

├── assets/

│   └── prediction\_demo.png

│

├── model.py

├── requirements.txt

├── README.md

└── .gitignore

```







 ⚙️ Installation



Clone the repository:



```bash

git clone https://github.com/Karunya0403/toxic-comment-detector.git

```



Move into the project directory:



```bash

cd toxic-comment-detector

```



Install the required packages:



```bash

pip install -r requirements.txt

```



\---



 ▶️ Running the Project



```bash

python model.py

```







💻 Sample Output



```text

========================================

&#x20;     Toxic Comment Detector

========================================



Test Accuracy: 0.50



Enter a comment (type 'exit' to stop):



I love this project

Prediction: Non-Toxic ✅



You are useless

Prediction: Toxic ❌

```







 📊 Model Details



| Component | Description |

|-----------|-------------|

| Feature Extraction | TF-IDF Vectorizer |

| Algorithm | Logistic Regression |

| Evaluation | Accuracy, Precision, Recall, F1-Score |

| Framework | Scikit-learn |










 🚀 Future Improvements



 Train the model on a larger real-world toxic comment dataset

 Improve prediction accuracy using advanced NLP models

 Build a Flask or FastAPI web application

 Add a modern web-based user interface

 Experiment with transformer-based models such as BERT

 Deploy the application to the cloud







 🎯 Learning Outcomes



This project demonstrates practical knowledge of:



 Natural Language Processing (NLP)
 
 Text Vectorization

 Machine Learning Classification

 Model Evaluation

 Python Programming

 Scikit-learn Workflow






 👨‍💻 Author



Karunya GK



Artificial Intelligence \& Data Science Engineer



 GitHub: https://github.com/Karunya0403







 ⭐ Support



If you found this project useful, consider giving it a ⭐ on GitHub.

