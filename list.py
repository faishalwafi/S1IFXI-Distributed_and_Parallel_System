import numpy
fname = "john.txt";
num_lines = sum(1 for line in open(fname));
array = numpy.zeros((num_lines,4));
k = 0;
with open(fname, "r") as ins:
    for line in ins:    
        a =[int(i) for i in line.split(' ')];
        array[k,0:4] =a;
        k = k+1;
print(array)