from typing import List, Tuple


class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, 'r', encoding='utf-8') as f:

            temperatura_total = 0
            humedad_total = 0
            presion_total = 0
            velocidad_total_viento = 0

            for linea in f:
                if linea.startswith("Estación"):
                    estacion = linea.split(':')
                    print(estacion)

                elif linea.startswith("Latitud"):
                    latitud = linea.split(':')
                    print(latitud)

                elif linea.startswith("Longitud"):
                    longitud = linea.split(':')
                    print(longitud)

                elif linea.startswith("Fecha"):
                    fecha = linea.split(':')
                    print(fecha)

                elif linea.startswith("Hora"):
                    hora = linea.split(':')
                    print(hora)

                elif linea.startswith("Temperatura"):
                    temperatura = linea.split(':')
                    temperatura_total += temperatura
                    print(temperatura_total)

                elif linea.startswith("Humedad"):
                    humedad = linea.split(':')
                    humedad_total += humedad
                    print(humedad_total)

                elif linea.startswith("Presión"):
                    presion = linea.split(':')
                    presion_total += presion
                    print(presion_total)

                elif linea.startswith("Viento"):
                    viento = linea.split(':')
                    velocidad_total_viento += viento[0]
                    print(velocidad_total_viento)

        DatosMeteorologicos(r'C:\Users\Bas\PycharmProjects\ActividadParticipacion9\DatosMeteorologicos\datos_meteorologicos.txt')
