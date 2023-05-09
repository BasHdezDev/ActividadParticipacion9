from typing import List, Tuple


class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, 'r', encoding='utf-8') as f:
            line_data =  f.read()

        def _direccion_viento_a_grados(self, direccion_viento: str) -> float:
            # Convertir dirección del viento a grados
            direccion_viento = direccion_viento.strip()
            if direccion_viento == 'N':
                return 0
            elif direccion_viento == 'NNE':
                return 22.5
            elif direccion_viento == 'NE':
                return 45
            elif direccion_viento == 'ENE':
                return 67.5
            elif direccion_viento == 'E':
                return 90
            elif direccion_viento == 'ESE':
                return 112.5
            elif direccion_viento == 'SE':
                return 135
            elif direccion_viento == 'SSE':
                return 157.5
            elif direccion_viento == 'S':
                return 180
            elif direccion_viento == 'SSW':
                return 202.5
            elif direccion_viento == 'SW':
                return 225
            elif direccion_viento == 'WSW':
                return 247.5
            elif direccion_viento == 'W':
                return 270
            elif direccion_viento == 'WNW':
                return 292.5
            elif direccion_viento == 'NW':
                return 315
            elif direccion_viento == 'NNW':
                return 337.5


        DatosMeteorologicos(r'C:\Users\Bas\PycharmProjects\ActividadParticipacion9\DatosMeteorologicos\datos_meteorologicos.txt')
