import subprocess
import json
import time
import csv
import traceback

attacker = "white"
prob_cutoff = 0.01
trimmed_prob_cutoff = 0.10
attacker_win_prob_cutoff = 0.45
num_attacking_moves_to_consider = 10
num_defending_first_moves_to_consider = 5
num_defending_subsequent_moves_to_consider = 2
min_num_games = 500
raw_json_output_filename = ""
output_filename = ""

if attacker == "white":
	output_filename = "data_from_queries/position_data_white_attacking.txt"
elif attacker == "black":
	output_filename = "data_from_queries/position_data_black_attacking.txt"

if attacker == "white":
	raw_json_output_filename = "data_from_queries/raw_json_data_white_attacking.txt"
elif attacker == "black":
	raw_json_output_filename = "data_from_queries/raw_json_data_black_attacking.txt"

with open(output_filename, "w") as myfile:
	myfile.write("Opening\tUCI_moves\tmove_index\tprob\tprob_trimmed\twhite_wins\tdraws\tblack_wins\twhite_win_prob\tdraw_prob\tblack_win_prob\n")

# Each node is a dict with four key-value pairs: the comma-separated UCI moves, the move index, the probability of this position, and the trimmed probability

stack = []

initial_position = {'opening_name': 1, 'moves': "", 'move_index': 0, 'prob': 1, 'prob_trimmed': 1, 'white_wins':min_num_games, 'draws':min_num_games, 'black_wins':min_num_games, 'white_win_prob':1, 'draw_prob':1, 'black_win_prob':1}
stack.append(initial_position)

# Restart run from intermediate logfile
#stack = eval(open("logs/32000_stack.txt").read())

n_api_queries = 0

while len(stack) > 0:
	print("Stack size: " + str(len(stack)))
	current_position = stack.pop()

	#print("Current position: " + str(current_position))
	if n_api_queries % 1000 == 0:
		# Save stack to file in case there is a need to restart
		with open("logs/" + str(n_api_queries) + "_stack.txt", "w") as myfile:
			myfile.write(str(stack))

	current_attacker_win_prob = float("NaN")
	if attacker == "white":
		current_attacker_win_prob = current_position['white_win_prob']
	if attacker == "black":
		current_attacker_win_prob = current_position['black_win_prob']

	# Check for stop criteria before API query. If we are stopping here, write to file now, using a potentially out of date opening name.
	# Otherwise, we will run the API query to potentially update the opening name then write to file.
	if (current_position['prob_trimmed'] < trimmed_prob_cutoff) or (current_position['prob'] < prob_cutoff) or (current_position['white_wins'] + current_position['draws'] + current_position['black_wins'] < min_num_games) or (current_attacker_win_prob < attacker_win_prob_cutoff):
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
	attempt_number = 1
	query_success = False
	while (attempt_number < 5) & (query_success == False):
		attempt_number = attempt_number + 1
		try:
			while query_success == False:
				num_moves_to_consider = 0
				if attacker == "white":
					if current_position['move_index'] == 1: # This means the next move if black's first move
						num_moves_to_consider = num_defending_first_moves_to_consider
					elif current_position['move_index'] % 2 == 1: # This means the next move is black's non-first move
						num_moves_to_consider = num_defending_subsequent_moves_to_consider
					else: # White to move
						num_moves_to_consider = num_attacking_moves_to_consider
				if attacker == "black":
					if (current_position['move_index'] == 0): # This means the next move is white's first move
						num_moves_to_consider = num_defending_first_moves_to_consider
					elif current_position['move_index'] % 2 == 0: # This means the next move is white's non-first move
						num_moves_to_consider = num_defending_subsequent_moves_to_consider
					else: # Black to move
						num_moves_to_consider = num_attacking_moves_to_consider

				# curl -G --data-urlencode "play=e2e4,e7e5,g1f3,b8c6,f1c4,f8c5,e1h1,g8f6,d2d4" --data-urlencode "topGames=0" --data-urlencode "recentGames=0" --data-urlencode "moves=12" https://explorer.lichess.ovh/lichess

				result = subprocess.run(['curl -G --data-urlencode "play=' + current_position['moves'] + '" --data-urlencode "topGames=0" --data-urlencode "recentGames=0" --data-urlencode "moves=' + str(num_moves_to_consider) + '" https://explorer.lichess.ovh/lichess'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
				if "429 Too Many Requests" in str(result.stdout):
					print("Received 429 status - waiting 1 minute")
					time.sleep(60)
				else:
					query_success = True
			
			json_data = json.loads(result.stdout)
		except Exception as e:
			with open('errors.txt', 'a') as f:
				f.write("Caught an error on attempt " + str(attempt_number) + "\n")
				f.write(str(current_position) + "\n")
				f.write(str(e))
				f.write(traceback.format_exc())

	n_api_queries = n_api_queries + 1
	print("Number of API queries: " + str(n_api_queries))

	# Write raw json output to file
	with open(raw_json_output_filename, "a") as myfile:
	    myfile.write(str(json_data) + "\n")

	white_win_prob = json_data['white'] / (json_data['white'] + json_data['draws'] + json_data['black'])
	draw_prob = json_data['draws'] / (json_data['white'] + json_data['draws'] + json_data['black'])
	black_win_prob = json_data['black'] / (json_data['white'] + json_data['draws'] + json_data['black'])

	current_opening_name = ""
	if current_position['move_index'] > 0:
		current_opening_name = json_data['opening']['eco'] + ": " + json_data['opening']['name']

	# Write line to file for this position, using the potentially updated opening name and other stats
	if current_position['move_index'] > 0:
		with open(output_filename, "a") as myfile:
		    myfile.write(
		    	current_opening_name + "\t" +
		    	current_position['moves'] + "\t" +
		    	str(current_position['move_index']) + "\t" +
		    	str(current_position['prob']) + "\t" +
		    	str(current_position['prob_trimmed']) + "\t" +
		    	str(json_data['white']) + "\t" +
		    	str(json_data['draws']) + "\t" +
		    	str(json_data['black']) + "\t" +
		    	str(white_win_prob) + "\t" +
		    	str(draw_prob) + "\t" +
		    	str(black_win_prob) + "\n")

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
