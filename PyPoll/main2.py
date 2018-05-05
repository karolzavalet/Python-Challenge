# Import the os module
import os
#Import module for reading CSV
import csv
file_name = input("What is the document name and extension? (example_doc.csv)")
csvpath1 = os.path.join('Resources',file_name)
output_file = os.path.join("Analysis_PyPoll.txt")

#Read the CSV module
with open (csvpath1, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    num_voters=0
    candidates_list = []
    candidates_votes = []
    election_results = []
    #Skiping the first row (headers)
    next(csvreader,None)
    for row in csvreader:
        candidate = row[2]
        # Calculate the number of voters
        num_voters +=1
        #Calculating the number of votes per candidate
        if candidate not in candidates_list:
            #If candidate not in the list it will added
            candidates_list.append(candidate)
            i = candidates_list.index(candidate)
            #Initial number of votes per candidate is zero
            candidates_votes.append(0)
        i = candidates_list.index(candidate)
        candidates_votes[i] += 1
    

    #--------------Tests---------------
    #print(candidates_list)
    #print(candidates_votes)
    #print(election_results)
    #----------------------------------

    #Show the results
    print("Election Results")
    print("-"*20)
    print("Total Voters:",num_voters)
    print("-"*20)
    #Calculating and showing the votes per candidate
    c=0
    for i in candidates_votes:
        Candidate_percntg = round(((i/num_voters)*100),1)
        print(str(candidates_list[c])+": "+str(Candidate_percntg)+"% ("+str(i)+")")
        #Creating a list that combines candidates and votes per candidate:i
        election_results.append([candidates_list[c],i])
        #Goes to the next candidate
        c +=1
    print("-"*20)
    #Calculating the winner
    index, winner = max(election_results,key=lambda item: item[1])
    print("Winner: "+str(index))
    print("-"*20)

#Creating a text document for the output
with open(output_file, "w") as f:
    f.write("Election Results\n")
    f.write("----------------------------\n")
    f.write("Total Voters:")
    f.write(str(num_voters))
    f.write("\n")
    f.write("----------------------------\n")
    c=0
    for i in candidates_votes:
        Candidate_percntg = round(((i/num_voters)*100),1)
        f.write(str(candidates_list[c]))
        f.write(": ")
        f.write(str(Candidate_percntg))
        f.write("% (")
        f.write(str(i))
        f.write(")")
        f.write("\n")
        #Creating a list that combines candidates and votes per candidate:i
        election_results.append([candidates_list[c],i])
        #Goes to the next candidate
        c +=1
    f.write("----------------------------\n")
    index, winner = max(election_results,key=lambda item: item[1])
    f.write("Winner:")
    f.write(str(index))
    f.write("\n")
    f.write("----------------------------\n")