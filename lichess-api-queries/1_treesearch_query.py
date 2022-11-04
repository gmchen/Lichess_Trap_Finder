import subprocess
import json
import time
import csv

attacker = "white"
trimmed_prob_cutoff = 0.10
attacker_win_prob_cutoff = 0.45
num_defending_first_moves_to_consider = 5
num_defending_subsequent_moves_to_consider = 2
min_num_games = 100
output_filename = ""

opening_name_dict = {}

# Get opening names from eco database
with open("../external_data/eco_openings_processed/eco_openings_unique_names.tsv", "r", encoding="utf8") as fruits_file:
	tsv_reader = csv.reader(fruits_file, delimiter="\t")

	# Skip the first row, which is the header
	next(tsv_reader)

	for row in tsv_reader:
		opening_name = row[0] + ": " + row[1]
		moves = row[5]
		opening_name_dict[moves] = opening_name

if attacker == "white":
	output_filename = "data_from_queries/position_data_white_attacking.txt"
elif attacker == "black":
	output_filename = "data_from_queries/position_data_black_attacking.txt"

with open(output_filename, "w") as myfile:
	myfile.write("Opening\tUCI_moves\tmove_index\tprob\tprob_trimmed\twhite_wins\tdraws\tblack_wins\twhite_win_prob\tdraw_prob\tblack_win_prob\n")

# Each node is a dict with four key-value pairs: the comma-separated UCI moves, the move index, the probability of this position, and the trimmed probability
stack = []

initial_position = {'opening_name': 1, 'moves': "", 'move_index': 0, 'prob': 1, 'prob_trimmed': 1, 'white_wins':min_num_games, 'draws':min_num_games, 'black_wins':min_num_games, 'white_win_prob':1, 'draw_prob':1, 'black_win_prob':1}
stack.append(initial_position)

while len(stack) > 0:
	print("Stack size: " + str(len(stack)))
	current_position = stack.pop()

	current_attacker_win_prob = float("NaN")
	if attacker == "white":
		current_attacker_win_prob = current_position['white_win_prob']
	if attacker == "black":
		current_attacker_win_prob = current_position['black_win_prob']

	# Check for stop criteria before API query. If we are stopping here, write to file now, using a potentially out of date opening name.
	# Otherwise, we will run the API query to potentially update the opening name then write to file.
	if (current_position['prob_trimmed'] < trimmed_prob_cutoff) or (current_position['white_wins'] + current_position['draws'] + current_position['black_wins'] < min_num_games) or (current_attacker_win_prob < attacker_win_prob_cutoff):
		# Write line to file for this position, using the existing opening name
		with open(output_filename, "a") as myfile:
		    myfile.write(
		    	current_position['opening_name'] + "\t" +
		    	current_position['moves'] + "\t" +
		    	str(current_position['move_index']) + "\t" +
		    	str(current_position['prob']) + "\t" +
		    	str(current_position['prob_trimmed']) + "\t" +
		    	str(current_position['white_wins']) + "\t" +
		    	str(current_position['draws']) + "\t" +
		    	str(current_position['black_wins']) + "\t" +
		    	str(current_position['white_win_prob']) + "\t" +
		    	str(current_position['draw_prob']) + "\t" +
		    	str(current_position['black_win_prob']) + "\n")
		continue
	
	result = ""

	while True:
		num_moves_to_consider = 12
		if (current_position['move_index'] == 2) & (attacker == "white"):
			num_moves_to_consider = 5
		if (current_position['move_index'] == 1) & (attacker == "black"):
			num_moves_to_consider = 5

		# curl -G --data-urlencode "play=e2e4,e7e5,g1f3,b8c6,f1c4,f8c5,e1h1,g8f6,d2d4" --data-urlencode "topGames=0" --data-urlencode "recentGames=0" --data-urlencode "moves=12" https://explorer.lichess.ovh/lichess

		result = subprocess.run(['curl -G --data-urlencode "play=' + current_position['moves'] + '" --data-urlencode "topGames=0" --data-urlencode "recentGames=0" --data-urlencode "moves=' + str(num_moves_to_consider) + '" https://explorer.lichess.ovh/lichess'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		if "429 Too Many Requests" in str(result.stdout):
			print("Received 429 status - waiting 1 minute")
			time.sleep(60)
		else:
			break
	
	json_data = json.loads(result.stdout)

	white_win_prob = json_data['white'] / (json_data['white'] + json_data['draws'] + json_data['black'])
	draw_prob = json_data['draws'] / (json_data['white'] + json_data['draws'] + json_data['black'])
	black_win_prob = json_data['black'] / (json_data['white'] + json_data['draws'] + json_data['black'])

	current_opening_name = ""
	if current_position['move_index'] > 0:
		current_opening_name = json_data['opening']['eco'] + ": " + json_data['opening']['name']

	# Write line to file for this position, using the potentially updated opening name
	if current_position['move_index'] > 0:
		with open(output_filename, "a") as myfile:
		    myfile.write(
		    	current_opening_name + "\t" +
		    	current_position['moves'] + "\t" +
		    	str(current_position['move_index']) + "\t" +
		    	str(current_position['prob']) + "\t" +
		    	str(current_position['prob_trimmed']) + "\t" +
		    	str(current_position['white_wins']) + "\t" +
		    	str(current_position['draws']) + "\t" +
		    	str(current_position['black_wins']) + "\t" +
		    	str(current_position['white_win_prob']) + "\t" +
		    	str(current_position['draw_prob']) + "\t" +
		    	str(current_position['black_win_prob']) + "\n")

	# Check next moves to add to stack if conditions are met. Use reverse order to pop the most frequent position first from the stack
	for next_move in reversed(json_data['moves']):
		next_move_index = current_position['move_index'] + 1

		# Empirical probability of this next move occurring
		prob_next_move = (next_move['white'] + next_move['draws'] + next_move['black']) / (json_data['white'] + json_data['draws'] + json_data['black'])

		# Empirical cumulative probabilities of the entire sequence of moves including the next move
		prob_next_move_cumulative = current_position['prob']
		prob_trimmed_next_move_cumulative = current_position['prob_trimmed']

		# Next move win probabilities
		next_move_white_win_prob = next_move['white'] / (next_move['white'] + next_move['draws'] + next_move['black'])
		next_move_draw_prob = next_move['draws'] / (next_move['white'] + next_move['draws'] + next_move['black'])
		next_move_black_win_prob = next_move['black'] / (next_move['white'] + next_move['draws'] + next_move['black'])

		# Number of games where the next move was played
		next_move_num_games = next_move['white'] + next_move['draws'] + next_move['black']

		# Update probabilities
		next_move_attacker_win_prob = float("NaN")
		if attacker == "white":
			next_move_attacker_win_prob = next_move_white_win_prob
			if(next_move_index % 2 == 0):
				prob_next_move_cumulative = prob_next_move_cumulative * prob_next_move
				if next_move_index > 2:
					prob_trimmed_next_move_cumulative = prob_trimmed_next_move_cumulative * prob_next_move
		if attacker == "black":
			next_move_attacker_win_prob = next_move_black_win_prob
			if(next_move_index % 2 == 1):
				prob_next_move_cumulative = prob_next_move_cumulative * prob_next_move
				if next_move_index > 2:
					prob_trimmed_next_move_cumulative = prob_trimmed_next_move_cumulative * prob_next_move

		# Update the move sequence
		next_position_moves = current_position['moves']
		if current_position['moves'] == "":
			next_position_moves = next_move['uci']
		else:
			next_position_moves = current_position['moves'] + "," + next_move['uci']

		# Update the opening name based on the separately downloaded ECO database
		#next_position_opening_name = current_position['opening_name']
		# Tentatively assign the opening name of the next positions to the opening position of the current position
		next_position_opening_name = current_opening_name

		if next_position_moves in opening_name_dict:
			next_position_opening_name = opening_name_dict[next_position_moves]

		
		next_move_position = {
			'opening_name': next_position_opening_name, 
			'moves': next_position_moves, 
			'move_index': next_move_index, 
			'prob': prob_next_move_cumulative, 
			'prob_trimmed': prob_trimmed_next_move_cumulative,
			'white_wins': next_move['white'],
			'draws': next_move['draws'],
			'black_wins': next_move['black'],
			'white_win_prob': next_move_white_win_prob,
			'draw_prob': next_move_draw_prob,
			'black_win_prob': next_move_black_win_prob
			}
		stack.append(next_move_position)