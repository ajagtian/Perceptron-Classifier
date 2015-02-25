#!/usr/bin/python3 -tt

import sys
import re
from subprocess import call

def	tokenize_a_line_to_3_words(line, tokenized_lines):
		words = re.findall(r'(\S+)', line)
		prev = 'BOS'
		curr = ''
		next = ''
		for i in range(len(words)):
			context_string = ''
			word = words[i]
			l_slash_index = len(word) - word[::-1].index('/') -1
			clazz = word[l_slash_index+1:].strip()
			curr = word[:l_slash_index].strip()

			if i == len(words)-1:
				next = 'EOS'
			else:
				next = words[i+1]
				next = next[:len(next) - next[::-1].index('/') - 1].strip()

			context_string = clazz + ' ' + 'CUR:' + curr + ' ' + 'PREV:'+prev + ' ' + 'NEXT:' + next + '\n'
			tokenized_lines.append(context_string)
			prev = curr

		return tokenized_lines


def	tokenize_training_set(training_file):
		f = open(training_file, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		tokenized_lines = []

		for line in lines:
			tokenized_lines = tokenize_a_line_to_3_words(line, tokenized_lines)

		return tokenized_lines

def	write_interim_training_file(tokenized_lines, interim_file_name):
		f = open(interim_file_name, 'w')
		f.writelines(tokenized_lines)
		f.close()


def	main():
		args = sys.argv[1:]
		if len(args) != 2:
			print('usage: ./nb_postrain.py <training_file> <model_file>')	
			sys.exit(0)

		tokenized_lines = tokenize_training_set(args[0])
		
		interim_file_name = 'interim_pos_training.txt'
		write_interim_training_file(tokenized_lines, interim_file_name)

		call(['../../../csci544-hw1/nblearn.py', interim_file_name, args[1]])
			
		

if __name__ == '__main__':
	main()
			

			
			
				
