# IMDB Sentiment Analysis using TensorFlow

## 📌 Project Description

This project implements a Deep Learning model for Sentiment Analysis on the IMDB Movie Reviews dataset using TensorFlow and Keras. The model classifies movie reviews as either Positive or Negative based on the sentiment expressed in the text.

The project demonstrates key Natural Language Processing (NLP) concepts such as text tokenization, sequence padding, neural network training, model evaluation, and inference.

---

## 🎯 Objectives

- Build a Deep Learning model for text classification.
- Perform sentiment analysis on movie reviews.
- Apply text preprocessing techniques.
- Evaluate model performance using accuracy metrics.
- Save the trained model for future predictions.
- Visualize training performance using training curves.

---

## 🛠 Technologies Used

- Python 3.11
- TensorFlow
- Keras
- Matplotlib
- NumPy

---

## 📂 Dataset

**Dataset:** IMDB Movie Reviews Dataset

The dataset contains 50,000 movie reviews labeled as:

- Positive Review (1)
- Negative Review (0)

The dataset is automatically downloaded using TensorFlow.

---

## 🧠 Model Architecture

The neural network consists of:

1. Embedding Layer
2. Global Average Pooling Layer
3. Dense Layer (ReLU Activation)
4. Output Layer (Sigmoid Activation)

This architecture is suitable for binary sentiment classification tasks.

---

## ⚙️ Features

- Deep Learning-based Sentiment Analysis
- Automatic Dataset Download
- Text Tokenization and Padding
- Model Training and Evaluation
- Accuracy Visualization
- Saved Model for Inference
- Simple Prediction Script

---

## 📁 Project Structure

```text
IMDB-Sentiment-Analysis-TensorFlow/
│
├── LICENSE
├── README.md
├── predict.py
├── requirements.txt
├── sentiment_model.h5
├── train.py
└── training_curve.png
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
cd PROJECT1
```

Install required packages:

```bash
pip install tensorflow matplotlib numpy
```

---

## ▶️ Training the Model

Run:

```bash
py -3.11 train.py
```

The script will:

- Load the IMDB dataset
- Preprocess text data
- Train the neural network
- Evaluate model performance
- Save the trained model
- Generate a training curve

---

## 📊 Results

Example Results:

| Metric | Value |
|----------|----------|
| Training Accuracy | ~93% |
| Validation Accuracy | ~88% |

Results may vary slightly depending on training conditions.

---

## 📈 Training Curve

The training process generates:

```text
training_curve.png
```

This graph shows:

- Training Accuracy
- Validation Accuracy

across multiple epochs.

---

## 🔮 Running Inference

Run:

```bash
py -3.11 predict.py
```

Expected Output:

```text
Model loaded successfully!
```

---

## 💾 Saved Model

The trained model is saved as:

```text
sentiment_model.h5
```

This model can be loaded later for prediction and deployment.

---

## 📌 Future Enhancements

- Implement LSTM-based sentiment analysis
- Use GRU networks
- Integrate BERT for higher accuracy
- Deploy using FastAPI
- Build a web-based prediction interface

---

## 📚 Learning Outcomes

Through this project, the following concepts were explored:

- Deep Learning Fundamentals
- Natural Language Processing
- Text Tokenization
- Neural Networks using TensorFlow
- Model Evaluation
- Data Visualization
- Model Deployment Preparation

---

## 👨‍💻 Author

**Golla Manikshita**

Undergraduate Student  
Interested in Python, Data Analytics, Machine Learning, and Artificial Intelligence.

---

## 📄 License

This project is developed for educational and internship purposes.
