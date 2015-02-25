#!/usr/bin/python3 -tt

import ast 
import sys
sys.path.insert(0, '../../../csci544-hw1/')
import nbclassify
import re
import io

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


def	classify_word(cur, prev, next, probability_hash, smoothed_hash, document_probabilities):
		context_string = 'CUR:' + cur + ' PREV:' + prev + ' NEXT:' + next
		clazz = nbclassify.classify_line(context_string, probability_hash, smoothed_hash, document_probabilities)
		return clazz


def	tag_word(word, clazz):
		return word + '/' + clazz


def	tag_text(test_text, probability_hash, smoothed_hash, document_probabilities):
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

			clazz = classify_word(CUR, PREV, NEXT, probability_hash, smoothed_hash, document_probabilities)
	
			out_text += tag_word(CUR, clazz) + space

			PREV = CUR
		
		#print(out_text)
		return out_text
		
		
def	tag_lines(lines, probability_hash, smoothed_hash, document_probabilities):
		out_lines = []
		for line in lines:
			out_lines.append(tag_text(line, probability_hash, smoothed_hash, document_probabilities))
		
		return out_lines


def	write_out_lines(out_lines):
		for line in out_lines:
			print(line)
		
		
def	main():
		args = sys.argv[1:]
		if len(args) != 1:
			print('usage: ./nb_postag.py <model_file>')
			sys.exit(0)

		(probability_hash, smoothed_hash, document_probabilities) = nbclassify.modelfile_to_hash(args[0])
		input_stream = io.TextIOWrapper(sys.stdin.buffer, errors='ignore')
		test_lines = input_stream.readlines()
		write_out_lines(tag_lines(test_lines, probability_hash, smoothed_hash, document_probabilities))



if __name__ == '__main__':
	main()
	

