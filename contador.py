myfile=open("textonormal.txt", "rt") #abrir el archivo textonormal.txt en modo lectura
textocompleto = myfile.read() #guardar sus contenidos en la variable llamada textocompleto
myfile.close() #cerrar el archivo
textosinw=textocompleto.replace("W", "") #guardar el texto sin las W's en textosinw
textosiny=textocompleto.replace("Y","") #guardar el texto sin las Y's en textosiny
textosinf=textocompleto.replace("F","") #guardar el texto sin las F's en textosinf
numerow=len(textocompleto)-len(textosinw) #restar la longitud del texto completo menos la del texto sin la letra deseada, dará el número de veces que estaba escrita
numeroy=len(textocompleto)-len(textosiny)
numerof=len(textocompleto)-len(textosinf)
print("W: " + str(numerow) + "\n") #escribir la información por terminal
print("Y: " + str(numeroy) + "\n")
print("F: " + str(numerof) + "\n")
CEM=5600*numerow+1350*numeroy+200*numerof+17*125 #fórmula sacada del guión de prácticas
print("Coeficiente de extinción molar teórico de la BSA a 280 nm: " + str(CEM) + " M^-1*cm^-1") #escribir la información por terminal
