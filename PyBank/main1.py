# Import the os module
import os
#Import module for reading CSV
import csv
file_name = input("What is the document name and extension? (example_doc.csv)")
csvpath1 = os.path.join('Resources',file_name)
output_file = os.path.join("Analysis_PyBank.txt")

#Read the CSV module
with open (csvpath1, newline='') as csvfile:
    # Split the data on commas
    csvreader=csv.reader(csvfile,delimiter=',')
    #print(csvreader)
    
    #c is a counter for row numbers in the worksheet
    c=0
    total_rev = 0
    rev_chg = 0
    #past value is the revenue of the previous month
    past = 0
    first = 0
    sum_chg = 0
    rev_chg_data =[]
    for row in csvreader:
        #print(row)
        #data = row
        #next(data,None)
        #print(data)

        if (c>0) :
            #Calculating the total revenue
            total_rev = int(row[1]) + total_rev
            #Calculating the change in revenue per month
            #   For the first value
            if (c==1):
                first = int(row[1])
                past = first
            #   rev_chg: present value - past value
            rev_chg = int(row[1])-past
            #   Storing the current value as past value for the next loop
            past = int(row[1])
            #print(rev_chg)
            sum_chg = rev_chg + sum_chg
            #Storing all the change in revenues in an array
            #rev_chg_data.append(rev_chg)
            rev_chg_data.append([row[0],rev_chg])
            
        #counting number of rows in the worksheet 
        c = c+1
    
    #Calculating total months: total rows - the header row
    total_months = c-1
    #Calculating the average change in revenue between months over the entire period
    #print(sum_chg)
    avrg_chg = (sum_chg)/(total_months-1)
    #Calculating the revenue greatest increase
    #print(rev_chg_data)
    #great_inc = max(rev_chg_data)
    index, great_inc = max(rev_chg_data, key=lambda item: item[1])
    #Calculating the revenue greatest decrease
    #great_dec = min(rev_chg_data)
    index1, great_dec = min(rev_chg_data, key=lambda item: item[1])
    
    #Show the results
    print("Financial Analysis")
    print("-"*20)
    print("Total Months:",total_months)
    print("Total Revenue: $"+str(total_rev))
    print("Average Revenue Change: $"+str(avrg_chg))
    print("Greatest Increase in Revenue: "+str(index)+" ($"+str(great_inc)+")")
    #print("Greatest Decrease in Revenue: $"+str(great_dec))
    print("Greatest Decrease in Revenue: "+str(index1)+" ($"+str(great_dec)+")")

#Creating a text document for the output
with open(output_file, "w") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: ")
    f.write(str(total_months))
    f.write("\n")
    f.write("Total Revenue: $ ")
    f.write(str(total_rev))
    f.write("\n")
    f.write("Average Revenue Change: $")
    f.write(str(avrg_chg))
    f.write("\n")
    f.write("Greatest Increase in Revenue: ")
    f.write(str(index))
    f.write(" ($")
    f.write(str(great_inc))
    f.write(")")
    f.write("\n")
    f.write("Greatest Decrease in Revenue: ")
    f.write(str(index1))
    f.write(" ($")
    f.write(str(great_dec))
    f.write(")")
    f.write("\n")