"""
download_data.py

Download a large ancient genome FASTA file from a public database (e.g., AADR or NCBI).
"""

import requests

# TODO: Set the URL for the large FASTA file you want to download
FASTA_URL = ""
OUTPUT_PATH = "../data/ancient_genome.fasta"


def download_fasta(url: str, output_path: str):
    """Download a FASTA file efficiently using streaming."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"Downloaded {output_path}")


if __name__ == "__main__":
    # TODO: Ask the LLM for possible URLs or use your own
    # download_fasta(FASTA_URL, OUTPUT_PATH)
    pass
