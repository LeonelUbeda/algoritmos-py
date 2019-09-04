
import pymysql
conn = pymysql.connect(host='localhost',  user='root', passwd='admin', db='diccionario')
cur = conn.cursor()

arreglo = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U']

valores = [arreglo[1]]

print(''.join(valores))
for aumento in range(5000000):
    acarreo = False
    for posicion in range(0,len(valores)):
        #print(valores[posicion])
        for unitario in range(0,len(arreglo)): 

            if valores[-posicion-1] == arreglo[unitario]:
                if valores[-posicion-1] == arreglo[-1]: # Si el digito es igual al ultimo del diccionario, lo resetea y pasa al siguiente
                    valores[-posicion-1] = arreglo[0] #Reset
                    acarreo = True #Existe acarreo
                else: #Sino existe acarreo entonces le aumenta uno
                    acarreo = False
                    valores[-posicion-1] = arreglo[unitario+1]
                break
            
       #print(acarreo)
        if acarreo == False:
            break
    if acarreo == True: #Si al final de recorrer toda la cadena, sigue habiendo un acarreo significa que esta en el maximo por lo tanto se le añade un digito
        print('FULL')
        valores.append(arreglo[0])
    string = "insert palabras(nombre) values('" + ''.join(valores) + "')"
    cur.execute(string)

conn.commit()
cur.close()
conn.close()
#print(''.join(valores))
print('LISTO! Ultimo valo: ' + ''.join(valores))