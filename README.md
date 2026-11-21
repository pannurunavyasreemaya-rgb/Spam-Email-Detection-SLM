# Spam Email Detection Using a Custom Small Language Model (SLM)

## 1. Project Overview

This project develops a custom Transformer-based Small Language Model (SLM) for binary email and message classification.

The model classifies messages into two categories:
- **Ham (0):** Legitimate message
- **Spam (1):** Unwanted or suspicious message

The custom architecture includes Token Embeddings, Grouped Query Attention (GQA), Rotary Positional Embeddings (RoPE), RMS Normalization, and SwiGLU-style Feed Forward layers.

## 2. Project Objectives

- Develop a custom Transformer-based SLM.
- Classify messages as Spam or Ham.
- Train and evaluate the model.
- Compare model performance.
- Export model weights and configuration.
- Explore GGUF export and Ollama integration.

## 3. Model Architecture

- Architecture: Custom Qwen-inspired Transformer Classifier
- Embedding dimension: 128
- Transformer layers: 2
- Attention heads: 4
- KV groups: 2
- Feed-forward dimension: 256
- Maximum sequence length: 128
- Output classes: 2

## 4. Technologies Used

- Python
- PyTorch
- Hugging Face
- Google Colab
- GGUF
- Ollama

## 5. Model Evaluation

The custom SLM was evaluated on a separate test dataset containing 2,000 messages.

| Metric | Result |
|---|---:|
| Accuracy | 86.00% |
| Spam Precision | 85.69% |
| Spam Recall | 86.71% |
| Spam F1-score | 86.19% |

These results represent the evaluated test dataset and do not guarantee the same performance on all messages.

## 6. Hugging Face Model

The trained model, configuration, tokenizer files, and GGUF export are hosted here:

https://huggingface.co/Pannuru/Spam-Detection-SLM

GGUF file: `spam_detection_slm.gguf`

## 7. Ollama Compatibility

A GGUF export was created and successfully imported into Ollama as a model entry.

However, the custom architecture identifier `spam_transformer_classifier` is not supported by the standard Ollama runtime. Therefore, direct execution of this custom GGUF model has not been achieved.

The project also explores using a separately supported Ollama model, Qwen2.5 0.5B, for conversational explanations. This does not mean that the custom classifier itself runs inside Ollama.

## 8. Project Outcome

This project demonstrates the development, training, evaluation, and export of a custom Transformer-based spam classification model. It also explores GGUF conversion and the challenges of deploying a custom architecture through Ollama.

**GitHub Repository:**  
https://github.com/pannurunavyasreemaya-rgb/Spam-Email-Detection-SLM
