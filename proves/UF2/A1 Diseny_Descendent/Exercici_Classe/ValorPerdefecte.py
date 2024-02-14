def operar(n1, n2, operador='+', resposta='El resultat és '):

   resultat= resposta

   if operador=="+":

       resultat= resultat + str(n1+n2)

   elif operador=="-":

       resultat= resultat + str(n1-n2)

   else:

       resultat= resultat +  "BACALAOOOOOOO"

   return resultat


r=operar(40,10, operador="-")
print(r)
#print(operar(5,7))                     #'El resultado es 12'

#print(operar(5,7,"-"))                 #'El resultado es -2'

#print(operar(5,7,"-","La resta es "))  #'La resta es -2'

#print(operar(5,7,"/"))                 # El resultat és BACALAOOOOOOO