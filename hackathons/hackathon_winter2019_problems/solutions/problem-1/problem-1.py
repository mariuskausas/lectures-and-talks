def count_nt(s):
	""" Count nt using for loop."""
	nts = (set(s))
	nt_count = {}
	for nt in nts:
		nt_count[nt] = s.count(nt)
	return nt_count


def count_nt2(s):
	""" Count nt using list comprehension."""
	nts = ['A', 'C', 'G', 'T']
	nt_count = [s.count(nt) for nt in nts]
	return nt_count


print(count_nt2("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))

