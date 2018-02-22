"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
"""
#output:
#0.8475

str = "X-DSPAM-Confidence:    0.8475d fds a"
left = -1
right = -1

for letter in str:
    if ((not letter.isdigit()) and left == -1):
        continue
    elif (letter.isdigit() and left == -1):
        left = str.find(letter)
    elif ((not letter.isdigit()) and letter != "." and right == -1):
        right = str.find(letter, left)
        break
    
if right == -1:
    substr = str[left:]
else:
    substr = str[left:right]
    
try:
    print(float(substr))
except:
    print("Invalid number")
     
