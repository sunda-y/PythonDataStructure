"""
 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and coput the average of those values and produce an output as shown below.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

#output:
#Average spam confidence: 0.750718518519

# Use the file name mbox-short.txt as the file name

fileName = input("Please input file name: ")
fhandle = open(fileName, "r")

count = 0
total = 0

for line in fhandle:
    if not "X-DSPAM-Confidence:" in line:
        continue
    else:
        count = count + 1
        
        pos = line.find(":")
        str = line[pos+1:]
        try: 
            num = float(str)
        except:
            print("Invalid number")
            num = 0
        total = total + num

print("#Average spam confidence:", total/count)
        