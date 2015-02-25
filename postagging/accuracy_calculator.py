#!/usr/bin/python3 -tt

import ast 
import sys
sys.path.insert(0, '../')
import percepclassify
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


def	classify_word(cur, prev, next, g_hash):
		context_string = 'CUR:' + cur + ' PREV:' + prev + ' NEXT:' + next
		clazz = percepclassify.classify(context_string, g_hash)
		return clazz


def	tag_word(word, clazz):
		return word + '/' + clazz


def	tag_text(test_text, g_hash, correct_guesses, total_words):
		words = re.findall(r'(\S+)', test_text)
		PREV = 'BOS'
		out_text = ''
		for i in range(len(words)):
			space = ''
			word = words[i]
			CUR = word[:len(word) - 1 - word[::-1].index('/')].strip()
			clazz = word[len(word) - 1 - word[::-1].index('/')+1:].strip()
			if i == len(words)-1:
				NEXT = 'EOS'
			else:
				next_word = words[i+1]
				NEXT = next_word[:len(next_word) - 1 - next_word[::-1].index('/')].strip()
				space = ' '

			p_clazz = classify_word(CUR, PREV, NEXT, g_hash)

			if p_clazz == clazz:
				correct_guesses += 1

			total_words += 1

			out_text += tag_word(CUR, p_clazz) + space

			PREV = CUR
		
		#print(out_text)
		return (out_text, correct_guesses, total_words)
		
		
def	tag_lines(lines, g_hash):
		out_lines = []
		correct_guesses = 0
		total_words = 0
		for line in lines:
			(out_text, correct_guesses, total_words) = tag_text(line, g_hash, correct_guesses, total_words)
			out_lines.append(out_text)
		
		return (out_lines, correct_guesses, total_words)


def	write_out_lines(out_lines):
		for line in out_lines:
			print(line)
		
		
def	main():
		args = sys.argv[1:]
		if len(args) != 1:
			print('usage: ./accuracy_calculator.py <model_file>')
			sys.exit(0)

		g_hash = read_g_hash_from_file(args[0])
		input_stream = io.TextIOWrapper(sys.stdin.buffer, errors='ignore')
		test_lines = input_stream.readlines()
		(out_lines, correct_guesses, total_words) = tag_lines(test_lines, g_hash)
		print(str(correct_guesses/total_words))
		write_out_lines(out_lines)



if __name__ == '__main__':
	main()
	

