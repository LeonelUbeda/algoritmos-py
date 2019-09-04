#One of the basic skills a programmer needs is the ability to convert numbers between decimal, hexadecimal, and binary. 
# This article will demonstrate the conversions between each of these bases. 
# Decimal to Hexadecimal Here is an algorithm to convert a decimal integer to hexadecimal: 
# 1) Let X be the decimal integer you wish to convert and let k = 1. 
# 2) Divide X by 16, saving the quotient as Q, and the remainder (in hexadecimal) as Rk . 
# 3) If Q is not zero, let X = Q, k = k + 1, and go back to step 2. Otherwise go to step 4. 
# 4) Assume steps 1-3 were repeated n times. Arrange the remainders as a string of digits - RnRn-1Rn-2…R3R2R1 . 
# Here is an example where we number and describe each iteration of the algorithm: 
# 1) Let X = 954 and let k = 1. Dividing by 16 we have Q = 59 and R1 = A (10 = A in hexadecimal). 
# Since Q is not zero, we let X = 59 and go back to start the second iteration. 
# 2) Dividing X = 59 by 16, we have Q = 3 and R2 = B since 11 = B in hexadecimal. 
# Since Q is not zero, we let X = 3 and start the third iteration. 
# 3) Dividing X = 3 by 16, we have Q = 0 and R3 = 3. 
# Since Q = 0, the loop terminates and the algorithm is completed by arranging the remainders as "3BA". 
# Here is another example using long division. In this example we convert 2623 in decimal to A3F in hexadecimal. 
# The computations move from right to left. FROM 

prueba = ['A','B','C']
salida = ""

def DecToHex(valor): 
    residuo = valor % len(prueba)
    resultado = valor // len(prueba)
    global salida

    salida = salida + prueba[residuo]

    if resultado > 0:
        DecToHex(resultado)

for x in range(0, 20):
    DecToHex(x)
    print(x , salida)
    salida = ""

DecToHex(x)
print(salida)
