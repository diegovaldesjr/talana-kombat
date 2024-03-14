import time
from functools import reduce

def who_starts(player1: list, player2: list) -> str:
  """
    Evalua que jugador empezara el combate.

    Parameters
    ----------
      player1 (str): datos del player 1
      player2 (str): datos del player 2
      
    Returns
    -------
      str: nombre del jugador que comenzara el combate

    :Authors:
      - Diego Valdes

    :Created:
      - 2024.03.13
  """
  #Movimientos
  player1_moves = len(reduce(lambda a,b: a+b, player1['movimientos']))
  player2_moves = len(reduce(lambda a,b: a+b, player2['movimientos']))
  
  #Golpes
  player1_hits = len(reduce(lambda a,b: a+b, player1['golpes']))
  player2_hits = len(reduce(lambda a,b: a+b, player2['golpes']))
  
  #Combinacion de botones
  player1_combination = player1_moves + player1_hits
  player2_combination = player2_moves + player2_hits
     
  if player1_combination != player2_combination:
    return player1['name'] if player1_combination < player2_combination else player2['name']
  
  if player1_moves != player2_moves:
    return player1['name'] if player1_moves < player2_moves else player2['name']
  
  if player1_hits != player2_hits:
    return player1['name'] if player1_hits < player2_hits else player2['name']

  return player1['name']

def validate_play_and_damage(moves: str, hit: str, player_name: str) -> dict:
  """
    Valida los movimientos, golpes y daño realizados por el jugador

    Parameters
    ----------
      moves (str): movimientos del jugador
      hit (str): golpe del jugador
      player_name (str): nombre del jugador
      
    Returns
    -------
      dict: diccionario con movimientos no correspondientes a combinacion con
      golpe, daño y nombre del golpe

    :Authors:
      - Diego Valdes

    :Created:
      - 2024.03.13
  """
  if hit == '': 
    return {
      'moves': moves,
      'damage': 0,
      'name_move': None
    }
  
  special_moves = {
    'Tony': [
      {
        'combination': 'DSDP',
        'name_move': 'Taladoken',
        'damage': 3
      },
      {
        'combination': 'SDK',
        'name_move': 'Remuyuken',
        'damage': 2
      }
    ],
    'Arnaldor': [
      {
        'combination': 'SAK',
        'name_move': 'Remuyuken',
        'damage': 3
      },
      {
        'combination': 'ASAP',
        'name_move': 'Taladoken',
        'damage': 2
      }
    ],
  }

  move = moves.upper() + hit.upper()
  
  for special_move in special_moves[player_name]:
    if move.find(special_move['combination']) >= 0:
      return {
        'moves': move.replace(special_move['combination'], ''),
        'damage': special_move['damage'],
        'name_move': special_move['name_move']
      }
  
  return {
    'moves': moves,
    'damage': 1,
    'name_move': 'puñetazo' if hit == 'P' else 'patada'
  }

def generate_narration_of_the_movement(moves: str, name_move: str, player_name: str) -> str:
  """
    Genera la narrativa del movimiento realizado por el jugador.

    Parameters
    ----------
      moves (str): movimientos realizados por el jugador
      name_move (str): nombre del movimiento de daño del jugador
      player_name (str): nombre del jugador

    Returns
    -------
      str: cadena de caracteres con la narrativa

    :Authors:
      - Diego Valdes

    :Created:
      - 2024.03.13
  """
  color_text = '\033[91m' if player_name == 'Tony' else '\033[94m'
  move_narration = ''
  hit_narration = {
    'taladoken': 'usa un Taladoken',
    'remuyuken': 'conecta un Remuyuken',
    'puñetazo': 'da un puñetazo',
    'patada': 'da una patada'
  }

  if moves: 
    move_narration = 'se mueve'
    if (player_name == 'Tony' and moves.find('D') >= 0) or (player_name == 'Arnaldor' and moves.find('A') >=0): move_narration = 'avanza'

  narration = f'{color_text}{player_name} {move_narration if move_narration else ''}{' y' if move_narration and name_move else ''} {hit_narration[name_move.lower()] if name_move else ''}'
  return narration.replace('  ', ' ').strip()

def execute_rounds(first_player: dict, second_player: dict, rounds: int) -> None:
  """
    Ejecuta los rounds del combate

    Parameters
    ----------
      first_player (dict): diccionario con datos del jugador que comienza
      second_player (dict): diccionario con datos del jugador que juega de segundo
      rounds (int): numero de rounds

    Returns
    -------

    :Authors:
      - Diego Valdes

    :Created:
      - 2024.03.13
  """
  i = 0
  fight_comments = []
  round = 0
  color_text_win = '\033[93m'

  #Ciclo por turno
  while(i < rounds*2):
    player_in_turn = second_player if i%2 else first_player
    opponent = first_player if player_in_turn['name'] != first_player['name'] else second_player
    
    #Validar jugada
    play = validate_play_and_damage(player_in_turn['movimientos'][round], player_in_turn['golpes'][round], player_in_turn['name'])

    #Generar relato
    fight_comments.append(generate_narration_of_the_movement(play['moves'], play['name_move'], player_in_turn['name']))
    print(fight_comments[-1])
    time.sleep(1)

    if opponent['energy'] - play['damage'] <= 0: 
      fight_comments.append(f'{color_text_win}{player_in_turn['name']} Gana la pelea y aun le queda {player_in_turn['energy']} de energía')
      print(fight_comments[-1])
      break
    
    if play['damage'] > 0: opponent['energy'] -=play['damage']

    if i%2: round+=1
    i+= 1
  return
