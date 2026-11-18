# Spam Email Detection Using a Custom Small Language Model (SLM)

## 1. Project Overview

This project develops a custom Small Language Model (SLM) using Transformer architecture to classify messages as **Spam** or **Ham (Not Spam)**.

The model uses a custom Qwen-inspired architecture with Grouped Query Attention (GQA), RMS Normalization, Rotary Positional Embeddings (RoPE), and SwiGLU Feed Forward Networks.

The trained model is saved as a PyTorch checkpoint and hosted on Hugging Face.

## 2. Objectives

- Develop a custom Transformer-based SLM.
- Detect spam and legitimate messages.
- Implement text tokenization.
- Train a lightweight classification model.
- Evaluate model performance.
- Develop an interactive spam detection demonstration.

## 3. Technologies Used

- Python
- Google Colab
- PyTorch
- Pandas
- NumPy
- Scikit-learn
- Hugging Face
- GitHub
- Ollama (planned demonstration integration)

## 4. Project Workflow

1. Dataset Collection
2. Data Preprocessing
3. Text Tokenization
4. Custom SLM Architecture
5. Model Training
6. Model Evaluation
7. Hugging Face Model Hosting
8. GitHub Source Code Hosting
9. Interactive Demonstration

## 5. Custom SLM Architecture

The model contains:

- Token Embedding
- RMS Normalization
- Grouped Query Attention (GQA)
- Rotary Positional Embeddings (RoPE)
- SwiGLU Feed Forward Network
- Transformer Blocks
- Final RMS Normalization
- Classification Layer

### Model Configuration

| Parameter | Value |
|---|---:|
| Vocabulary Size | 151,669 |
| Embedding Dimension | 128 |
| Attention Heads | 4 |
| KV Groups | 2 |
| Transformer Layers | 2 |
| Feed Forward Dimension | 256 |
| Number of Classes | 2 |

## 6. Classification Categories

- **Spam (1):** Unwanted, promotional, suspicious, or potentially fraudulent messages.
- **Ham (0):** Normal and legitimate messages.

## 7. Model Files

- `Spam_Detection_SLM.ipynb` – Model development and training notebook.
- `modeling_spam.py` – Custom model architecture.
- `spam_slm_model.pth` – Trained model weights.
- `ollama_chat_demo.py` – Interactive demonstration (to be completed).
- `requirements.txt` – Python dependencies.
- `config.json` – Model configuration.

## 8. Hugging Face Integration

The trained model and tokenizer are hosted on Hugging Face.

**Model Repository:**  
https://huggingface.co/Pannuru/Spam-Detection-SLM

The repository contains the trained PyTorch checkpoint, model configuration, README, and tokenizer files.

## 9. Ollama Integration

The PyTorch classification checkpoint is not directly compatible with Ollama as a generative chat model.

An interactive demonstration will use a compatible inference approach or a separate supported Ollama model connected to the spam classifier.

## 10. Expected Output

The system classifies user-provided messages into:

- Spam
- Ham (Not Spam)

The demonstration allows users to enter messages and view the classification result.

## 11. Future Enhancements

- Improve classification performance.
- Support multiple languages.
- Improve detection of slang and spelling variations.
- Develop a user-friendly web application.
- Expand the training dataset.

## 12. Conclusion

This project demonstrates the development of a custom Small Language Model for spam detection using Transformer architecture. It combines tokenization, model development, training, and text classification to explore the practical application of lightweight language models.

## 13. Author

**Pannuru Navya Sree**  
B.Tech – CSE (AI & ML)
## Model Evaluation

### Custom SLM
- Architecture: Custom PyTorch-based classifier
- Embedding dimension: 128
- Attention heads: 4
- Layers: 2
- Output classes: Ham and Spam

### Comparison Model
- Algorithm: TF-IDF + Logistic Regression
- TF-IDF features: 30,000
- N-gram range: (1, 2)
- Held-out test accuracy: **98.63%**

Note: The comparison model is a separate baseline and its accuracy must not be attributed to the custom SLM.

### Sample Testing
The comparison model was also checked using 5 Ham and 5 Spam samples selected from the dataset. All 10 were classified correctly. This is a sample check, not an independent test evaluation.

### Ollama Chat Demo
Ollama with Qwen 2.5 0.5B is used to demonstrate conversational explanations. The custom `.pth` classifier checkpoint is not directly imported into Ollama.
