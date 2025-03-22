def buscarPalabra(objetivo, palabras):
    objetivo = input("Buscar nombre: ")
    if(objetivo in nombres):
      print(objetivo + ' ' + 'tiene ' + str(edades[objetivo]) + ' años')
    elif(objetivo not in nombres):
      print("el nombre no existe") 
def imprimirListaInversa(lista):
 lista = nombres.reverse

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}
print(buscarPalabra(nombres,edades))
print(imprimirListaInversa(nombres))