
import csv
import os


path = "/Users/frankwang/Desktop/election_analysis"
file_to_load = os.path.join(path,"Resources", "election_results.csv")

file_to_save = os.path.join(path,"analysis", "election_analysis.txt")
# election_data = open(file_to_load, "r")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)


    # headers = next(file_reader)
    # print(headers)

# path1 = "/Users/frankwang/Desktop/election_analysis"
# file_to_save = os.path.join(path,"analysis", "election_analysis.txt")
# open(file_to_save, "w")

# with open (file_to_save, "w") as txt_file:

#     txt_file.write("Counties in the Election\n ------------- \nArapahoe\nDenver\nJefferson")


