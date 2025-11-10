import os
from jiwer import wer

# Folder containing transcripts
DATA_DIR = "../data/"

def load_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def main():
    reference_file = os.path.join(DATA_DIR, "reference.txt")
    reference_text = load_transcript(reference_file)

    results = {}

    for file in os.listdir(DATA_DIR):
        if file != "reference.txt" and file.endswith(".txt"):
            model_text = load_transcript(os.path.join(DATA_DIR, file))
            error_rate = wer(reference_text, model_text)
            results[file] = error_rate

    # Sort models by lowest WER
    sorted_results = sorted(results.items(), key=lambda x: x[1])

    print("Model Performance (WER):")
    for model, score in sorted_results:
        print(f"{model}: {score:.2f}")

if __name__ == "__main__":
    main()
