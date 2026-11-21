from pathlib import Path
from huggingface_hub import hf_hub_download

repo_id = "Pannuru/Spam-Detection-SLM"
filename = "spam_detection_slm.gguf"
folder = Path(__file__).resolve().parent

path = hf_hub_download(
    repo_id=repo_id,
    filename=filename,
    repo_type="model",
    local_dir=str(folder),
)
print(f"GGUF downloaded: {path}")
print(f"Size: {Path(path).stat().st_size / (1024 * 1024):.2f} MB")
