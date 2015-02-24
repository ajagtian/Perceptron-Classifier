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


def	tag_text(test_text, g_hash):
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
		
		#print(out_text)
		return out_text
		
		
def	tag_lines(lines, g_hash):
		out_lines = []
		for line in lines:
			out_lines.append(tag_text(line, g_hash))
		
		return out_lines


def	write_out_lines(out_lines):
		for line in out_lines:
			print(line)
		
		
def	main():
		args = sys.argv[1:]
		if len(args) != 1:
			print('usage: ./postag.py <model_file>')
			sys.exit(0)

		g_hash = read_g_hash_from_file(args[0])
		input_stream = io.TextIOWrapper(sys.stdin.buffer, errors='ignore')
		test_lines = input_stream.readlines()
		write_out_lines(tag_lines(test_lines, g_hash))



if __name__ == '__main__':
	main()
	

