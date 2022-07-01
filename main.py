#Pasos a seguir
#? 1) cargar todos los datasets como dataframes
#? 2) entender los datos
#? 3) chequear las primary keys
#? 4) chequear valores faltantes
#? 5) chequear la distribucion

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sqlalchemy import null


df_cliente = pd.read_csv('Clientes.csv', delimiter=';', encoding='utf-8')
df_compra = pd.read_csv('Compra.csv', delimiter=',', encoding='utf-8')
df_gasto = pd.read_csv('Gasto.csv', delimiter=',', encoding='utf-8')
df_localidades = pd.read_csv('Localidades.csv', delimiter=',', encoding='utf-8')
df_proveedores = pd.read_csv('Proveedores.csv', delimiter=',', encoding = 'latin1')
df_sucursales = pd.read_csv('Sucursales.csv', delimiter=';', encoding='utf-8')
df_venta = pd.read_csv('Venta.csv', delimiter=',', encoding='utf-8')

print(df_venta)


#----------------------------------------------------------------------------------------------------------------------
#?REVISION GENERAL DE TABLAS 
#----------------------------------------------------------------------------------------------------------------------
## CLIENTES 

'''
#tamanio
print(df_cliente.shape)

#info general de clientes
print(df_cliente.info())

#revisar las tabla clientes 
print(df_cliente.head())
print(df_cliente.tail())

# ver las columnas 
print(df_cliente.columns)

# ver si los id estan repetidos o son nulos
print(df_cliente[df_cliente['ID'].duplicated() == True])   #? no hay id repetidos
print(df_cliente[df_cliente['ID'].isnull() == True])       #? no hay id nulos
# valores unicos
print(df_cliente['Provincia'].unique())
print(df_cliente['Localidad'].unique())

#! Diagnostico a resolver
# 1. cambiar valores de las columnas 
# 2. Algunos valores faltantes
# 3. col10 es innecesaria
# 4. cambiar coma por punto en X Y

'''

#----------------------------------------------------------------------------------------------------------------------
# COMPRA


'''
#tamanio
print(df_compra.shape)

# ver las columnas 
print(df_compra.columns)


#info general de clientes
print(df_compra.info())   #faltan valores de precios

#revisar las tabla  
print(df_compra.head())
print(df_compra.tail())       #cambiar tipo de dato fecha_periodo

# ver si los id estan repetidos o son nulos
print(df_compra[df_compra['IdCompra'].duplicated() == True])   #? no hay id repetidos
print(df_compra[df_compra['IdCompra'].isnull() == True])       #? no hay id nulos



#deteccion visual de outlyiers con histograma
x = df_compra['Cantidad']
plt.hist(x, bins=25, color="pink", ec="black")    # no parece haber ouliers con cantidad
plt.show() 

x = df_compra['Precio']
plt.hist(x, bins=25, color="pink", ec="black")
plt.show() 

#! Diagnostico a resolver
# 1. cambiar nombre de las columnas 
# 2. Algunos valores faltantes de precios
# 3. cambiar tipo de dato fecha_periodo
# 4. posible outliers con precios
'''
''''''
#----------------------------------------------------------------------------------------------------------------------
# GASTO

'''

#tamanio
print(df_gasto.shape)                                         #(8640, 5)

# ver las columnas 
print(df_gasto.columns)                                       # escritas correctamente

#info general
print(df_gasto.info())                                        #no hay nulos

#revisar las tabla  
print(df_gasto.head())
print(df_gasto.tail())                                         # parece correcto a simple vista

# ver si los id estan repetidos o son nulos
print(df_gasto[df_gasto['IdGasto'].duplicated() == True])      #? no hay id repetidos
print(df_gasto[df_gasto['IdGasto'].isnull() == True])          #? no hay id nulos

#deteccion visual de outlyiers con histograma
x = df_gasto['Monto']
plt.hist(x, bins=35, color="pink", ec="black")                 # no parece haber ouliers con monto
plt.show() 
'''

#----------------------------------------------------------------------------------------------------------------------
# VENTA

'''
#tamanio
print(df_venta.shape)                       # (46645, 10)

# ver las columnas 
print(df_venta.columns)                     # campos escritos correctamente

#info general
print(df_venta.info())                      #! precio y cantidad tienen faltantes  

#revisar las tabla  
print(df_venta.head())
print(df_venta.tail())                      # parece estar todo normal en principio

# ver si los id estan repetidos o son nulos
print(df_venta[df_venta['IdVenta'].duplicated() == True])      #? no hay id repetidos
print(df_venta[df_venta['IdVenta'].isnull() == True])           #? no hay id nulos

#deteccion visual de outlyiers con histograma
x = df_venta['Precio']
plt.hist(x, bins=2, color="pink", ec="black")                 
plt.show() 

x = df_venta['Precio']
plt.hist(x, bins=2, color="pink", ec="black")                 
plt.show() 

'''
#----------------------------------------------------------------------------------------------------------------------
# LOCALIDAD

'''
#tamanio
print(df_localidades.shape)                               #(4142, 14)

# ver las columnas 
print(df_localidades.columns)                           #! ARREGLAR NOMBRES Y ORDENAR COLUMNAS

#info general
print(df_localidades.info())                            #!VALORES FALTANTES EN MUNICIPIOID Y NOMBRE

#revisar las tabla  
print(df_localidades.head())
print(df_localidades.tail())                            

# BUSCAR VALORES REPETIDOS O NULOS EN ID
print(df_localidades[df_localidades['localidad_censal_id'].duplicated() == True])      
print(df_localidades[df_localidades['localidad_censal_id'].isnull() == True])        #no hay repetidos o nulos


# valores unicos de ciertas columnas
print(df_localidades['provincia_nombre'].unique())                               # no hay valores mal escritos de provincias
print(df_localidades['municipio_nombre'].unique()) 


#deteccion visual de outlyiers con histograma
x = df_localidades['centroide_lat']
plt.hist(x, bins=20, color="pink", ec="black")                 
plt.show()                                                     #centroide_lat al parecer no hay outliers

x = df_localidades['centroide_lon']
plt.hist(x, bins=20, color="pink", ec="black")                 #centroide_lon al parecer no hay outliers
plt.show()  
'''

#----------------------------------------------------------------------------------------------------------------------
# SUCURSALES

'''
#tamanio
print(df_sucursales.shape)                                  # (31, 7)

# ver las columnas 
print(df_sucursales.columns)                                #!CAMBIAR NOMBRE COLUMNA ID
 
#info general
print(df_sucursales.info())                                 #NO HAY NULOS

#revisar las tabla  
print(df_sucursales.head())
print(df_sucursales.tail())                                  #!CAMBIAR COMA POR PUNTO EN LATITUD LONGITUD, NORMALIZAR CABA EN LOCALIDAD Y PROVINCIAS

# BUSCAR VALORES REPETIDOS O NULOS EN ID
print(df_sucursales[df_sucursales['ID'].duplicated() == True])      
print(df_sucursales[df_sucursales['ID'].isnull() == True])                 #NO HAY NULOS NI DUPLICADOS


# valores unicos de ciertas columnas
print(df_sucursales['Provincia'].unique())                               #! NORMALIZAR
print(df_sucursales['Localidad'].unique())                               #! NORMALIZAR

'''
#----------------------------------------------------------------------------------------------------------------------
# PROVEEDORES 

'''
#tamanio
print(df_proveedores.shape)                                         #(14, 7)

# ver las columnas 
print(df_proveedores.columns)                                      #!MODIFICAR NOMBRES COLUMNAS.ESTAN IN INGLES

#info general
print(df_proveedores.info())                                       #! Dos valores nulos en Nombre

#revisar las tabla  
print(df_proveedores.head(20))
print(df_proveedores.tail())                                      #! borrar country

# BUSCAR VALORES REPETIDOS O NULOS EN ID
print(df_proveedores[df_proveedores['IDProveedor'].duplicated() == True])      
print(df_proveedores[df_proveedores['IDProveedor'].isnull() == True])         # no hay valores nulos o repetidos en id 

# valores unicos de ciertas columnas
print(df_proveedores['City'].unique())                               # ok
print(df_proveedores['State'].unique())                              #! NORMALIZAR
print(df_proveedores['departamen'].unique())                          # ok

'''

#----------------------------------------------------------------------------------------------------------------------
#? PROBLEMAS A RESOLVER
#? 1) Modificar nombre de algunas columnas
#? 2) modificar punto por coma y tipo de dato
#? 3) llenar los espacios vacios en el caso de strings
#? 4 ) normalizar los nombres de las provincias principalmente
#? 5 ) deteccion de outliers
#----------------------------------------------------------------------------------------------------------------------
## 1) Modificacion de nombre de columnas

df_cliente.rename(columns={'ID':'IdCliente'}, inplace=True)

df_sucursales.rename(columns={'ID':'IdSucursal'}, inplace=True)

df_proveedores.rename(columns={'Address':'Direccion', 
                               'City':'Localidad', 
                               'State':'Provincia', 
                               'Country':'Pais', 
                               'departamen':'Departamento',
                               'IDProveedor':'IdProveedor'}, inplace=True)

df_localidades.rename(columns={'departamento_id':'IdDepartamento', 
                               'departamento_nombre':'Departamento', 
                               'municipio_id':'IdMunicipio', 
                               'municipio_nombre':'Municipio', 
                               'provincia_id':'IdProvincia',
                               'provincia_nombre':'Provincia',
                               'centroide_lat':'Latitud',
                               'centroide_lon':'Longitud'}, inplace=True)


#----------------------------------------------------------------------------------------------------------------------
## 2) eliminar columnas redundantes 
 
df_cliente.drop("Y", axis = 1, inplace = True )
df_cliente.drop("X", axis = 1, inplace = True )
df_cliente.drop("col10", axis = 1, inplace = True )
df_localidades.drop("nombre", axis = 1, inplace = True )
df_localidades.drop("categoria", axis = 1, inplace = True )
df_proveedores.drop("Pais", axis = 1, inplace = True )
#----------------------------------------------------------------------------------------------------------------------
## 3) llenar los espacios vacios en el caso de strings

#? tabla clientes
df_cliente['Nombre_y_Apellido'].fillna('Sin dato', inplace=True)
df_cliente['Provincia'].fillna('Sin dato', inplace=True)
df_cliente['Domicilio'].fillna('Sin dato', inplace=True)
df_cliente['Telefono'].fillna('Sin dato', inplace=True)
df_cliente['Localidad'].fillna('Sin dato', inplace=True)
#print(df_cliente.info())

#? localidades
df_localidades['Municipio'].fillna('Sin dato', inplace=True)
df_localidades['Departamento'].fillna('Sin dato', inplace=True)
#print(df_localidades.info())

#? Proveedores
df_proveedores['Nombre'].fillna('Sin dato', inplace=True)
#----------------------------------------------------------------------------------------------------------------------
## 4 ) normalizar los nombres de las provincias principalmente



#sucursales                         
df_sucursales['Provincia'].replace(['Ciudad de Buenos Aires', 'CABA', 'C deBuenos Aires', 'Bs As', 'Bs.As. ',
 'Buenos Aires', 'B. Aires', 'B.Aires', 'Provincia de Buenos Aires','Prov de Bs As.', 'Pcia Bs AS'], 'Buenos Aires', inplace=True)
df_sucursales['Provincia'].replace('Cordoba', 'Córdoba', inplace=True)


df_sucursales['Localidad'].replace(['CABA', 'Capital', 'Capital Federal', 'CapFed',
 'Cap. Fed.', 'Cap.   Federal', 'Cdad de Buenos Aires'], 'Ciudad de Buenos Aires', inplace=True)
df_sucursales['Localidad'].replace([ 'Coroba', 'Cordoba'], 'Córdoba', inplace=True)



#proveedores 
df_proveedores['Provincia'].replace( 'CABA', 'BUENOS AIRES', inplace=True)
df_proveedores['Provincia'].replace( 'CAPITAL', 'CIUDAD DE BUENOS AIRES', inplace=True)


#localidades
#print(df_localidades['provincia_nombre'].unique())                              
#print(df_localidades['municipio_nombre'].unique()) 
#print(df_localidades.info())

# ## 4.2 ) normalizar los nombres de todas las columnas con el metodo title
#proveedores
df_proveedores['Provincia'] = df_proveedores['Provincia'].str.title()
df_proveedores['Departamento'] = df_proveedores['Departamento'].str.title()
df_proveedores['Localidad'] = df_proveedores['Localidad'].str.title()
df_proveedores['Direccion'] = df_proveedores['Direccion'].str.title()
df_proveedores['Nombre'] = df_proveedores['Nombre'].str.title()
#sucursales
df_sucursales['Sucursal'] = df_sucursales['Sucursal'].str.title()
df_sucursales['Direccion'] = df_sucursales['Direccion'].str.title()
df_sucursales['Localidad'] = df_sucursales['Localidad'].str.title()
df_sucursales['Provincia'] = df_sucursales['Provincia'].str.title()

#cliente
df_cliente['Nombre_y_Apellido'] = df_cliente['Nombre_y_Apellido'].str.title()
df_cliente['Domicilio'] = df_cliente['Domicilio'].str.title()
df_cliente['Localidad'] = df_cliente['Localidad'].str.title()


#localidades
df_localidades['Provincia'] = df_localidades['Provincia'].str.title()
df_localidades['Municipio'] = df_localidades['Municipio'].str.title()
df_localidades['Departameno'] = df_localidades['Provincia'].str.title()

print(df_localidades)
#----------------------------------------------------------------------------------------------------------------------
#? 5 ) deteccion de outliers



#for i in (df_venta['IdProducto'].unique()):
# print(df_venta[df_venta['IdProducto'] == i][df_venta['Precio'] > df_venta[df_venta['IdProducto'] == i]['Precio'].mean() + 2*df_venta[df_venta['IdProducto'] == i]['Precio'].std()])


#df_venta["Outlier"] = np.where(df_venta["Precio"] > df_venta[df_venta['IdProducto'] == 42817]['Precio'].mean() + 2*df_venta[df_venta['IdProducto'] == 42817]['Precio'].std(), 1, 0)

#? Se crea una columna en ventas, llamada outliers la cual toma el valor de 0 si es outlier. es decir si su valor
#? es mayor a al media por produco mas el desvio
#? luego se eliminan los outliers y registros vacios
for i in df_venta["IdProducto"].unique():
     df_venta["Outlier"] = np.where(df_venta["Precio"] > df_venta[df_venta['IdProducto'] == i ]['Precio'].mean() + 2*df_venta[df_venta['IdProducto'] == i ]['Precio'].std(), 0, 1)

df_venta["Precio2"] = df_venta["Precio"] * df_venta["Outlier"]


#se lleva a cabo lo mismo pero con Compra
print(df_compra[df_compra['IdProducto'] == 42833])

for i in df_venta["IdProducto"].unique():
    df_compra["Outlier"] = np.where(df_compra["Precio"] > (df_compra[df_compra['IdProducto'] == i ]['Precio'].mean() + 4*df_compra[df_compra['IdProducto'] == i ]['Precio'].std()), 0, 1)
    #print(df_compra[df_compra['IdProducto'] == 42833][df_compra['Precio'] > df_compra[df_compra['IdProducto'] == 42833]['Precio'].mean() + 2*df_compra[df_compra['IdProducto'] == 42833]['Precio'].std()])
print(df_compra.sum())

df_compra["Precio2"] = df_compra["Precio"] * df_compra["Outlier"]




#---------------------------------------------------------------------------------------------------------------------
#Autolatizacion de la ingesta de datos de la tabla clientes
#? importante colocar cliente_vn ---> siendo n un numero.

'''
import glob
import os
import pandas as pd
path =r'C:\Users\54261\OneDrive\Escritorio\Proyecto-individual I\clientes'
filenames = glob.glob(path + "/*.csv")
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))

df_cliente = pd.concat(dfs, ignore_index=True)
'''

# se realiza lo mismo con cada tabla, creando un archivo con el nombre de cada unos
#Posteriormente, se debe proceder a ejecutar el siguiento bloque de codigo


'''

df_cliente.rename(columns={'ID':'IdCliente'}, inplace=True)

df_sucursales.rename(columns={'ID':'IdSucursal'}, inplace=True)

df_proveedores.rename(columns={'Address':'Direccion', 
                               'City':'Localidad', 
                               'State':'Provincia', 
                               'Country':'Pais', 
                               'departamen':'Departamento',
                               'IDProveedor':'IdProveedor'}, inplace=True)

df_localidades.rename(columns={'departamento_id':'IdDepartamento', 
                               'departamento_nombre':'Departamento', 
                               'municipio_id':'IdMunicipio', 
                               'municipio_nombre':'Municipio', 
                               'provincia_id':'IdProvincia',
                               'provincia_nombre':'Provincia',
                               'centroide_lat':'Latitud',
                               'centroide_lon':'Longitud'}, inplace=True)


 
 
df_cliente.drop("Y", axis = 1, inplace = True )
df_cliente.drop("X", axis = 1, inplace = True )
df_cliente.drop("col10", axis = 1, inplace = True )
df_localidades.drop("nombre", axis = 1, inplace = True )
df_localidades.drop("categoria", axis = 1, inplace = True )
df_proveedores.drop("Pais", axis = 1, inplace = True )


#? tabla clientes
df_cliente['Nombre_y_Apellido'].fillna('Sin dato', inplace=True)
df_cliente['Provincia'].fillna('Sin dato', inplace=True)
df_cliente['Domicilio'].fillna('Sin dato', inplace=True)
df_cliente['Telefono'].fillna('Sin dato', inplace=True)
df_cliente['Localidad'].fillna('Sin dato', inplace=True)
#print(df_cliente.info())

#? localidades
df_localidades['Municipio'].fillna('Sin dato', inplace=True)
df_localidades['Departamento'].fillna('Sin dato', inplace=True)
#print(df_localidades.info())

#? Proveedores
df_proveedores['Nombre'].fillna('Sin dato', inplace=True)


#sucursales                         
df_sucursales['Provincia'].replace(['Ciudad de Buenos Aires', 'CABA', 'C deBuenos Aires', 'Bs As', 'Bs.As. ',
 'Buenos Aires', 'B. Aires', 'B.Aires', 'Provincia de Buenos Aires','Prov de Bs As.', 'Pcia Bs AS'], 'Buenos Aires', inplace=True)
df_sucursales['Provincia'].replace('Cordoba', 'Córdoba', inplace=True)


df_sucursales['Localidad'].replace(['CABA', 'Capital', 'Capital Federal', 'CapFed',
 'Cap. Fed.', 'Cap.   Federal', 'Cdad de Buenos Aires'], 'Ciudad de Buenos Aires', inplace=True)
df_sucursales['Localidad'].replace([ 'Coroba', 'Cordoba'], 'Córdoba', inplace=True)



#proveedores 
df_proveedores['Provincia'].replace( 'CABA', 'BUENOS AIRES', inplace=True)
df_proveedores['Provincia'].replace( 'CAPITAL', 'CIUDAD DE BUENOS AIRES', inplace=True)


#localidades
#print(df_localidades['provincia_nombre'].unique())                              
#print(df_localidades['municipio_nombre'].unique()) 
#print(df_localidades.info())

# ## 4.2 ) normalizar los nombres de todas las columnas con el metodo title
#proveedores
df_proveedores['Provincia'] = df_proveedores['Provincia'].str.title()
df_proveedores['Departamento'] = df_proveedores['Departamento'].str.title()
df_proveedores['Localidad'] = df_proveedores['Localidad'].str.title()
df_proveedores['Direccion'] = df_proveedores['Direccion'].str.title()
df_proveedores['Nombre'] = df_proveedores['Nombre'].str.title()
#sucursales
df_sucursales['Sucursal'] = df_sucursales['Sucursal'].str.title()
df_sucursales['Direccion'] = df_sucursales['Direccion'].str.title()
df_sucursales['Localidad'] = df_sucursales['Localidad'].str.title()
df_sucursales['Provincia'] = df_sucursales['Provincia'].str.title()

#cliente
df_cliente['Nombre_y_Apellido'] = df_cliente['Nombre_y_Apellido'].str.title()
df_cliente['Domicilio'] = df_cliente['Domicilio'].str.title()
df_cliente['Localidad'] = df_cliente['Localidad'].str.title()


#localidades
df_localidades['Provincia'] = df_localidades['Provincia'].str.title()
df_localidades['Municipio'] = df_localidades['Municipio'].str.title()
df_localidades['Departameno'] = df_localidades['Provincia'].str.title()

print(df_localidades)


#for i in (df_venta['IdProducto'].unique()):
# print(df_venta[df_venta['IdProducto'] == i][df_venta['Precio'] > df_venta[df_venta['IdProducto'] == i]['Precio'].mean() + 2*df_venta[df_venta['IdProducto'] == i]['Precio'].std()])


#df_venta["Outlier"] = np.where(df_venta["Precio"] > df_venta[df_venta['IdProducto'] == 42817]['Precio'].mean() + 2*df_venta[df_venta['IdProducto'] == 42817]['Precio'].std(), 1, 0)


for i in df_venta["IdProducto"].unique():
     df_venta["Outlier"] = np.where(df_venta["Precio"] > df_venta[df_venta['IdProducto'] == i ]['Precio'].mean() + 2*df_venta[df_venta['IdProducto'] == i ]['Precio'].std(), 0, 1)

df_venta["Precio2"] = df_venta["Precio"] * df_venta["Outlier"]


#se lleva a cabo lo mismo pero con Compra
print(df_compra[df_compra['IdProducto'] == 42833])

for i in df_venta["IdProducto"].unique():
    df_compra["Outlier"] = np.where(df_compra["Precio"] > (df_compra[df_compra['IdProducto'] == i ]['Precio'].mean() + 4*df_compra[df_compra['IdProducto'] == i ]['Precio'].std()), 0, 1)
    #print(df_compra[df_compra['IdProducto'] == 42833][df_compra['Precio'] > df_compra[df_compra['IdProducto'] == 42833]['Precio'].mean() + 2*df_compra[df_compra['IdProducto'] == 42833]['Precio'].std()])
print(df_compra.sum())

df_compra["Precio2"] = df_compra["Precio"] * df_compra["Outlier"]



Print("Limpieza y normalizacion de datos ejecutada correctamente")
'''

























