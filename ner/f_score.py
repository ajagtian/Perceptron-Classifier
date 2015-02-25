#!/usr/bin/python3 -tt

import sys
import re

def	calculate_statistics(in_text, out_text, t_clazz):
		words1 = re.findall(r'(\S+)', in_text)
		words2 = re.findall(r'(\S+)', out_text)
	
		total_classified = 0
		correctly_classified = 0
		total_belonging = 0
		
		if not len(words1) == len(words2):
			print('files not aligned')
			sys.exit(0)

		for i in range(len(words1)):
			word_a = words1[i]
			word_b = words2[i]

		
			clazz_a = word_a[len(word_a) - 1 - word_a[::-1].index('/')+1:].strip()
			clazz_b = word_b[len(word_b) - 1 - word_b[::-1].index('/')+1:].strip()
		
			if clazz_a == t_clazz:
				total_belonging += 1
		
			if clazz_b == t_clazz:
				total_classified += 1

			if clazz_a == t_clazz and clazz_b == t_clazz:
				correctly_classified +=1
		
		
		return (total_belonging, correctly_classified, total_classified)


def	get_file_text(filename):
		f = open(filename, 'rU', errors = 'ignore')
		text = f.read()
		f.close()
		return text


def	main():
		args = sys.argv[1:]
		if len(args) != 3:
			print('usage: ./f_score dev_file out_file test_class')
			sys.exit(0)
		
		(total_belonging, correctly_classified, total_classified) = calculate_statistics(get_file_text(args[0]), get_file_text(args[1]), args[2])
		
		precision = correctly_classified / total_classified
	
		recall = correctly_classified / total_belonging


		f_score = (2 * precision * recall) / (precision + recall)

		print('precision: '+str(precision))
		print('recall: '+str(recall))
		print('f_score: '+str(f_score))


		
if __name__ == '__main__':
	main()	





	

			
		
			
