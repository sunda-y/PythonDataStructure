"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the senders mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

#output
#cwen@iupui.edu 5
fileName = input("Please enter file name: ")
fhandle = open(fileName, "r")

dic = {}
email = None
commits = None

for line in fhandle:
    if line.startswith("From "):
        line = line.split()[1]
        dic[line] = dic.get(line, 0) + 1
        if (commits is None or dic[line] > commits):
            email = line
            commits = dic[line]
            
print("Email is:", email, "commits is:", commits)