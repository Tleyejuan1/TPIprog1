
def convertir_libras_a_kilogramos(valor, tipo_conversion):
    if tipo_conversion == 1:  # Libras a kilogramos
        return valor * 0.453592  
    elif tipo_conversion == 2:  # Kilogramos a libras
        return valor / 0.453592  
    else:
        return "Opción de conversión inválida"


def convertir_pulgadas_a_centimetros(valor, tipo_conversion):
    if tipo_conversion == 1:  # Pulgadas a centímetros
        return valor * 2.54 
    elif tipo_conversion == 2:  # Centímetros a pulgadas
        return valor / 2.54  
    else:
        return "Opción de conversión inválida"


def convertir_pies_a_metros(valor, tipo_conversion):
    if tipo_conversion == 1:  # Pies a metros
        return valor * 0.3048  
    elif tipo_conversion == 2:  # Metros a pies
        return valor / 0.3048  
    else:
        return "Opción de conversión inválida"

def convertir_millas_a_kilometros(valor, tipo_conversion):
    if tipo_conversion == 1:  # Millas a kilómetros
        return valor * 1.60934  
    elif tipo_conversion == 2:  # Kilómetros a millas
        return valor / 1.60934  
    else:
        return "Opción de conversión inválida"

def convertir_fahrenheit_a_celsius(valor, tipo_conversion):
    if tipo_conversion == 1:  # Fahrenheit a Celsius
        return (valor - 32) * 5/9  
    elif tipo_conversion == 2:  # Celsius a Fahrenheit
        return (valor * 9/5) + 32  
    else:
        return "Opción de conversión inválida"

