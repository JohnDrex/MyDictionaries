# Write a program that uses a dictionary to assign “codes” to each
# letter of the alphabet. For example:

# codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .} 
# Using this example, the letter A would be assigned the symbol %, 
# the letter a would be assigned the number 9, the letter B would 
# be assigned the symbol @, and so forth. 
# The program should open this file -  info_security.txt  
# Download info_security.txt, read its contents, 
# then use the dictionary to write an encrypted version of the
#  file’s contents to a second file (name it 'encrypted.txt').
#  Each character in the second file should contain the code for
#  the corresponding character in the first file.

infile = open("info_security.txt", 'r')
for line in infile:
    text = line

codes = {
'A' : 'I', 'B' : 'w', 'C' : 'r', 'D':'@', 'E':'$', 'F' :'g', 'G': '&', 'H':'(', 'I': '_', 
'J': '+', 'K': '/', 'L':'g', 'M': 'v', 'N':"0", 'O': '9', 'P': '`', 'Q' : '~', 'R':'?', 'S': '>', 'T': '{', 'U':'}', 'V'
: '7', 'W': '.', 'X':',', 'Y': '/', 'Z':']',

'a': 'z', 'b':'6', 'c':')', 'd':'B', 'e':'%', 'f':'5', 'g':'9', 'h':'89', 'i':'^', 'j':'|', 'k':'0', 'l':'{', 'm':'!','n':'O'
, 'o':'_', 'p':'~', 'q':'1', 'r':'>','s':'>', 't':'K', 'u':'2', 'v':'6', 'w':'9', 'x':'0', 'y':'_', 'z': '*'
}

NewText = ""
  
for i in range(0, len(text)):
    if text[i] in codes.keys():
        NewText += codes[text[i]]
    else:
        NewText += text[i]
  
print(NewText)

outfile = open('encrypted.txt', 'w')
outfile.write(NewText + '\n')

outfile.close()


