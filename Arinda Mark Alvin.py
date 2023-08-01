print("Enter five family names with their ages.\n")

family = {}
for n in range(1, 6):
	name = input(f'Enter {n} name: ')
	age = int(input(f"Provide {n} name's age: "))
	family[name] = age

print('\n******Family Members******')
age_sum = 0
for name, age in family.items():
	print(f'{name} is {age} years old.')
	age_sum += age

mean_age = age_sum / 5
print(f'\nSum of all the ages is {age_sum} years.')
print(f'Average of all the ages is {mean_age} years.')

if mean_age > 60:
	print('The family is mature.')
else:
	print('The family is young.')


