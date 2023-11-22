contI=1
contJ=1
while contI<=10:
   while contJ <= 10:
       print("%d x %d = %d"%(contI,contJ,contI*contJ))
       contJ+=1
   contJ = 1
   contI = contI + 1
   print("--------------")