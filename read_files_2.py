fname = input("Enter file name: ")
fh = open(fname)
count = 0
total_count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    count = count + 1
    num = float(line[21:])
    total_count = num + total_count
aver = total_count/count    
     
    
print("average spam confidence:", aver)
