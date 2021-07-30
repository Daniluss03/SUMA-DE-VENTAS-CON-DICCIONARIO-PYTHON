def suma_valores_dic(main_dic):
#creamos el diccionario donde se pasaran la suma de las ventas         
        dic_result = {}
#tomamos cada llave in el los items del diccionario y lo recorremos para despues sumarlo        
        for key, value in main_dic.items():
            suma = 0
            for v in value:
                suma += v
            dic_result[key] = suma
        return dic_result

#aca tomamos el diccionario con los valores de las n facturas  en los puntos y en la tienda virtual
facturas = {'tola_ventas_punto': [7670, 3455, 767, 767, 34, 767], 'total_ventas_virtual': [354353, 55435767]}
resultado = suma_valores_dic(facturas)
print(resultado)
