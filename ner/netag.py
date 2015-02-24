#!/usr/bin/python3 -tt

import ast 
import sys
sys.path.insert(0, '../')
import percepclassify
import re

def	read_g_hash_from_file(model_file_name):
		f = open(model_file_name, 'rU', errors = 'ignore')	
		g_hash = {}
		lines = f.readlines()
		clazz_count = int(lines[0].strip())
		lines = lines[1:]
		for line in lines:
			clazz = line[:line.find('~')]
			hash_text = line[line.find('~')+1:]
			clazz_hash = ast.literal_eval(hash_text)
			g_hash[clazz] = clazz_hash
		
		return g_hash


def	classify_word(cur, prev, next, g_hash):
		context_string = 'CUR:' + cur + ' PREV:' + prev + ' NEXT:' + next
		clazz = percepclassify.classify(context_string, g_hash)
		return clazz


def	tag_word(word, clazz):
		return word + '/' + clazz


def	tag_text(test_text, model_file_name):
		g_hash = read_g_hash_from_file(model_file_name)
		words = re.findall(r'(\S+)', test_text)
		PREV = 'BOS'
		out_text = ''
		for i in range(len(words)):
			space = ''
			CUR = words[i]
			if i == len(words)-1:
				NEXT = 'EOS'
			else:
				NEXT = words[i+1]
				space = ' '

			clazz = classify_word(CUR, PREV, NEXT, g_hash)
	
			out_text += tag_word(CUR, clazz) + space

			PREV = CUR
		
		print(out_text)
		
		
def	main():
		args = sys.argv[1:]
		if len(args) != 1:
			print('usage: ./netag.py <model_file>')
			sys.exit(0)
		test_text = input()
		tag_text(test_text, args[0])



if __name__ == '__main__':
	main()
	

