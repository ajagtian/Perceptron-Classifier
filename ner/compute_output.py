#!/usr/bin/python3 -tt

import netag
import sys


def	get_g_hash(model_file_name):
		g_hash = netag.read_g_hash_from_file(model_file_name)
		return g_hash


def	tag_text(text, g_hash):
		out_text = netag.tag_text(text, g_hash)	
		return out_text


def	tag_file(filename, g_hash):
		f = open(filename, 'rU', errors = 'ignore')
		lines = f.readlines()
		f.close()
		
		out_lines = []
		c = 1
		for line in lines:
			print('tagging line - '+str(c))
			out_lines.append(tag_text(line, g_hash)+'\n')
			c += 1
		
		return out_lines


def	write_out_file(out_file_name, lines):
		f = open(out_file_name, 'w')
		f.writelines(lines)
		f.close()


def	main():	
		args = sys.argv[1:]
		if len(args) != 3:
			print('usage: ./compute_output <test_file> <out_file> <model_file>')
			sys.exit(0)
	
		print('preprocessing...')
		g_hash = get_g_hash(args[2])
		out_lines = tag_file(args[0], g_hash)
		write_out_file(args[1], out_lines)


if __name__ == '__main__':
	main()
	
		
		
