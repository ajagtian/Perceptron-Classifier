#!/usr/bin/python3 -tt

import sys
import os
import re

def	extract_classes_and_mine_words_from_training_file(filename):
		f = open(filename, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		classes = {}
		word_hash = {}
		word_count = 1
		for line in lines:
			clazz = line[:line.find(' ')]
			classes[clazz] = 1
			text = line[line.find(' ')+1:]
			(word_hash, word_count) = index_file(text, word_count, word_hash)

		return (classes, word_hash, word_count)


def	index_file(text, word_count, word_hash):
		words = re.findall(r'(\S+)', text)
		
		for word in words:
			if word not in word_hash.keys():
				word_hash[word] = word_count
				word_count += 1
		return (word_hash, word_count)



def 	init_hashes(classes, words):
		g_hash = {}
		for clazz in classes.keys():
			clazz_hash = {}
			for word in words.keys():
				clazz_hash[word] = 0
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


def	update_g_hash_with_a_file(original_class, text, g_hash):
		score_hash = {}
		words = re.findall(r'(\S+)', text)
		for clazz in g_hash.keys():
			score = 0
			clazz_hash = g_hash[clazz]
			for word in words:
				score += clazz_hash[word]
			score_hash[clazz] = score
		
		predicted_class = max_score(score_hash)
		accuracy_adddendum = 0	
		if not predicted_class.strip() == original_class.strip():
			for clazz in g_hash.keys():
				clazz_hash = g_hash[clazz]
				if clazz == original_class:
					for word in words:
						clazz_hash[word] += 1
				else:
					for word in words:
						clazz_hash[word] -= 1
				g_hash[clazz] = clazz_hash
	
		else:
			accuracy_adddendum = 1
			
		return (g_hash, accuracy_adddendum)


def	update_g_hash(training_file_name, g_hash):
		f = open(training_file_name, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		correct_guesses = 0
		total_lines = 0
		for line in lines:
			(g_hash, accuracy_adddendum) = update_g_hash_with_a_file(line[:line.find(' ')], line[line.find(' ')+1:], g_hash)		
			correct_guesses += accuracy_adddendum
			total_lines += 1
		

		return (g_hash, correct_guesses, total_lines)


def	write_g_hash_to_file(g_hash, model_file_name):
		f = open(model_file_name, 'w')
		clazz_count = len(g_hash.keys())
		f.write(str(clazz_count)+'\n')
		for clazz in g_hash.keys():
			clazz_hash = g_hash[clazz]
			f.write(clazz+'~'+str(clazz_hash)+'\n')
		f.close()


def	main():
		args = sys.argv[1:]
		if len(args) != 2:
			print('usage: ./perceplearn.py <training_file> <mode_file>')
			sys.exit(0)		
		print('preprocessing...')
		(classes, word_hash, word_count) = extract_classes_and_mine_words_from_training_file(args[0])
		print('initializing model...')
		g_hash = init_hashes(classes, word_hash)
		#loop start
		print('training...')
		for i in range(30):
			(g_hash, correct_guesses, total_lines) = update_g_hash(args[0], g_hash)
			print('... accuracy '+str(correct_guesses/total_lines))
			if correct_guesses/total_lines > .99:
				break
		print('trained by '+str(i+1)+' iterations')
		# loop end
		print('saving model to file '+args[1]+' ...')
		write_g_hash_to_file(g_hash, args[1])
		
			
if __name__ == '__main__':
	main()
