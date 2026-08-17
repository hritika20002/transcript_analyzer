# 🎙️ Transcript Analyzer — ASR Evaluation

A Python-based evaluation tool for comparing **Automatic Speech Recognition (ASR)** outputs against reference transcripts using **Word Error Rate (WER)**.

The project provides a lightweight workflow for measuring transcription errors, comparing multiple ASR outputs, and identifying which system produces the closest transcription to a reference.

---

## 🎯 Project Objective

Automatic Speech Recognition systems can produce transcripts that appear similar while containing different substitution, deletion, and insertion errors.

This project explores how transcription quality can be evaluated quantitatively using **Word Error Rate (WER)**.

The tool:

* Loads reference and hypothesis transcripts
* Calculates WER for ASR-generated outputs
* Compares results across multiple hypotheses
* Ranks outputs according to transcription accuracy

---

## 📏 Word Error Rate

Word Error Rate is one of the most widely used metrics for evaluating ASR systems.

It measures the number of word-level errors relative to the number of words in the reference transcript.

```text
WER = (Substitutions + Deletions + Insertions) / Reference Words
```

Lower WER generally indicates that a transcription is lexically closer to the reference.

---

## 🔬 Evaluation Workflow

```text
Reference Transcript
        │
        ├──────────────┐
        │              │
        ↓              ↓
ASR Output A      ASR Output B
        │              │
        ↓              ↓
     WER(A)          WER(B)
        │              │
        └──────┬───────┘
               ↓
        Result Comparison
               ↓
         Model Ranking
```

This creates a simple and reproducible workflow for comparing transcription outputs.

---

## 🚀 Features

* Reference-to-hypothesis transcript comparison
* Word Error Rate calculation
* Support for multiple ASR outputs
* Model/output comparison
* Accuracy-based ranking
* Lightweight Python workflow

---

## 🛠️ Tech Stack

**Language:** Python
**Domain:** Natural Language Processing · Automatic Speech Recognition
**Evaluation:** Word Error Rate (WER)
**Library:** jiwer

---

## 📁 Project Structure

```text
transcript_analyzer/
│
├── data/
│   └── ...
│
├── src/
│   └── ...
│
├── requirements.txt
└── README.md
```

The `data/` directory contains the transcripts used for evaluation, while `src/` contains the evaluation logic.

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/hritika20002/transcript_analyzer.git
cd transcript_analyzer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The evaluation scripts can then be run from the `src/` directory using the provided transcript data.

---

## 🧪 Example

Given a reference transcript:

```text
the quick brown fox jumps over the lazy dog
```

and an ASR hypothesis:

```text
the quick brown fox jumped over the lazy dog
```

the evaluator compares the two transcripts and calculates their Word Error Rate.

When multiple hypotheses are provided, their WER scores can be compared to determine which output is lexically closest to the reference.

---

## 💡 What I Learned

This project helped me develop practical experience with:

* Automatic Speech Recognition evaluation
* Word Error Rate and transcription errors
* NLP text comparison
* Reference/hypothesis evaluation workflows
* Python-based research tooling
* Experimental model comparison
* Reproducible evaluation workflows

It also introduced me to an important limitation of ASR evaluation: **lexical similarity does not always capture whether a transcription preserves the meaning of the original speech.**

---

## 🔭 Future Improvements

Potential extensions include:

* Character Error Rate (CER)
* Text normalization before evaluation
* Batch evaluation across larger datasets
* CSV/JSON result export
* Visualization of evaluation results
* Command-line interface
* Additional lexical and semantic evaluation metrics

---

## 👩‍💻 Author

**Hritika Sharma**

Computer Science Graduate · AI & Data Developer

[Portfolio](https://portfolio-pink-ten-96.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/hritikasharma2002/)
