"""Print the GC content of each sequence in a FASTA file."""

import argparse
import sys


def fasta_records(path):
    """Yield each FASTA header and its concatenated sequence."""
    header = None
    sequence = []

    with open(path) as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(sequence)
                header = line[1:]
                sequence = []
            elif line:
                sequence.append("".join(line.split()))

    if header is not None:
        yield header, "".join(sequence)


def main():
    parser = argparse.ArgumentParser(
        description="Print GC content for each sequence in a FASTA file."
    )
    parser.add_argument("fasta_file", help="path to a FASTA file")
    parser.add_argument(
        "--min-gc",
        type=float,
        help="print only records with GC content above this percentage",
    )
    args = parser.parse_args()

    for header, sequence in fasta_records(args.fasta_file):
        if not sequence:
            print(f"Warning: skipping empty sequence for {header!r}", file=sys.stderr)
            continue
        gc_percent = (sequence.upper().count("G") + sequence.upper().count("C")) / len(
            sequence
        ) * 100
        if args.min_gc is not None and gc_percent <= args.min_gc:
            continue
        print(f"{header}\t{gc_percent:.3f}%")


if __name__ == "__main__":
    main()
