import json
from utils import get_dict_from_file, str_to_dict, validate_length, validate_characters

def get_and_validate_input(input: str) -> dict:
  data = {}

  try:
    if input.find('.json') >= 0:
      #Data desde un archivo .json
      data = get_dict_from_file(input)
    else:
      data = str_to_dict(input)
    
    if not validate_length(data['player1']['movimientos'], 5) or not validate_length(data['player2']['movimientos'], 5): 
      raise TypeError('Número maximo de movimientos excedido, maximo 5 por movimiento.')
    if not validate_length(data['player1']['golpes'], 1) or not validate_length(data['player2']['golpes'], 1): 
      raise TypeError('Número maximo de golpes excedido, maximo 1.')
    if not validate_characters(data['player1']['movimientos']) or not validate_characters(data['player1']['golpes']):
      raise TypeError('Caracteres invalidos registrados en los movimientos del jugador 1')
    if not validate_characters(data['player2']['movimientos']) or not validate_characters(data['player2']['golpes']):
      raise TypeError('Caracteres invalidos registrados en los movimientos del jugador 2')
      
    return {
      "player1": {
        "movimientos": data['player1']['movimientos'], 
        "golpes": data['player1']['golpes']
      },
      "player2": {
        "movimientos": data['player2']['movimientos'], 
        "golpes": data['player2']['golpes']
      }
    }
  except Exception as e:
    print(e)
    raise TypeError('Ocurrio algo mal. Revise el formato de los datos ingresados.')
