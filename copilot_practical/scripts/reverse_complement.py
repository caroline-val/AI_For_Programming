# reverse_complement.py
# Reads a DNA sequence from a single-record FASTA file and prints its
# reverse complement.

COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def read_fasta_sequence(path):
    """Return the sequence (str) from a single-record FASTA file."""
    sequence_lines = []
    header_seen = False
    sequence_seen = False

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header_seen:
                    raise ValueError("Expected a single-record FASTA file")
                if sequence_seen:
                    raise ValueError("FASTA sequence data precedes its header")
                header_seen = True
                continue
            sequence_seen = True
            sequence_lines.append("".join(line.split()))

    sequence = "".join(sequence_lines)
    if not sequence:
        raise ValueError("FASTA file contains no sequence")
    return sequence


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    invalid_bases = set(seq) - COMPLEMENT.keys()
    if invalid_bases:
        raise ValueError(
            f"Sequence contains invalid character(s): {''.join(sorted(invalid_bases))}; "
            "expected only A, T, C, or G"
        )
    return "".join(COMPLEMENT[base] for base in reversed(seq))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Print the reverse complement of a single-record FASTA sequence."
    )
    parser.add_argument("fasta_file", help="path to a FASTA file")
    args = parser.parse_args()

    seq = read_fasta_sequence(args.fasta_file)
    print(reverse_complement(seq))
