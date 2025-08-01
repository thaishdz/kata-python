"""
Se te proporciona el punto de inicio inicial (x, y) de un rover y la dirección (N, S, E, W) 
en la que está orientado.
El rover recibe una matriz de caracteres con comandos.
Implementa comandos que muevan el rover hacia adelante/atrás (f, b).
Implementa comandos que giren el rover a la izquierda/derecha (l, r).

"""

class Rover:

    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.orientation = 'N'

    def process_commands(self,commands: list[str]): # F,R,F,F,L

        for command in commands:
            if command == 'F' or command == 'B':
                self.move(command)
            elif command == 'R' or command == 'L':
                self.rotate(command)
            else:
                raise "CommandNotFound"

    def move(self, movement: str): 
        if movement == 'F':
            self.position_y += 1
        elif movement == 'B':
            self.position_y -= 1
        
    def rotate(self,direction: str):

        if self.orientation == 'N' and direction == 'R':
            self.orientation = 'E'
            return 
        elif direction == 'L':
            self.orientation = 'W'
            return 

        if self.orientation == 'E' and direction == 'R':
            self.orientation = 'S'
            return
        elif direction == 'L':
            self.orientation = 'N'
            return
        if self.orientation == 'S' and direction == 'R':
            self.orientation = 'W'
            return
        elif direction == 'L':
            self.orientation = 'E'
            return
        if self.orientation == 'W' and direction == 'R':
            self.orientation = 'N'
            return
        elif direction == 'L':
            self.orientation = 'S'
            return



if __name__ == "__main__":
    Rover()
