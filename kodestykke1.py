
def checkInputValue(value):
	if value > 3:
		if value <= 10:
			print("Value is larger than 3 and smaller than 10")
		else:
			print("Value is larger than or equal to 10")
	else:
		if value < 0:
			print("Value is negative")
		else:
			print("Value is between zero and three")


# White box test: Alle grene testes:
# 3 < value <= 10 --> Value is larger than 3 and smaller than 10
# value > 10 --> Value is larger than or equal to 10
# value < 0 --> Value is negative
# 0 < value < 3 --> Value is between zero and three

# Black box test:
# 0: Value is between zero and three
# "h" Fail: TypeError: '>' not supported between instances of 'str' and 'int'
# None Fail: TypeError: '>' not supported between instances of 'NoneType' and 'int'
# 2.5911 Value is between zero and three
# -2.5911 Value is negative
# 2 Value is between zero and three
# -2 Value is negative
# False Fail (Not a number): Value is between zero and three
# True Fail (Not a number): Value is between zero and three
# [3,1,1,5] TypeError: '>' not supported between instances of 'list' and 'int'
# {"a": 1, "b": 2} TypeError: '>' not supported between instances of 'dict' and 'int'

valToBeChecked = {"a": 1, "b": 2}
print('For value ' +str(valToBeChecked))
checkInputValue(valToBeChecked)
