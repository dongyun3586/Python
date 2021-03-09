s1 = [20, 19, 18, 17, 16]
s2 = [20, 18, 16, 14, 12]
s3 = [10, 8, 6, 4, 2]

fp = open("경우의수.txt", 'w', encoding='utf-8')

for a in s1:
    for b in s2:
        for c in s3:
            for d in s3:
                for e in s3:
                    for f in s3:
                        for g in s3:
                            for h in s3:
                                fp.write(str(a+b+c+d+e+f+g+h)+"\n")
                            
                            
fp.close()