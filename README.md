# Spam Email Detection Using a Custom Small Language Model (SLM)

## 1. Project Overview
This project develops a custom Small Language Model (SLM) using Transformer architecture to classify messages as **Spam** or **Ham (Not Spam)**.

Unlike traditional machine learning approaches, this project implements a custom Transformer-based architecture with Grouped Query Attention (GQA), RMS Normalization, and Feed Forward Networks.

The trained model is integrated with Ollama for an interactive chat demonstration.

## 2. Objectives
- Develop a custom Transformer-based SLM.
- Detect spam and legitimate messages.
- Implement tokenization and vocabulary creation.
- Train and evaluate the custom model.
- Integrate the trained model into an interactive demonstration.

## 3. Technologies Used
- Python
- Google Colab
- PyTorch
- Pandas
- NumPy
- Scikit-learn
- Ollama
- GitHub

## 4. Project Workflow
1. Dataset Collection
2. Data Preprocessing
3. Text Tokenization
4. Vocabulary Creation
5. Custom SLM Architecture
6. Model Training
7. Model Evaluation
8. Ollama Integration
9. Interactive Chat Demonstration

## 5. Custom SLM Architecture

The model contains the following components:

- Token Embedding
- RMS Normalization
- Grouped Query Attention (GQA)
- Feed Forward Network
- Transformer Blocks
- Final RMS Normalization
- Classification Layer

### Model Configuration

| Parameter | Value |
|---|---:|
| Vocabulary Size | 76,408 |
| Embedding Dimension | 128 |
| Attention Heads | 4 |
| KV Groups | 2 |
| Transformer Layers | 2 |
| Feed Forward Dimension | 256 |
| Number of Classes | 2 |
| Model Parameters | 10,078,082 |

## 6. Classification Categories

- **Spam:** Unwanted, promotional, suspicious, or potentially fraudulent messages.
- **Ham:** Normal and legitimate messages.

## 7. Model Files

- `Spam_Detection_SLM.ipynb` – Model development and training notebook.
- `modeling_spam.py` – Custom model architecture.
- `spam_slm_model.pth` – Trained model weights.
- `ollama_chat_demo.py` – Interactive Ollama demonstration.
- `requirements.txt` – Python dependencies.

## 8. Ollama Integration

Ollama is used to demonstrate the model through an interactive chat interface.

The integration workflow includes preparing a compatible model format, configuring Ollama, and testing spam and ham messages.

Note: The PyTorch checkpoint and the Ollama model are separate artifacts. The Ollama integration must use a compatible model format or a documented inference bridge.

## 9. Expected Output

The system classifies user-provided messages into:

- Spam
- Ham (Not Spam)

The interactive demonstration allows users to enter messages and view the classification response.

## 10. Future Enhancements

- Improve classification accuracy.
- Support multiple languages.
- Improve detection of slang and spelling variations.
- Develop a user-friendly web application.
- Expand the training dataset.

## 11. Conclusion

This project demonstrates the development of a custom Small Language Model for spam detection using Transformer architecture. It combines model development, training, text classification, and an interactive demonstration to explore the practical application of SLMs.

## 12. Author

**Pannuru Navya Sree**

B.Tech – CSE (AI & ML)
