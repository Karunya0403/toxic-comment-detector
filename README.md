\# Toxic Comment Detector



A machine learning project that classifies user comments as \*\*Toxic\*\* or \*\*Non-Toxic\*\* using Natural Language Processing (NLP) techniques. The application converts text into numerical features using \*\*TF-IDF Vectorization\*\* and predicts toxicity with a \*\*Logistic Regression\*\* classifier.



\---



\## Features



\- Detects toxic and non-toxic comments in real time.

\- Uses TF-IDF for text feature extraction.

\- Trained with Logistic Regression.

\- Evaluates model performance using a train-test split.

\- Interactive command-line interface for live predictions.



\---



\## Tech Stack



\- Python

\- pandas

\- scikit-learn

\- TF-IDF Vectorizer

\- Logistic Regression



\---



\## Project Structure



```

toxic-comment-detector/

│

├── assets/

├── model.py

├── requirements.txt

├── README.md

└── .gitignore

```



\---



\## Installation



```bash

pip install -r requirements.txt

```



\---



\## Run the Project



```bash

python model.py

```



\---



\## Sample Output



```

=== Toxic Comment Detector ===



Enter a comment:

> You are amazing



Prediction: Non-Toxic ✅



Enter a comment:

> I hate you



Prediction: Toxic ❌

```



\---



\## Future Improvements



\- Train on a larger real-world dataset.

\- Build a Flask or Streamlit web interface.

\- Save the trained model using Joblib.

\- Add precision, recall, and F1-score metrics.



\---



\## License



This project is intended for educational and portfolio purposes.

