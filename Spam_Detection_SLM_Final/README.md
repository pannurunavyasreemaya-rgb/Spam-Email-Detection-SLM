# Spam Detection SLM

## Project Overview
A Small Language Model (SLM) project for binary SMS spam detection.

## Model Details
- Architecture: Custom Qwen-inspired Transformer classifier
- Vocabulary Size: 151669
- Embedding Dimension: 128
- Attention Heads: 4
- KV Groups: 2
- Transformer Layers: 2
- Feed Forward Dimension: 256
- Classes: Ham (0), Spam (1)

## Dataset
- Total records: 13,172
- Training: 8,000
- Validation: 3,172
- Testing: 2,000

## Files
- spam_slm_model.pth: Model checkpoint
- config.json: Model configuration
- dataset_info.json: Dataset information
- tokenizer/: Tokenizer files
- requirements.txt: Python dependencies

## Labels
- 0 = Ham
- 1 = Spam

## Hugging Face
https://huggingface.co/Pannuru/Spam-Detection-SLM

## Important
The checkpoint requires its matching model architecture and preprocessing code.
The Ollama demo must use a compatible inference bridge; this classifier
checkpoint is not directly an Ollama generative chat model.
