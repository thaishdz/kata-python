"""
Se te proporciona el punto de inicio inicial (x, y) de un rover y la dirección (N, S, E, W) 
en la que está orientado.
El rover recibe una matriz de caracteres con comandos.
Implementa comandos que muevan el rover hacia adelante/atrás (f, b).
Implementa comandos que giren el rover a la izquierda/derecha (l, r).

"""

class Rover:

    """
    Omití un detalle importate y es que la kata dice "Se te proporciona el punto de inicio inicial (x, y) de un rover y la dirección (N, S, E, W) en la que está orientado." 
    Lo he corregido haciendo que ahora, al instanciar el Rover tome estos parámetros iniciales.
    """
    def __init__(self, initial_x: int, initial_y:int, orientation: str):
        self.position_x = initial_x
        self.position_y = initial_y
        self.orientation = orientation

    def process_commands(self,commands: list[str]): # F,R,F,F,L

        for command in commands:
            if command in ('F', 'B'): # Esto es lo que había pensado :p
                self.move(command)
            elif command in ('R', 'L'):
                self.rotate(command)
            else:
                raise ValueError(f"Comando no válido: {command}")

    def move(self, movement: str): 
        # La idea del diccionario que tenía, al final si el patrón de movimiento es de +1 o -1 se pueden 
        # definir coordenadas exactas para cada orientación y ejecutar el movimiento hacia arriba o abajo
        # en función de las coord (x,y)

        moves = {
            'N' : {'F': (0,1), 'B': (0,-1)},
            'E' : {'F': (1,0), 'B': (-1,0)},
            'S' : {'F': (0,-1), 'B': (0,1)},
            'W' : {'F': (-1,0), 'B': (1,0)},
        }

        # este punto es con el que estaba lidiando, quiero saber la orientación en la que está el rover
        # ahora mismo, accediendo al diccionario me ubico y le paso el movimiento, 
        # haciendo un destructuring de la tupla 
        coord_x, coord_y = moves[self.orientation][movement]

        self.position_x += coord_x
        self.position_y += coord_y


        
    def rotate(self,direction: str):

        # Siguiendo la misma lógica:

        directions = {
            'N' : {'L': 'W', 'R': 'E'},
            'E' : {'L': 'N', 'R': 'S'},
            'S' : {'L': 'E', 'R': 'W'},
            'W' : {'L': 'S', 'R': 'N'},
        }

        rotate_to_direction = directions[self.orientation][direction]
        self.orientation = rotate_to_direction


if __name__ == "__main__":
    Rover()
