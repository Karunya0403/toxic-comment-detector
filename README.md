\# Toxic Comment Detector



A simple Natural Language Processing (NLP) project that classifies user comments as \*\*Toxic\*\* or \*\*Non-Toxic\*\* using \*\*TF-IDF Vectorization\*\* and \*\*Logistic Regression\*\*. The application is built with Python and scikit-learn and provides real-time predictions through an interactive command-line interface.



\---



\## Features



\- Detects toxic and non-toxic comments

\- TF-IDF text vectorization

\- Logistic Regression classifier

\- Interactive command-line prediction

\- Model evaluation using Accuracy and Classification Report



\---



\## Tech Stack



\- Python

\- Pandas

\- scikit-learn

\- TF-IDF Vectorizer

\- Logistic Regression



\---



\## Project Structure



```

toxic-comment-detector/

│── assets/

│   └── comment detector.png

│── model.py

│── requirements.txt

│── README.md

│── .gitignore

```



\---



\## Installation



Clone the repository:



```bash

git clone https://github.com/Karunya0403/toxic-comment-detector.git

cd toxic-comment-detector

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\---



\## Usage



Run the project:



```bash

python model.py

```



Example:



```

Enter a comment (type 'exit' to stop): I love this project

Prediction: Non-Toxic ✅



Enter a comment (type 'exit' to stop): You are useless

Prediction: Toxic ❌

```



\---



\## Model



\- Text Vectorization: TF-IDF

\- Machine Learning Algorithm: Logistic Regression

\- Dataset: Small sample dataset created for demonstration purposes



\---



\## Sample Output



The project includes a sample prediction screenshot inside the \*\*assets\*\* folder.



\---



\## Future Improvements



\- Train on a larger real-world dataset

\- Build a Flask/FastAPI web interface

\- Deploy as a web application

\- Improve model accuracy with advanced NLP techniques



\---



\## License



This project is intended for learning and portfolio purposes.

