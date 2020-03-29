
import csv
import os


path = "/Users/frankwang/Desktop/election_analysis"
file_to_load = os.path.join(path,"Resources", "election_results.csv")

file_to_save = os.path.join(path,"analysis", "election_analysis.txt")
# election_data = open(file_to_load, "r")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1 
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1

# print(total_votes)
# print(candidate_options)
# print(candidate_votes)

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = int(votes) / int(total_votes) * 100
    # print(f"{candidate} : received {vote_percentage:.1f}% of the vote.")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

        print(f"{candidate}: {vote_percentage:.1f}% {votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



    # for row in file_reader:
    #     print(row)

# path1 = "/Users/frankwang/Desktop/election_analysis"
# file_to_save = os.path.join(path,"analysis", "election_analysis.txt")
# open(file_to_save, "w")

# with open (file_to_save, "w") as txt_file:

#     txt_file.write("Counties in the Election\n ------------- \nArapahoe\nDenver\nJefferson")


