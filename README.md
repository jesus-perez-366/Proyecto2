# <img src=imagen/Tiburon2.jpg width="1000"> 
# Limpieza de un Archivo CSV    


## Explicación
   Este proyecto esta enfocado en realizar la limpieza de un archivo .csv

## Pasos a realizar
1. En primera instancia se debe visualizar el archivo .csv y realizar una exploración de datos de forma global.
2. Los archivos .cvs pueden contener gran extensión de datos por ellos es importante en la manera de lo posible delimitar la busqueda, para asi extraer la información que realmente se requiere y a partir de esa información trabajar sobre ella.
3. Platear los métodos a aplicar para estructurar la información.
4. Implementar y ejectutar las acciones para obtener una Data limpia y organizada.
5. Realizar los análisis a través de gráficos para representar la información lo más breve, estructurada y exacta para su entendimiento.

## Código para Limpieza
En función de los pasos a seguir para limpiar la data del archivo attacks.csv se implementarón filtros, intercambio de columnas, busqueda de patrones y remplazo de string determinados.

*Vista preliminar de la data Original*

<img src=imagen/data_original.jpg width="650">



A manera de resumen, para de limitar la información se planteó una hipótesis y a partir de ella se extrajo la infomración necesaria y se organizó la data para poder analizarla. Los códigos aplicados relevantes para este trabajo fueron.

A) Filtrar la información entre los años 1990 y 1999.
```

df_data_Content_Year=df_data_Content[(df_data_Content.Year >= 1990) & (df_data_Content.Year <= 1999)]

```

B) Verificación se si alguna información estaba duplicada.

```
df_data_Content_Year["Original Order"].duplicated().sum()

```
`Lo que se hizo fue verificar si los valores de la columna Original Orden se repetia en la misma columna, si la suma da 0 significa que no coincidencia, en caso contrario si habria, y por lo tanto habria que verificar si la demas informacion coincidia.`

C) Busqueda de patrones

```
patron=[r'\(.*\)', r'^\w.*\.$', r'\d.*\.?', r'^\w.*\:', r'^\w.\w$', r'^[a-z].*[a-z]$', r'[A-Z]\W$', r'^[A-Z]\s.*\w$', r'^\w.*\”$']
for i in patron:
        df_data_clean.Name=df_data_clean.Name.replace(regex=i, value= '')
df_data_clean.Name=df_data_clean.Name.replace(["female", "male", '', ' '], "Sin Identificar")

```
        
`Se crearon diversos patrones que permitieron limpiar la columna Name y asi obtener solo nombres o la expresion Sin Identificar`

Nota: este mismo proceso se aplicó para la columna Area

Al finalizar la limpieza se obtuvo una data de la siguiente manera:

*Data Arreglada*

<img src=imagen/data_arreglado.jpg width="650">

    

## Códigos para Análisis

Para verificar la hipótesis planteada se realizarón varios gráficos de barra y para ello se usaron solo 2 códigos.

Código A
```
df_Country_Area_Attacke_more_10.plot(kind='bar', color=['red','blue','orange','black','silver'])
```

Código B
```
sns.countplot(df_USA.Area, hue=df_USA.Sex)
```

Para darle un título y etiquetas a los ejes de cada gráfico se implementó el siguiente codigo, el cual fue definido como una función para asi evitar repetir el código en cada gráfico.

```
def etiquetas(x,y,z,n):
    '''
    Pertime darle un formato a la graficas (Titulo y tamaño, etiqueta a los ejes, tamño del grafico)
    args:
    x (String) = Es el titulo del grafico
    y (String) = Es la etiqueta del eje x
    z (String) = Es la etiqueta del eje y
    n (int) = Tamaño de la letra del titulo
    Return:
    none
    '''
    plt.suptitle(x, size=n)
    plt.xlabel(y)
    plt.ylabel(z)
    plt.figure(figsize=(12,5))

```
Los gráficos permitieron determinar que la hipótesis era falsa ya que uno de los argumentos no se cumplia.

Imagen del Código A
<img src=imagen/Codigo_A.jpg width="500">

Imagen del Código B
<img src=imagen/Codigo_B.jpg width="600">
