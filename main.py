import sys, time
from controllers.kombat_controller import  execute_rounds, who_starts
from controllers.input_controller import get_and_validate_input

def main():
  fight_json = {}

  try:
    if len(sys.argv) != 2:
      print("Uso: py main.py 'cadena_de_diccionario' o nombre de archivo,json")
      sys.exit(1)

    #Validar input
    fight_json = get_and_validate_input(sys.argv[1])

    print('\033[95mBienvenido a Talana Kombat')
    time.sleep(1.5)
    
    player1 = fight_json['player1']
    player2 = fight_json['player2']

    player1['name'] = 'Tony'
    player2['name'] = 'Arnaldor'

    #Calcula numero de rounds
    rounds = max(len(player1['movimientos']), len(player2['movimientos']))

    #Definir quien empieza
    starting_player = who_starts(player1, player2)

    player1['energy'] = 6
    player2['energy'] = 6

    print('El combate empezara en: 3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Fight!\n')
    time.sleep(1)

    # Llamar función para ejecutar combate
    execute_rounds(player1, player2, rounds) if starting_player == player1['name'] else execute_rounds(player2, player1, rounds)
  except Exception as e:
    print(e)
  
if __name__ == "__main__":
  main()
