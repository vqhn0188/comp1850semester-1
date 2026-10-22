# Worksheet 1.3: Task 3

# Your code for the overall grade classification
import os
os.chdir('/workspaces/comp1850semester-1/week1.3/worksheet/task3')
# ask for filename of the student file
fileName = input('What is the filename of the student file? ')
# open the file
with open(fileName, 'r') as file:
    for line in file:
        data = [line.strip().split(',') for line in data]
        L = len(data)
        for x in range (1,L):
            total = total + x
            mean = total / L
            classification = ''
            if mean >= 70 :
                classification = '1'
            elif 70 < mean >= 60 :
                classification = '2:1'
            elif 60 < mean >=  50:
                classification = '2:2'
            elif 50 < mean >= 40 :
                classification = '3'
            else:
                classification = 'F'
            calculatedData = (f'{data[0]},{mean:.2f},{classification}')
            with open (f'{fileName}_out.csv', 'w') as outfile:
                outfile.write(calculatedData)        

    

    # read in the data, and for each student calculate their average grade and classification



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder