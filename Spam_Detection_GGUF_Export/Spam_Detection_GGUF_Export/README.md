# Spam Detection SLM — GGUF Export Package

This package contains the key supporting files and a downloader for the GGUF model.

## Download the actual GGUF

The binary file is hosted in Hugging Face and is not duplicated in this ZIP. Run:

```bash
pip install -r requirements.txt
python download_gguf.py
```

This downloads `spam_detection_slm.gguf` into this folder.

- GGUF file: https://huggingface.co/Pannuru/Spam-Detection-SLM/blob/main/spam_detection_slm.gguf
- Model repository: https://huggingface.co/Pannuru/Spam-Detection-SLM

## Important Ollama compatibility note

The custom GGUF export was accepted by `ollama create`, but runtime execution failed with:

`unknown model architecture: spam_transformer_classifier`

Therefore, this custom GGUF is **not currently runnable by standard Ollama**. Do not describe it as a working Ollama model.

GGUF is a model container format for tensors and metadata. It does not convert Python source code, datasets, reports, or every project file into GGUF. The `.pth` checkpoint, model implementation, and tokenizer remain separate supporting artifacts.
