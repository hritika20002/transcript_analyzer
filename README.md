# 🎙️ Transcript Analyzer — ASR Evaluation

A Python-based evaluation tool for comparing **Automatic Speech Recognition (ASR)** outputs against reference transcripts using **Word Error Rate (WER)**.

The project provides a lightweight and reproducible workflow for measuring transcription errors, comparing multiple ASR outputs, and identifying which output is lexically closest to a reference transcript.

---

## 🎯 Project Objective

Automatic Speech Recognition systems can produce transcripts that appear similar while containing different word substitutions, deletions, and insertions.

This project explores how transcription quality can be evaluated quantitatively using **Word Error Rate (WER)**.

The current version of Transcript Analyzer can:

* Load reference and hypothesis transcripts
* Calculate WER for ASR-generated outputs
* Compare multiple transcription hypotheses
* Rank outputs based on transcription accuracy
* Provide a lightweight Python workflow for ASR evaluation

---

## 📏 Word Error Rate

Word Error Rate is one of the most widely used metrics for evaluating ASR output.

It measures the number of word-level errors relative to the number of words in the reference transcript.

```text
WER = (Substitutions + Deletions + Insertions) / Reference Words
```

Where:

* **Substitutions (S):** one word is replaced by another
* **Deletions (D):** a reference word is missing
* **Insertions (I):** an additional word appears in the hypothesis

A lower WER generally indicates that a transcription is lexically closer to the reference.

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
         Output Ranking
```

This provides a straightforward workflow for comparing transcription outputs using the same reference.

---

## 🚀 Current Features

* Reference-to-hypothesis transcript comparison
* Word Error Rate calculation
* Support for multiple ASR outputs
* Output comparison and ranking
* Python-based evaluation workflow
* Reproducible transcript evaluation

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

The `data/` directory contains transcripts used during evaluation, while `src/` contains the Python evaluation logic.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hritika20002/transcript_analyzer.git
cd transcript_analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the evaluation

Run the evaluation script from the project directory using the transcript data provided in `data/`.

The evaluation compares reference transcripts against ASR-generated hypotheses and calculates their Word Error Rates.

---

## 🧪 Example

Suppose the reference transcript is:

```text
the quick brown fox jumps over the lazy dog
```

and an ASR system produces:

```text
the quick brown fox jumped over the lazy dog
```

Transcript Analyzer compares the hypothesis with the reference and calculates its WER.

When multiple hypotheses are available:

```text
Reference
    │
    ├── ASR Output A → WER
    ├── ASR Output B → WER
    └── ASR Output C → WER
                      ↓
               Compare Results
```

The resulting scores can be used to determine which output is lexically closest to the reference.

---

## 🧠 Why WER Isn't the Whole Story

WER is useful for measuring lexical differences, but a lower WER does not necessarily mean that a transcript better preserves the meaning of the original speech.

For example, two hypotheses may contain different words while expressing very similar meanings. Traditional edit-distance metrics can still penalize those differences.

This limitation makes ASR evaluation an interesting problem beyond simply calculating word-level accuracy and motivates future exploration of both **lexical and semantic evaluation metrics**.

---

## 💡 What I Learned

Building this project helped me develop practical experience with:

* Automatic Speech Recognition evaluation
* Word Error Rate
* NLP text comparison
* Reference/hypothesis evaluation
* Python-based evaluation tooling
* Experimental model comparison
* Reproducible evaluation workflows

It also helped me better understand the difference between **lexical accuracy** and the broader question of whether an ASR transcript preserves the intended meaning.

---

# 🗺️ Development Roadmap

The current implementation focuses on Word Error Rate.

Future development will expand Transcript Analyzer into a more complete ASR evaluation toolkit supporting deeper error analysis, larger datasets, visualization, and additional evaluation metrics.

---

## Phase 1 — Expanded Error Metrics

* [ ] Add Character Error Rate (CER)
* [ ] Report substitutions separately
* [ ] Report deletions separately
* [ ] Report insertions separately
* [ ] Add per-transcript statistics
* [ ] Generate aggregate evaluation statistics

**Goal:** Move beyond a single WER value and provide more diagnostic information about transcription errors.

---

## Phase 2 — Text Normalization

Add a configurable preprocessing pipeline for consistent transcript comparison.

Planned functionality:

* [ ] Lowercasing
* [ ] Punctuation removal
* [ ] Whitespace normalization
* [ ] Contraction normalization
* [ ] Number normalization
* [ ] Evaluation with and without normalization

Example workflow:

```text
Raw Transcript
      ↓
Text Normalization
      ↓
Normalized Transcript
      ↓
ASR Evaluation
```

**Goal:** Understand how preprocessing decisions affect reported ASR performance.

---

## Phase 3 — Batch Evaluation

Expand the tool from individual comparisons to dataset-level evaluation.

Planned functionality:

* [ ] Evaluate multiple transcript pairs in one run
* [ ] Support CSV input
* [ ] Support JSON input
* [ ] Calculate per-transcript metrics
* [ ] Calculate aggregate metrics
* [ ] Compare multiple ASR systems across a dataset

Target workflow:

```text
Dataset
   ↓
Reference + Hypotheses
   ↓
Batch Evaluation
   ↓
Per-Sample Metrics
   ↓
Aggregate Results
   ↓
System Comparison
```

**Goal:** Make the project useful for larger ASR evaluation experiments.

---

## Phase 4 — Result Export

Add structured output for reproducible analysis.

Planned functionality:

* [ ] Export results to CSV
* [ ] Export results to JSON
* [ ] Store model/system names
* [ ] Store per-transcript metrics
* [ ] Store aggregate metrics
* [ ] Generate ranked comparison results

Example target output:

| System |  WER |  CER | Rank |
| ------ | ---: | ---: | ---: |
| ASR A  | 0.12 | 0.06 |    1 |
| ASR B  | 0.18 | 0.09 |    2 |
| ASR C  | 0.23 | 0.12 |    3 |

*Values above are illustrative examples, not reported experimental results.*

**Goal:** Make evaluation results easier to reproduce, analyze, and share.

---

## Phase 5 — Visualization

Add visual analysis of ASR performance.

Planned visualizations include:

* [ ] WER comparison charts
* [ ] CER comparison charts
* [ ] Error-type distributions
* [ ] System-level performance comparisons
* [ ] Per-sample error distributions
* [ ] Summary evaluation reports

**Goal:** Make differences between ASR outputs easier to understand and communicate.

---

## Phase 6 — Command-Line Interface

Develop a CLI so evaluations can be configured without modifying the Python source code.

Target usage:

```bash
python evaluate.py \
  --reference data/reference.csv \
  --hypotheses data/predictions.csv \
  --metrics wer cer \
  --output results/
```

Potential options:

```text
--reference
--hypotheses
--metrics
--normalize
--output
--format
```

**Goal:** Turn the project from a collection of evaluation scripts into a reusable command-line tool.

---

## Phase 7 — Semantic Evaluation

Traditional metrics such as WER and CER measure lexical differences.

A future version of Transcript Analyzer may also experiment with metrics designed to capture **semantic similarity**.

Potential additions include:

* [ ] BERTScore
* [ ] Sentence-embedding similarity
* [ ] Lexical vs. semantic metric comparison
* [ ] Analysis of cases where WER and semantic metrics disagree
* [ ] Combined evaluation reports

A future evaluation pipeline could therefore look like:

```text
                    ┌── WER
                    ├── CER
Transcript Pair ────┼── Error Analysis
                    ├── BERTScore
                    └── Semantic Similarity
                           ↓
                    Evaluation Report
```

**Goal:** Explore whether combining lexical and semantic metrics provides a more informative view of transcription quality.

---

## 🔭 Long-Term Direction

The long-term goal is to evolve Transcript Analyzer from a lightweight WER evaluation script into a **reproducible ASR evaluation toolkit**.

```text
Transcripts
     ↓
Normalization
     ↓
Lexical Evaluation
     ↓
Semantic Evaluation
     ↓
Error Analysis
     ↓
Dataset-Level Comparison
     ↓
Visualization
     ↓
Structured Results
```

Development will be incremental, with each phase adding functionality while keeping the evaluation workflow transparent and reproducible.

---

## 👩‍💻 Author

**Hritika Sharma**

Computer Science Graduate · AI & Data Developer

[Portfolio](https://portfolio-pink-ten-96.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/hritikasharma2002/)
