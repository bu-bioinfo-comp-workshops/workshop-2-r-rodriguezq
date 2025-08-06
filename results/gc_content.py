import gzip
import urllib.request

url = "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/014/836/715/GCF_014836715.1_ASM1483671v1/GCF_014836715.1_ASM1483671v1_genomic.fna.gz"

with urllib.request.urlopen(url) as response, gzip.open(response, 'rt') as f:
    seq = "".join(line.strip() for line in f if not line.startswith(">")).upper()

gc = (seq.count("G") + seq.count("C")) / len(seq) * 100 if seq else 0
print(f"Overall GC content: {gc:.2f}%")