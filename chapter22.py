import math

#finds bm25 score

file = open("record.txt")
a = file.readlines()

#format input into integer two-dimensional array
formattedArr = []
for x in a:
    row = [""]
    intRow = []
    for char in x:
        if char == ' ':
            row.append("")
        elif char != '\n':
            row[len(row) - 1] += char
    for y in row:
        intRow.append(int(y))
    formattedArr.append(intRow)
#---------------------------------------------------------------

finalValues = []


#---------------------------
#formattedArray[y][x]
#---------------------------
    
#find DF for each word. Stored in array------------
words = len(formattedArr[0]) - 2
df = []
r = 2
for x in range(words):
    value = 0
    for doc in range(len(formattedArr)):
        if formattedArr[doc][x + 2] != 0:
            value += 1
    df.append(value)
#---------------------------------------------------------------

#calculate L---------------------------------------
s = 0
for doc in range(len(formattedArr)):
    s += formattedArr[doc][1]
L = s / len(formattedArr)
#-----------------------------------------------------

#k and b values are given--------------------
k = 1.2
b = 0.75
#-----------------------------------------------------
for doc in range(len(formattedArr)):
    # calculate IDF of words and BM25-------------------------------------
    IDF = []
    N = len(formattedArr)
    BM25 = []

    for word in range(words):
        
        #calculating IDF-----------------------------------------------------------
        if (N - df[word] + 0.5)/(df[word] + 0.5) <= 0:
            IDF.append(1)
        else:
            IDF.append(math.log((N - df[word] + 0.5)/(df[word] + 0.5)))
        #-------------------------------------------------------------------------------
        

        #calculate BM25-------------------------
        TF = formattedArr[doc][word + 2]
        BM25.append(IDF[word] * ((TF * (k + 1)) / (TF + k * (1 - b + b * (formattedArr[doc][1]/L)))))

    #---------------------------------------------------------------------------------------

    

    #sum----------------------------------
    sumBM25 = 0
    for val in BM25:
        sumBM25 += val
    finalValues.append(sumBM25)
    #----------------------------------------

#output results
for doc in range(len(formattedArr)):
    print("BM25 Score for document {}: {:0.3f}".format(doc + 1, finalValues[doc]))
