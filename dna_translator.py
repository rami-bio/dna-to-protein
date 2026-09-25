# dna_translator.py
# A simple script to translate a DNA sequence into a protein sequence.

# The standard genetic code (codon table)
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

def translate_dna(sequence):
    """Translate a DNA sequence into a protein sequence."""
    protein = ""
    # Loop through the sequence in steps of 3 (codons)
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        # Stop if the codon is incomplete or a stop codon
        if len(codon) < 3 or codon_table.get(codon) == '*':
            break
        protein += codon_table.get(codon, '?') # '?' for unknown codons
    return protein

# Example usage
if __name__ == "__main__":
    dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
    protein_sequence = translate_dna(dna_sequence)
    print(f"DNA: {dna_sequence}")
    print(f"Protein: {protein_sequence}")
