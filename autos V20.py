def calcular_precio(marca,puertas,color,ventas):
    marcas = {'FORD':100000,'CHEVROLET':120000,'FIAT':80000}
    colores = {'Blanco':10000,'Azul':20000,'Negro':30000}
    puertas = {2:50000,4:65000,5:78000}
    precio = marcas[marca]+colores[color]+puertas[puerta]
    if ventas > 5 and ventas < 11:
        precio = precio*0.9
    elif ventas >10 and ventas<51:
        precio = precio*0.85
    elif largo>50:
        precio = precio*0.82
    return precio



mas_clientes = 'si'
ventas = []
marcas = ['FORD','CHEVROLET','FIAT']
puertas = [2,4,5]
colores = ['Blanco','Azul','Negro']
while mas_clientes == 'si':
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    marca = ''
    puerta=0
    color = ''
    while marca not in marcas:
        marca = input('Ingrese marca: ')
        marca = marca.upper()
    while puerta not in puertas:
        puerta = int(input('Ingrese cantidad de puertas: '))
    while color not in colores:
        color = input('Ingrese color: ')
    #precio = calcular_precio(marca,puerta,color)
    ventas.append({'nombre':nombre,'apellido':apellido,'marca':marca,'puertas':puerta,'color':color})
    mas_clientes = input('Hay más clientes?: ')
largo = len(ventas)
for i in ventas:
    precio = calcular_precio(marca,puertas,color,largo)
    print("La persona: " + i['nombre']+" "+i['apellido']+
          " compro un auto marca "+i['marca']+" de " +str(i['puertas'])+" puertas y color "+i['color']+" con un precio de $"+str(precio))

                                                          
