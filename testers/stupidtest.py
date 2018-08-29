def drawboard(kamal):
	kamal = int(kamal)
	i = 0
	ho = " ---*"
	ve = "|    "
	ho = ho * kamal
	ve = ve * (kamal + 1)
	while i < kamal + 1:
		if i == 0:
			print(*("  " + chr(ord('a') + j) for j in range(kamal)), sep="  ")
		if i < kamal:
			print(i, end="")

		print(ho)
		if not (i == kamal):
			print(ve)
		i += 1
drawboard(3)