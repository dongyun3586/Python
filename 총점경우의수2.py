s1 = [20, 18, 16]
s2 = [20, 15, 10]
s3 = [10, 9, 8]
s4 = [10, 8, 6]

fp = open("경우의수2.txt", 'w', encoding='utf-8')

for a in s1:
    for b in s2:
        for c in s2:
            for d in s3:
                for e in s4:
                    for f in s4:
                        for g in s4:
                            fp.write(str(a+b+c+d+e+f+g)+"\n")
                            
                            
fp.close()