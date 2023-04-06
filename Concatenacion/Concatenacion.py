texto1 = "Hola"
texto2 = "Mundo"
textoFinal= ((texto1) + " " + (texto2))
print (textoFinal) # concatencaion 1

print ("el saludo es: %s %s" % (texto2,texto1)) # cocatenacion 2  en esta segunda concatenacion el espacio lo dot en %s %s imprime mundo hola
# pero si pongo %s          %s imprime  mundo          hola

saludoFinal1 = "saludo: {0} {1}".format(texto1, texto2)
print (saludoFinal1) 
#concatenacion 3
saludoFinal2 = "saludo: {x} {y}".format(x= texto1,y= texto2)
print (saludoFinal2) 
#concatenacion 4
