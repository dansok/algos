def two_sum(l, target):
	l = sorted(l)
	i = 0
	j = len(l)-1
	while i < j:
		if l[i] + l[j] == target:
			print l[i], l[j]
		i += 1
		j += 1
