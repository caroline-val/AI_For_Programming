`scripts/gc_content.py` is a command-line tool that calculates the GC content of each sequence in a FASTA file. GC content is the percentage of a sequence’s bases that are guanine (G) or cytosine (C). The script prints each sequence’s FASTA header followed by its GC percentage, rounded to two decimal places.

The required positional argument, `fasta_file`, specifies the path to the input FASTA file. For example, `python scripts/gc_content.py sequences.fasta` processes that file and reports every non-empty sequence. FASTA headers begin with `>`; sequence data may span multiple lines, which the script joins before calculating the percentage. It ignores blank lines and handles lowercase bases by converting sequences to uppercase for counting.

The optional `--min-gc` argument filters the output by GC percentage. For instance, `--min-gc 50` reports only sequences with GC content strictly greater than 50%; sequences at or below the threshold are omitted. Without this option, all non-empty records are reported.

Empty sequences are skipped, and a warning identifying the affected header is written to standard error rather than included in the results. Each reported record appears on its own line, with the header and percentage separated by a tab.
