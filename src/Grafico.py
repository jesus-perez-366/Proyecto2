import matplotlib.pyplot as plt

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