from typing import Tuple


class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, 'r', encoding='utf-8') as f:

            temperatura_total = 0
            humedad_total = 0
            presion_total = 0
            velocidad_total_viento = 0

            data = f.readlines()

            for linea in data:
                if linea.startswith("Estación"):
                    estacion = linea.split(':')

                elif linea.startswith("Latitud"):
                    latitud = linea.split(':')

                elif linea.startswith("Longitud"):
                    longitud = linea.split(':')

                elif linea.startswith("Fecha"):
                    fecha = linea.split(':')

                elif linea.startswith("Hora"):
                    hora = linea.split(':')

                elif linea.startswith("Temperatura"):
                    temperatura = linea.split(':')
                    temperatura_total += temperatura

                elif linea.startswith("Humedad"):
                    humedad = linea.split(':')
                    humedad_total += humedad

                elif linea.startswith("Presión"):
                    presion = linea.split(':')
                    presion_total += presion

                elif linea.startswith("Viento"):
                    viento = linea.split(':')
                    velocidad_total_viento += viento[0]

            print(data)


DatosMeteorologicos(r'C:\Users\Bas\PycharmProjects\ActividadParticipacion9\datos_meteorologicos.txt')
