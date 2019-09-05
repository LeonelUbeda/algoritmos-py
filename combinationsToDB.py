
import pymysql
conn = pymysql.connect(host='localhost',  user='root', passwd='admin', db='diccionario')
cur = conn.cursor()

arreglo = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U']

valores = [arreglo[1]]

print(''.join(valores))
for increase in range(5000000):
    carriage = False
    for position in range(0,len(valores)):
        #print(valores[position])
        for unit in range(0,len(arreglo)): 

            if valores[-position-1] == arreglo[unit]:
                if valores[-position-1] == arreglo[-1]: # Si el digito es igual al ultimo del diccionario, lo resetea y pasa al siguiente
                    valores[-position-1] = arreglo[0] #Reset
                    carriage = True #Existe acarreo
                else: #Sino existe acarreo entonces le aumenta uno
                    carriage = False
                    valores[-position-1] = arreglo[unit+1]
                break
            
       #print(acarreo)
        if carriage == False:
            break
    if carriage == True: #Si al final de recorrer toda la cadena, sigue habiendo un acarreo significa que esta en el maximo por lo tanto se le añade un digito
        valores.append(arreglo[0])
    string = "insert palabras(nombre) values('" + ''.join(valores) + "')"
    cur.execute(string)
    print(''.join(valores))

conn.commit()
cur.close()
conn.close()
print('LISTO! Ultimo valo: ' + ''.join(valores))