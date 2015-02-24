#!/usr/bin/python3 -tt

import sys
import ast
import re

def	get_g_hash_from_file(model_file_name):
		f = open(model_file_name, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		g_hash = {}
		clazz_count = int(lines[0].strip())
		lines = lines[1:]
		for line in lines:
			clazz = line[:line.find('~')]
			clazz_hash = ast.literal_eval(line[line.find('~')+1:])
			g_hash[clazz] = clazz_hash
		
		return g_hash


def	max_score(score_hash):
		max = float('-Inf')
		max_class = ''
		for clazz in score_hash.keys():
			if score_hash[clazz] >= max:
				max = score_hash[clazz]
				max_class = clazz

		return max_class


def	classify(text, g_hash):
		score_hash = {}
		words = re.findall(r'(\S+)', text)
		for clazz in g_hash.keys():
			clazz_hash = g_hash[clazz]
			score = 0
			for word in words:
				if clazz_hash.get(word):
					score += clazz_hash[word]
			score_hash[clazz] = score
		
		predicted_class = max_score(score_hash)

		return predicted_class.strip()

					
def	main():
		args = sys.argv[1:]
		if(len(args) != 1):
			print('usage: ./percepclassify <model_file_name>')
			exit(0)
		test_text = input()
		g_hash = get_g_hash_from_file(args[0])
		print(classify(test_text, g_hash))


if __name__ == '__main__':
	main()
