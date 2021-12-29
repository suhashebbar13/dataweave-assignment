import os
os.system('sort "file1.txt" > "sorted_file1.txt"')
os.system('sort "file2.txt" > "sorted_file2.txt"')
f1 = open('sorted_file1.txt', 'r')
f2 = open('sorted_file2.txt', 'r')

res_file1 = open('result1.txt', 'w')
res_file2 = open('result2.txt', 'w')
try:
    d1 = f1.readline()
    d2 = f2.readline()
    res_file1.write("Occurance\n")
    while True:
        if (int(d1,16) < int(d2,16)):
            d1 = f1.readline()
        elif (int(d2,16) < int(d1,16)):
            d2 = f2.readline()
        else:
            temp = d1
            #print(temp, end='')
            res_file1.write(temp)
            while(d1 == temp):
                d1 = f1.readline()
            while(d2 == temp):
                d2 = f2.readline()            

except Exception as e:
	f1.close()
	f2.close()
res_file1.close()

with open('sorted_file2.txt') as f:
    c = 1
    temp = ''
    res_file2.write("repeatations\n")
    for line in f:
        if line == temp:
            c += 1
        else:
            if temp != '':
                res_file2.write(temp[:-1] + '\t' + str(c) + '\n')
            c = 1
            temp = line
    res_file2.write(temp[:-1] + '\t' + str(c))
res_file2.close()