dct = {} #for storing i and s

# opening the file
with open("input.txt") as file:
    for line in file:
        if ':' in line:
            idx = line.index(':')
            i = int(line[:idx])
            s = line[idx+1:-1]
            dct[i] = s
        elif line[:-1] != "":
            m = int(line[:-1])

# storing and sorting keys
dct_k = list(dct.keys())
dct_k.sort()

# creating the output
output = ""
for key in dct_k:
    if m%key==0:
        output+=dct[key]
if output == "":
    output+=str(m)

print(output)
