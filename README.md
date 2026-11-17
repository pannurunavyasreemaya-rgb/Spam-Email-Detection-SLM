# Spam Detection Using a Small Language Model (SLM)

## 1. Project Overview

Spam Detection Using a Small Language Model (SLM) is a deep learning project that classifies text messages or emails into two categories:

- **Ham:** Genuine or legitimate messages.
- **Spam:** Unwanted, promotional, or potentially fraudulent messages.

The project implements a custom Transformer-based architecture to perform binary text classification.

## 2. Project Objectives

- Develop a Small Language Model for spam detection.
- Understand Transformer architecture and its components.
- Preprocess and prepare text data for training.
- Train and evaluate the model using a labelled dataset.
- Host the trained model and dataset on Hugging Face.
- Maintain the complete source code on GitHub.
- Explore deployment and chatbot integration using Ollama.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Google Colab | Model development and training |
| PyTorch | Deep learning framework |
| Pandas | Dataset handling |
| NumPy | Numerical operations |
| Scikit-learn | Data preprocessing and evaluation |
| Hugging Face | Model and dataset hosting |
| GitHub | Source code management |
| Ollama | Planned local chat integration |

## 4. Dataset

The project uses a labelled spam detection dataset containing text samples classified into Ham and Spam categories.

The dataset is divided into:

- `TRAIN.csv` – Training data
- `VALIDATE.csv` – Validation data
- `TEST.csv` – Testing data

**Hugging Face Dataset:**  
https://huggingface.co/datasets/Pannuru/Spam-Detection-Dataset

## 5. Data Preprocessing

The text data is prepared for model training through the following steps:

1. Load the dataset.
2. Inspect the text and labels.
3. Convert text into tokens using a tokenizer.
4. Convert tokens into numerical input IDs.
5. Generate attention masks.
6. Prepare training, validation, and testing data.

## 6. Model Architecture

This project uses a custom Transformer-based Small Language Model.

### Model Configuration

| Parameter | Value |
|---|---:|
| Embedding Dimension | 128 |
| Attention Heads | 4 |
| Key-Value Groups | 2 |
| Transformer Layers | 2 |
| Feed Forward Dimension | 256 |
| Output Classes | 2 |
| Normalization | RMSNorm |

### Main Components

- Token Embedding
- Rotary Positional Embedding (RoPE)
- Grouped Query Attention (GQA)
- RMS Normalization
- SwiGLU Feed Forward Network
- Transformer Blocks
- Classification Layer

The final classification layer predicts whether the input text belongs to the Ham or Spam category.

## 7. Model Training

The model is implemented and trained using PyTorch in Google Colab.

The training workflow includes:

1. Loading the prepared training data.
2. Initializing the Transformer model.
3. Passing tokenized inputs and attention masks.
4. Calculating classification loss.
5. Updating model parameters through backpropagation.
6. Monitoring performance using validation data.
7. Saving the trained model weights.

## 8. Model Evaluation

The trained model should be evaluated using the test dataset.

The following evaluation metrics are used:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Actual evaluation results will be added after the final test evaluation.

## 9. Hugging Face Model Repository

The trained model files are hosted on Hugging Face.

**Model Repository:**  
https://huggingface.co/Pannuru/Spam-Detection-SLM

Important files include:

- `config.json`
- `spam_slm_model.pth`

## 10. GitHub Repository Structure

```text
Spam-Email-Detection-SLM/
│
├── Untitled3.ipynb
├── modeling_spam.py
├── requirements.txt
└── README.md
```

## 11. Installation

Clone the repository:

```bash
git clone https://github.com/pannurunavysreemaya-rgb/Spam-Email-Detection-SLM.git
```

Move into the project folder:

```bash
cd Spam-Email-Detection-SLM
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## 12. Future Enhancements

- Develop a user-friendly interface for spam detection.
- Improve classification performance using further experiments.
- Support different types of text messages and emails.
- Explore local model interaction through Ollama, subject to model compatibility.
- Deploy the application for practical use.

## 13. Conclusion

This project demonstrates the development of a custom Transformer-based Small Language Model for spam detection. It covers dataset preparation, model architecture, training, evaluation, and model hosting. The project provides practical experience in applying deep learning and Natural Language Processing to text classification.

---

**Project:** Spam Detection Using a Small Language Model (SLM)  
**Developer:** Pannuru Navya Sree  
**Department:** CSE – Artificial Intelligence and Machine Learning
