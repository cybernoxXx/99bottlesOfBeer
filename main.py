# Remember that the range function doesn't count the stop number (in this case 0), so it'll stop at 1
for i in range(99,0,-1):

    if i - 1 == 0:
        print(str(i) + " bottles of beer on the wall,\n" + str(i) + " bottles of beer,\nTake one down,\nPass it around,\nNo more bottles of beer on the wall!")
    else:
        print(str(i) + " bottles of beer on the wall,\n" + str(i) + " bottles of beer,\nTake one down,\nPass it around,\n" + str(i-1) + " bottles of beer on the wall,\n")

for i in range(99,0,-1):
    print(i)