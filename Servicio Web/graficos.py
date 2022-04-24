from turtle import width
import pygal
from datetime import datetime
from conexion_insertar import Transacciones

def grafico_precios(nombre_moneda, simbolo , fecha, precios, prediccion ):
    #Graficas con pygal 
    #Definimos un grafico de linea, a este le pasamos la altura x el ancho y la asignación de la leyenda | para este caso la leyenda queda en la parte inferior cemtrada
    line_chart = pygal.Line(width = 600, height = 280, legend_at_bottom=True)
    
    #Titulo del grafico    - - - - #EURO \u20ac
    line_chart.title = f'PRECIO ACTUAL DEL {nombre_moneda.upper()} {simbolo}{precios[-1]} - LA PREDICCIÓN ESTA EN: {simbolo}{prediccion[-1]}'
    
    #Asignación de la etiqueta de X (para este caso son las fechas)
    line_chart.x_labels = fecha
    
    #Agregando las variables a graficar (para este caso si se desea rellenar el area que cubre el punto)
    line_chart.add(f'Precio del {nombre_moneda}', precios) #, fill = True)
    line_chart.add(f'Prediccion del {nombre_moneda}', prediccion)#, fill = True)
    
    #Asignando un grafico vectorial que sera guardado como Tiempo.svg
    #line_chart.render_to_file(f'static/images/{nombre_moneda}.svg')
    grafica = line_chart.render_data_uri()
    return grafica
    #line_chart.render_to_file(f'static/images/{nombre_moneda}.svg')
    


if __name__ == '__main__':
    precios_btc, fechas_btc, prediccion_btc = Transacciones.seleccionar_btc()

    precios_usd, fechas_usd, prediccion_usd = Transacciones.seleccionar_usd()

    precios_eur, fechas_eur, prediccion_euro = Transacciones.seleccionar_eur()

    graf_btc = grafico_precios('Bitcoin', '\u20bf', fechas_btc, precios_btc, prediccion_btc)

    graf_usd = grafico_precios('Dolar', '\u0024', fechas_usd, precios_usd, prediccion_usd)

    graf_eur = grafico_precios('Euro', '\u20ac', fechas_eur, precios_eur, prediccion_euro)
    print(graf_eur)
    





#GRAFICANDO CON BOKEH
'''  
import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show
def datetime(x):
    return np.array(x, dtype=np.datetime64)

p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'

p1.line(datetime(fechas_usd), prediccion_euro, color='#A6CEE3', legend_label='PREDICCION')
p1.line(datetime(fechas_usd), precios_eur, color='#B2DF8A', legend_label='PRECIO EURO')
p1.legend.location = "top_left"

show(gridplot([[p1]], width=800, height=800))  # open a browser
'''