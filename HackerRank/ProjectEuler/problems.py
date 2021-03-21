res = []
f=open("Problems.txt", "w+")
for i in range(1,255):
    
    if i < 10:
        s = "https://www.hackerrank.com/contests/projecteuler/challenges/euler00"+str(i)+"/problem \n\n"
        res.append(s)
    elif i > 9 and i<100:
        s = "https://www.hackerrank.com/contests/projecteuler/challenges/euler0"+str(i)+"/problem \n\n"
        res.append(s)
    else:
        s = "https://www.hackerrank.com/contests/projecteuler/challenges/euler"+str(i)+"/problem \n\n"
        res.append(s)

f.writelines(res)