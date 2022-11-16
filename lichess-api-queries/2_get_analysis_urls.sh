#!/bin/bash

# White attacking
#input_filename="../Analysis/processed_data/white_cluster_representatives_without_analysis.tsv"
#output_filename="../Analysis/processed_data/white_cluster_representatives_with_analysis.tsv"

# Black attacking
input_filename="../Analysis/processed_data/black_cluster_representatives_without_analysis.tsv"
output_filename="../Analysis/processed_data/black_cluster_representatives_with_analysis.tsv"

echo "Start time: $(date)"

printf "Opening	UCI_moves	move_index	prob	prob_trimmed	white_wins	draws	black_wins	white_win_prob	draw_prob	black_win_prob	san	fen	cluster_idx	stockfish_eval	analysis_url\n" > $output_filename

while read -r line
do
	IFS=$'\t'
	read -ra myArray <<< "$line"
	san=${myArray[11]}
	if [[ "$san" == "san" ]]; then
		continue
	fi
	
	echo $line
	echo $san
	
	# Get computer analysis URL
	current_url=""
	while true
	do
		return_val=$(curl -X POST \
			-F "pgn=$san" \
			--retry 5\
			https://lichess.org/api/import)
		echo $return_val
		if [[ "$return_val" =~ .*"Too many requests".* ]]
		then
 			echo "Received too many requests message - waiting 1 minute"
			sleep 60
		else
			break
		fi
	done
	analysis_url="$(echo $return_val | jq -r '[.url] | @tsv')"
	
	printf "$line\t${analysis_url}\n" >> $output_filename
	
	# Sleep 40s to limit to <100 requests / hour
	echo "Sleeping for 40 seconds"
	sleep 40
	
	done < $input_filename

echo "End time: $(date)"
