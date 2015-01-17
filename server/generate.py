
import json
import random

rand_list = random.sample(range(1,638),4)

#opens personality traits file
fp = open("traits.txt","r")

count = 0
count_trt = 0
next = 0

#finds traits
while count_trt < 4:
	for trait in fp:
		if count in rand_list:
			print(trait.strip())
			next = 1
			count_trt += 1
		if count_trt == 4:
			break
		count += 1
