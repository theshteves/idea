
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


traits = generator("traits.txt",4,638)
#first_name = generator("firstnames.txt",1,)
#last_name = generator("lastname.txt",1)

print(traits)