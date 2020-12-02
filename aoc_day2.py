import os
import copy as cp

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

valid_passwords_p1 = 0
valid_passwords_p2 = 0
for e in lines:
	if not e:
		break

	rule,data = e.split(":")
	intervall,letter= rule.split()
	minimum,maximum = intervall.split("-")
	minimum = int(minimum)
	maximum = int(maximum)
	data = data[1:]
	occurances = data.count(letter)
	if minimum <= occurances <= maximum:
		valid_passwords_p1 += 1

	#part 2
	length = len(data)
	found_letters = 0
	
		
	if data[minimum-1] == letter:
		found_letters += 1
	if data[maximum-1] == letter:
		found_letters += 1 
	
	if found_letters == 1:
		valid_passwords_p2 += 1
	

print(valid_passwords_p1)
print(valid_passwords_p2)