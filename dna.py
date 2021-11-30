# dna
from sys import argv, exit
import csv

"""
written by zebadiah taylor for cs50 on 9/17/20 and is designed for the CS50 IDE.
Reads through a found dna sequence (in .txt) and tests it against a known samples (in a .csv)

test commands
python dna.py databases/small.csv sequences/1.txt           Expected Output: Bob
python dna.py databases/large.csv sequences/12.txt          Expected Output: Lily
python dna.py databases/large.csv sequences/18.txt          Expected Output: No Match
"""

# checks for the correct number of arguments.
if not len(argv) == 3:
    print("To try again, try typing:\n python dna.py __person_databases__.csv sequences/number.txt")
    exit()

# opens dna databases to read
with open(argv[1], newline='') as dna_db:
    reader = csv.DictReader(dna_db)
    
    # opens the dna sequences
    with open(argv[2]) as sequence_reader:
        sequence = sequence_reader.read()
        
    # stores # of max consecutive counts
    unknown_dna_sample = []
    
    # outer loop begins by isolating the STRs to check, found via fieldnames in DictReader
    for x in range(len(reader.fieldnames)):
        # initializes or sets counters to 0
        str_count = 0
        max_str_count = 0
        
        # lnitializes each STR here
        str_to_check = reader.fieldnames[x]
        
        # excludes "name" from iterations
        if str_to_check != "name":
            
            # each loop goes letter by letter through the unidentified sample (sequence)
            for each_letter in range(len(sequence)):
                
                # triggers when there's a STR match and counts repeats
                while str_to_check == (sequence[each_letter:each_letter+len(str_to_check)]):
                    each_letter += len(str_to_check)
                    str_count += 1
                    
                # once STR stops repeating, saves new max count if appropriate.
                if str_count > max_str_count:
                    max_str_count = str_count
                # and then resets str_count
                str_count = 0
                
        # stores STR max_counts into a list to check with.
        unknown_dna_sample.append(max_str_count)
        
    # var only used to output if no match is found.
    match_found = False
    
    # Once the STR counts from the found DNA sequence have been read into unknown_dna_sample
    # iterates through DNA databases and checks values.
    for row in reader:
        str_count_match = 0
        for cell in range(len(reader.fieldnames)):
            if str(unknown_dna_sample[cell]) == str(row[reader.fieldnames[cell]]):
                str_count_match += 1
                
        # checks if str_count_matches == number of possible matches
        # if so, we have the culprit! I mean, suspect.
        if str_count_match == len(reader.fieldnames) - 1:
            print(row['name'])
            match_found = True
            break
        else:
            str_count_match = 0
            
    if match_found == False:
        print("No Match")
