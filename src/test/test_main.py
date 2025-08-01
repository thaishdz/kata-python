import pytest

from src.main import Rover


def test_rover_init():
    rover = Rover()
    assert rover.position_x == 0
    assert rover.position_y == 0
    assert rover.orientation == 'N'

def test_proccess_commands():
    rover = Rover()
    commands = ['F','R','F','F','L']
    rover.process_commands(commands)
    assert rover.position_x == 2
    assert rover.position_y == 1
    assert rover.orientation == 'S'

def test_move_forward():
    rover = Rover()
    rover.move('F')
    assert rover.position_x == 0
    assert rover.position_y == 1
    assert rover.orientation == 'N'


def test_move_backward():
    rover = Rover()
    rover.move('B')

    assert rover.position_x == 0
    assert rover.position_y == -1
    assert rover.orientation == 'N'


def test_rotate_left():
    rover = Rover()
    rover.rotate('L')

    assert rover.orientation == 'W'


def test_rotate_right():
    rover = Rover()
    rover.rotate('R')

    assert rover.orientation == 'E'
