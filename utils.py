import json

def validate_length(lst: list, max: int) -> bool:
  """
    Valida el numero de caracteres maximo permitido 
    que puede tener cada item de una lista

    Parameters
    ----------
      lst (list): lista con items a validar
      max (int): numero de caracteres permitidos

    Returns
    -------
      bool: valor booleano que indica si todos los 
      items cumplen con el maximo permitido o no

    :Authors:
      - Diego Valdes

    :Created:
      - 2024.03.13
  """
  return not any(len(item) > max for item in lst)

def validate_characters(lst: list) -> bool:
  """
    Valida los caracteres permitidos que puede tener cada item de una lista

    Parameters
    ----------
      lst (list): lista con items a validar

    Returns
    -------
      bool: valor booleano que indica si todos los items contienen 
      solo caracteres permitidos o no

    :Authors:
      - Diego Valdes

    :Created:
      - 2024.03.13
  """
  allowed_chars = {'D', 'W', 'S', 'A', 'P', 'K'}
  return all(set(item) <= allowed_chars for item in lst)

def str_to_dict(str_dict: str) -> dict:
  """
    Convierte un str a un dict

    Parameters
    ----------
      str_dict (str): str a convertir

    Returns
    -------
      dict: diccionario resultante de la conversion

    :Authors:
      - Diego Valdes

    :Created:
      - 2024.03.13
  """
  try:
    # Convertir la cadena de JSON a un diccionario
    dict_data = json.loads(str_dict)
    return dict_data
  except json.JSONDecodeError as e:
    print("Error al decodificar la cadena JSON:", e)
    return None

def get_dict_from_file(input: str) -> dict:
  """
    Obtiene contenido de un archivo .json y lo convierte en un
    diccionario

    Parameters
    ----------
      input (str): nombre de archivo

    Returns
    -------
      dict: diccionario resultante con el contenido del archivo

    :Authors:
      - Diego Valdes

    :Created:
      - 2024.03.13
  """
  with open(input) as f_in:
    return json.load(f_in)
