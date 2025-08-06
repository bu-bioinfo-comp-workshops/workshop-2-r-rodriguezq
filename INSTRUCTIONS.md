# Workshop 2: Large Genome Analysis on the Compute Cluster

Welcome to Workshop 2! In this hands-on session, you will learn how to analyze a large ancient genome dataset using a compute cluster. These materials are scaffolded to guide you step-by-step, with code templates and documentation to help you complete each task.

## Table of Contents
1. Setup and Repository Overview
2. Downloading Large Genome Data
3. Efficient Sequence Analysis (Streaming/Chunking)
4. Submitting Jobs to the Compute Cluster
5. Summarizing and Reporting Results
6. Troubleshooting and Tips

---

## 1. Setup and Repository Overview
- Clone your GitHub Classroom repository.
- Explore the directory structure:
  - `src/`: Python scripts for each analysis step
  - `data/`: Input data files
  - `results/`: Output files
  - `templates/`: Reporting templates
  - `docs/`: Prompts, troubleshooting
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## 2. Downloading Large Genome Data
- Open `src/download_data.py`.
- **TODO:** Write Python code (or use LLM) to download a large FASTA file from a public database (e.g., AADR, NCBI).
- Save the file as `data/ancient_genome.fasta`.

## 3. Efficient Sequence Analysis
- Open `src/analyze_large_genome.py`.
- **TODO:** Modify the script to efficiently compute sequence length and GC content using streaming or chunking (not reading the whole file into memory).
- Print or save the results to `results/sequence_stats.txt`.

## 4. Submitting Jobs to the Compute Cluster
- Open `src/run_analysis.qsub` (or create it).
- **TODO:** Write a qsub script to submit your analysis job to the cluster.
- Use LLM prompts in `docs/sample_prompts.md` for examples.
- Submit your job and monitor its progress.

## 5. Summarizing and Reporting Results
- Use the templates in `templates/` to write your results summary and report.
- Commit and push all your files to GitHub Classroom.

## 6. Troubleshooting and Tips
- Refer to `docs/troubleshooting.md` for common issues and solutions.
- Use LLMs iteratively to debug and improve your code.

---

Good luck! Remember, this workshop is about learning through iteration and problem-solving. Ask for help, use the prompts, and have fun!
