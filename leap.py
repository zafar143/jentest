year= 2000

if(year%4)==0:

	if (year%100)==0:

		if(year%400)==0:
			print("{0} is leap year",format(year))

		else:
			print("{0} is not leap year",format(year))

	else:
		print("{0} is leap year",format(year))

else:
	print("{0} is not leap year",format(year))