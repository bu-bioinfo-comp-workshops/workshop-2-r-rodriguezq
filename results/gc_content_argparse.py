# Usage: python3 gc_content_argparse.py -i GCF_014836715.1_ASM1483671v1_genomic.fna -o gc_result.txt

import argparse
import gzip

def calculate_gc_content(seq):
    seq = seq.upper()
    gc_count = seq.count('G') + seq.count('C')
    return gc_count / len(seq) * 100 if seq else 0

def read_fasta(filepath):
    # Automatically handle gzip or plain text based on extension
    open_func = gzip.open if filepath.endswith('.gz') else open
    seq = ""
    with open_func(filepath, 'rt') as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq

def main():
    parser = argparse.ArgumentParser(
        description="Calculate overall GC content from a FASTA file (supports gzipped files).",
        epilog="Example usage:\n  python gc_content.py -i input.fasta.gz -o output.txt",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-i", "--input", required=True, help="Input FASTA file (plain or .gz)")
    parser.add_argument("-o", "--output", required=True, help="Output file to save GC content")
    args = parser.parse_args()

    sequence = read_fasta(args.input)
    gc_content = calculate_gc_content(sequence)

    with open(args.output, 'w') as out_f:
        out_f.write(f"GC content: {gc_content:.2f}%\n")

    print(f"GC content written to {args.output}")

if __name__ == "__main__":
    main()