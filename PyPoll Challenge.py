
import csv
import os


# path = "/Users/frankwang/Desktop/election_analysis"
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis2.txt")
# election_data = open(file_to_load, "r")


county_votes = {}
county_options = []
county_count = 0
county_percentage = 0
winning_county = ""
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_percentage_county = 0

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


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    for row in file_reader:
        county_name = row[1]

        if county_name not in county_options:

            county_options.append(county_name)
            county_votes[county_name] = 0
        
        county_votes[county_name] += 1 

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)
   
    txt_file.write("County Votes:")

    for county in county_votes:
        votes_1 = county_votes[county]
        county_percentage = int(votes_1) / int(total_votes) * 100
        county_results_summary = (
            f"{county}:{county_percentage:.1f}% ({votes_1:,})\n")
            

        txt_file.write(county_results_summary)
        # txt_file.write(f"-------------------------\n")

        if (votes_1 > county_count) and (county_percentage > winning_percentage_county):
            county_count = votes_1
            winning_percentage_county = county_percentage
            winning_county = county

        if (votes_1 > county_count):
        # county_count = votes_1
        # winning_percentage_county = county_percentage          
            winning_county = county

    winning_county_summary = (f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n") 

    txt_file.write(winning_county_summary)
    # txt_file.write(f"-------------------------\n")

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(candidate_results)

        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
        
   
        # print(f"{candidate}: {vote_percentage:.1f}% {votes:,})\n")


    # for row in file_reader:
    #     print(row)

# path1 = "/Users/frankwang/Desktop/election_analysis"
# file_to_save = os.path.join(path,"analysis", "election_analysis.txt")
# open(file_to_save, "w")

# with open (file_to_save, "w") as txt_file:

#     txt_file.write("Counties in the Election\n ------------- \nArapahoe\nDenver\nJefferson")


