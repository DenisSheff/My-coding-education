# Напишите программу,
# которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в
# этой четверти (x и y).

quarter = int(input("Enter a value from 1 to 4: "))
if quarter == 1:
	print("Possible values for x and is from 0 to 'possitiveinfinity'.")
elif quarter == 2:
	print("Possible values for x is from zero to 'negative infinity' and for y is from 0 to 'possitive infinity'.")
elif quarter == 3:
	print("Possible values for x and y are from zero to 'negative infinity'")
elif quarter == 4:
	print("Possible values for y is from zero to 'negative infinity' and for x is from 0 to 'possitive infinity'.")
else:
	print("YOU ENTERED WRONG VALUE!")