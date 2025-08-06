# Troubleshooting Guide: Workshop 2

## Common Issues and Solutions

### 1. Memory Errors
- **Problem:** Python script crashes or is killed when reading large FASTA files.
- **Solution:** Use file streaming (read line by line, not all at once). See examples in `src/analyze_large_genome.py`.

### 2. Slow Data Download
- **Problem:** Downloading large files is very slow or times out.
- **Solution:** Use `requests` with streaming, or command-line tools like `wget` or `curl`. Ensure your network connection is stable.

### 3. Cluster Job Fails
- **Problem:** qsub job does not complete or gives errors.
- **Solution:**
  - Check resource requests (memory, time, CPUs)
  - Review error/output logs
  - Ask for help with error messages

### 4. Output Files Not Found
- **Problem:** Analysis scripts can't find input or output files.
- **Solution:**
  - Double-check file paths and names
  - Use absolute paths if necessary
  - Ensure files are in the correct directories (`data/`, `results/`)

## Tips
- Use LLMs to help debug errors and improve your scripts.
- Ask for help early and often!
