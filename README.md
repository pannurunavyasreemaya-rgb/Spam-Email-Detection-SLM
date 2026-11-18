# Spam Email Detection Using DistilBERT

## 1. Project Overview

Spam Email Detection Using DistilBERT is a Natural Language Processing (NLP) project that classifies email messages into two categories:

- **HAM (0):** Legitimate email messages.
- **SPAM (1):** Unwanted or suspicious email messages.

The project uses a fine-tuned DistilBERT transformer model to understand email text and predict whether a message is spam or legitimate.

## 2. Project Objectives

- Develop an intelligent spam email classification system.
- Use transformer-based NLP for text classification.
- Identify spam and legitimate email messages.
- Evaluate the model using standard machine learning metrics.
- Host the trained model and dataset on Hugging Face.
- Develop a chat-style demonstration for users.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Google Colab | Model development and training |
| PyTorch | Deep learning framework |
| Hugging Face Transformers | Pretrained transformer model |
| DistilBERT | Text classification architecture |
| Scikit-learn | Evaluation metrics |
| Pandas | Dataset processing |
| GitHub | Source code management |
| Hugging Face Hub | Model and dataset hosting |
| Ollama | Planned local chat demonstration |

## 4. Dataset Collection

The project uses the **Enron Spam Dataset** from Hugging Face.

Dataset source: https://huggingface.co/datasets/SetFit/enron_spam

The dataset contains email text and corresponding labels.

Label mapping:

- 0 = HAM
- 1 = SPAM

## 5. Dataset Preparation

The dataset was loaded using the Hugging Face Datasets library.

The project selected:
- 8,000 email messages for training.
- 2,000 email messages for evaluation.

The notebook also contains code to create separate training, validation, and testing CSV files.

Dataset repository:

https://huggingface.co/datasets/Pannuru/spam-email-dataset

## 6. Data Preprocessing

The following preprocessing steps were performed:

1. Load the email dataset.
2. Convert labels into numerical values.
3. Extract email text and labels.
4. Tokenize email messages using the DistilBERT tokenizer.
5. Apply truncation.
6. Set the maximum sequence length to 128 tokens.
7. Convert the processed data into model-compatible inputs.

## 7. Model Architecture

The project uses **DistilBERT**, a transformer-based language model derived from BERT.

The model is fine-tuned for binary sequence classification.

Model configuration:

| Parameter | Value |
|---|---|
| Base model | distilbert-base-uncased |
| Number of classes | 2 |
| Maximum sequence length | 128 |
| Training epochs | 2 |
| Training batch size | 16 |
| Evaluation batch size | 32 |
| Learning rate | 2e-5 |
| Optimizer | Trainer default configuration |

## 8. Model Training

The model was trained using Google Colab with GPU acceleration.

Hugging Face Trainer was used to manage the training process and evaluation.

The model learns patterns from the email messages and their corresponding labels.

After training, the model and tokenizer were saved using:

```python
trainer.save_model("/content/final_spam_model")
tokenizer.save_pretrained("/content/final_spam_model")
```

## 9. Model Evaluation

The model was evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Evaluation loss

### Recorded evaluation results

| Metric | Result |
|---|---:|
| Accuracy | 98.45% |
| Precision | 98.90% |
| Recall | 98.02% |
| F1-score | 98.46% |
| Evaluation loss | 0.0682 |

These values are from the later training run recorded in the Colab notebook. They represent the notebook's evaluation output, not an independent external benchmark.

## 10. Prediction System

The trained model accepts an email message as input and predicts its category.

Example:

**Input:**

Congratulations! You won a free prize. Click here to claim now!

**Expected classification:**

SPAM

Another example:

**Input:**

Please find attached the meeting schedule for tomorrow.

**Expected classification:**

HAM

The prediction system also displays HAM and SPAM probability scores.

## 11. Spam Indicator Explanation

The project includes a keyword-based explanation feature.

It checks for predefined indicators such as:

- Prize and rewards
- Urgency
- Money offers
- Suspicious links
- Promotional language

These indicators provide additional clues but do not represent the model's actual internal reasoning.

## 12. Hugging Face Model Repository

The trained model is hosted on Hugging Face:

https://huggingface.co/Pannuru/spam-mail-detection

The dataset is hosted at:

https://huggingface.co/datasets/Pannuru/spam-email-dataset

## 13. Ollama Chat Demonstration

Ollama is being explored for a local chat-style demonstration.

Important deployment distinction: the fine-tuned DistilBERT sequence classifier is not directly an Ollama chat-generating model. A separate Python inference interface can call the classifier, while an Ollama language model can provide a conversational interface if integrated.

The final demonstration should clearly identify which model performs the actual spam classification.

## 14. Limitations

- The model is trained on the selected Enron email dataset.
- Performance on unrelated real-world email sources may differ.
- Long messages are truncated to 128 tokens.
- Keyword-based explanations are not causal explanations.
- Evaluation results depend on the dataset split and experimental setup.

## 15. Future Enhancements

- Improve generalization using additional email datasets.
- Test performance on independent real-world email samples.
- Add a professional chat interface.
- Develop a local deployment workflow.
- Explore integration with an Ollama-based conversational interface.
- Perform detailed statistical analysis and error analysis.

## 16. Conclusion

This project demonstrates the application of transformer-based NLP for spam email classification. By fine-tuning DistilBERT, the system learns to distinguish spam and legitimate email messages. The project combines dataset preparation, model training, evaluation, prediction, and model hosting into an end-to-end workflow.

## 17. Project Repository

GitHub: https://github.com/pannurunavysreemaya-rgb/Spam-Email-Detection-SLM

Hugging Face Model: https://huggingface.co/Pannuru/spam-mail-detection

Hugging Face Dataset: https://huggingface.co/datasets/Pannuru/spam-email-dataset
