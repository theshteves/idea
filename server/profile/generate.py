import json
import random

def generator(doc,amount,total):
	rand_list = random.sample(range(1,total),amount)

	#opens personality traits file
	fp = open(doc,"r")

	count = 0
	count_trt = 0
	a_list = []

	#finds traits
	while count_trt < amount:
		for trait in fp:
			if count in rand_list:
				a_list.append(trait.strip())
				count_trt += 1
			if count_trt == amount:
				break
			count += 1
	return a_list

def main(decider):
	person_list = []

	if decider == 1:
		first_name_male = generator("firstname_male.txt",1,100)
		person_list.extend(first_name_male)
	else:
		first_name_female = generator("firstname_female.txt",1,100)
		person_list.extend(first_name_female)

	last_name = generator("lastnames.txt",1,100)
	person_list.extend(last_name)

	traits = generator("traits.txt",4,638)
	person_list.extend(traits)

	person_dict = {}
	info_list = ['First Name', 'Last Name', 'Trait 1', 'Trait 2','Trait 3','Trait 4']
	for i in info_list:
		for j in person_list:
			person_dict[i] = j
			person_list.pop(0)
			break

	return person_dict


user_in = int(input())

new_user = json.dumps(main(user_in),ensure_ascii = False)


print(new_user)
