def find_motif(dna, motif):
	""" Finds a motif with a given DNA sequence."""
	# Define string search space
	dna_length = len(dna)
	motif_length = len(motif)
	dna_end = dna_length - motif_length + 1

	# Extract all subsequences with the sample length as a motif
	subseq = [dna[i:i+motif_length] for i in range(dna_end)]

	# Extract indices where a certain motif is with a right numbering (+1)
	indeces = [i+1 for i, j in enumerate(subseq) if j == motif]

	return indeces


print(find_motif("GATATATGCATATACTT", "ATAT"))

