import matplotlib.pyplot as plt
import numpy as np







inFile = open("ProteinDataset100.fasta")                      # this is to open the file
SeqList = []                   # this is to create a list to hold each string
for i, Line in enumerate(inFile):                          # Add a comment to justify your change
    if not(">" in Line):
        SeqList.append(Line.rstrip())                    
print(SeqList)

def ValCountFunction(SeqList): #this is creating the function
    counts = [] #this is the variable that holds the list of the fraction
    for i, seq in enumerate(SeqList):  #loop to go through each element
        count = seq.count('V')  #see how many no. of V in the each string
        seq_length = len(seq)  #lenth of string
        fraction = round(count / seq_length, 2) #making the fraction up to 2dp
        counts.append(fraction)  #this adds it to the List in counts.
    return counts

ValCountFunction(SeqList) # calling funtion

myCount = ValCountFunction(SeqList)
print(myCount)

plt.hist(myCount, range=(0, 0.25), bins = 10, edgecolor = "black")
plt.xlabel("Fraction of V in amino acid")
plt.ylabel("No. amino acid")
plt.show()

myArray = np.array(myCount) #creating a numpy array
myPercent = myCount * 100 
myPercentAve = np.mean(myArray) * 100 # working out the avg % of V in the amino acids
print('The average percentage of valine amino acids is', myPercentAve, "%")