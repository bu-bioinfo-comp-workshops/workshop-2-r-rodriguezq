"""
analyze_large_genome.py

Efficiently compute sequence length and GC content for a large FASTA file.
"""

# TODO: Import any required modules (e.g., Biopython)

INPUT_FASTA = "../data/ancient_genome.fasta"
OUTPUT_STATS = "../results/sequence_stats.txt"


def compute_stats(fasta_path: str):
    """Compute sequence length and GC content using streaming."""
    seq_len = 0
    gc_count = 0
    # TODO: Implement streaming/chunking logic here
    # Hint: Read file line by line, skip headers, count bases
    return seq_len, gc_count


def write_stats(seq_len: int, gc_count: int, output_path: str):
    """Write the computed stats to a file."""
    # TODO: Calculate GC percentage and write results
    pass


if __name__ == "__main__":
    # TODO: Call compute_stats and write_stats with the correct arguments
    pass
