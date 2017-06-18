def two_sum(l, target):
	l = sorted(l)
	i = 0
	j = len(l)-1
	while i < j:
		s = l[i] + l[j]
		if s == target:
			print l[i], l[j]
			i += 1
			j -= 1
		elif s < target:
			i += 1
		else:
			j -= 1
