import requests
import json
import random

def _init_():
	x = 1

def get_story(json_tags):
	"""# All your BLANK are belong to us.
	# You know BLANK, Jon Snow.
	# I want my BLANK back!
	# BLANK is thicker than BLANK...
	# Every BLANK has a silver BLANK

    if number of keywords == 1
    	Generate 1 1-word sentence
    else if number of keywords == 2
    	Generate 1 2-word sentence
    else if number of keywords == 3
    	Generate 2 1-word sentences
    else if number of keywords > 3
    	No limitations
    """
	# loads data from JSON data
	tags = json.loads(json_tags)["tags"]
	ns = []
	for t in tags:
		ns.append(t['name'])

	names = random.sample(ns[0:4], min(random.randint(1, 4), len(ns)))

	phrases = [
		[
			'All your {0} are belong to us.',
			'You know {0}, Jon Snow.',
			'I want my {0} back!!!!',
			"it's ya boi, ... {0}.",
			"hey look it {0}"
		],
		[
			'{0} is thicker than {1}...',
			'{0}?!! More like {1}...',
			'Every {0} has a silver {1}.',
			'{0} vs {1}! Who gonna win?',
			'you suck. theres a {0} and {1} too'
		]
	]
	def formatted(phrase, phrase_size):
		if(phrase_size == 0):
			return phrase.format(names.pop())
		if(phrase_size == 1):
			return phrase.format(names.pop(), names.pop())

	text = ""

	max_sentences = 2
	for phrase_size in range(len(phrases) - 1, -1, -1):
		while len(phrases[phrase_size]) > 0:
			if len(names) > phrase_size:
				text += formatted(phrases[phrase_size].pop(random.randint(0, len(phrases[phrase_size]) - 1)), phrase_size) + " ";
			else:
				break

	if text == "":
		text = "That's a thing"
	return text





	"""define reused variables: phrase = possible phrases, word = place to store randomly chosen words, phrase_string =
	ultimate string to be returned, used_ind = a set of indexes used to make sure all random numbers are not duplicated"""


	word = []
	phrase_string = ''
	used_ind = set()

	"""1 WORD in p_j_r"""
	if len(parsed_json_response) == 1:
		word.append(parsed_json_response["tags"][0]['name'])
		ind = random.randint(0,2)
		phrase_string += phrase[ind].format(word.pop())
		return phrase_string

	"""2 WORDS in p_j_r"""
	if len(parsed_json_response) == 2:
		word.append(parsed_json_response["tags"][0]['name'])
		word.append(parsed_json_response["tags"][1]['name'])
		ind = random.randint(3,4)
		phrase_string += phrase[ind].format(word.pop(), word.pop())
		return phrase_string

	"""3 WORDS in p_j_r"""
	if len(parsed_json_response) == 3:
		word.append(parsed_json_response["tags"][0]['name'])
		word.append(parsed_json_response["tags"][1]['name'])
		word.append(parsed_json_response["tags"][2]['name'])
		for i in range(2):
			ind = random.randint(0,4)
			while ind in used_ind:
				ind = random.randint(0,4)
			used_ind.add(ind)
			if ind < 3:
				phrase_string += phrase[ind].format(word.pop())
			else:
				phrase_string += phrase[ind].format(word.pop(), word.pop())
			phrase_string += ' '
			return phrase_string


	"""GREATER THAN 4 WORDS in p_j_r"""
	if len(parsed_json_response) >= 3:
		for i in range (4):
			ind = random.randint(0, 3)
			while ind in used_ind:
				ind = random.randint(0, 3)
			word.append(parsed_json_response["tags"][ind]['name'])
			used_ind.add(ind)

		used_ind = set()

		for i in range (2):
			ind = random.randint(0,4)
			while ind in used_ind:
				ind = random.randint(0,4)
			used_ind.add(ind)
			if ind < 3:
				phrase_string += phrase[ind].format(word.pop())
			else:
				phrase_string += phrase[ind].format(word.pop(), word.pop())
		phrase_string += ' '
		return phrase_string
