f = open('cicd.txt','w+')
for i in range(10):
    f.write(f'This is ${i+1} line')