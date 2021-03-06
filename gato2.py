# --------- Variables globales -----------


tablero = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# saber si el juego sigue
juego_continue = True


ganador = None


jugador_actual = "X"


# ------------- Funciones---------------

# jugar
def jugar_gato():

  # tablero inicial
  mostrar_tablero()

  # Loop hasta que pare el juego 
  while juego_continue:

    
    dar_turno(jugador_actual)

    
    revisar_si_acabo_juego()

    
    cambiar_jugador()
  
  # Si se acabo el juego decir ganador o empate
  if ganador == "X" or ganador == "O":
    print(ganador+ " Es el ganador")
  elif ganador == None:
    print("Empate")



def mostrar_tablero():
  print("\n")
  print(tablero[0] + " | " + tablero[1] + " | " + tablero[2] + "     1 | 2 | 3")
  print(tablero[3] + " | " + tablero[4] + " | " + tablero[5] + "     4 | 5 | 6")
  print(tablero[6] + " | " + tablero[7] + " | " + tablero[8] + "     7 | 8 | 9")
  print("\n")



def dar_turno(jugador):

  #posicion del jugador
  print("turno de " + jugador)
  posicion = input("Elige una posicion del 1-9: ")

  # asegurarse que sea una posicion valida
  valid = False
  while not valid:

    
    while posicion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      posicion = input("Elige una posicion del 1-9: ")
 
    # posicion en numeros tablero 
    posicion = int(posicion) - 1

    
    if tablero[posicion] == "-":
      valid = True
    else:
      print("Lugar ocupado, elige otro")

  
  tablero[posicion] = jugador

  
  mostrar_tablero()


def revisar_si_acabo_juego():
  revisar_ganador()
  revisar_empate()


#ganador
def revisar_ganador():
  
  global ganador
  
  ganador_fila = revisar_filas()
  ganador_columna = revisar_columnas()
  ganador_diagonal= revisar_diagonales()
  
  if ganador_fila:
    ganador = ganador_fila
  elif ganador_columna:
    ganador = ganador_columna
  elif ganador_diagonal:
    ganador = ganador_diagonal
  else:
    ganador = None



def revisar_filas():
  # Set global variables
  global juego_continue
  
  fila_1 = tablero[0] == tablero[1] == tablero[2] != "-"
  fila_2 = tablero[3] == tablero[4] == tablero[5] != "-"
  fila_3 = tablero[6] == tablero[7] == tablero[8] != "-"
  
  if fila_1 or fila_2 or fila_3:
    juego_continue = False
  
  if fila_1:
    return tablero[0] 
  elif fila_2:
    return tablero[3] 
  elif fila_3:
    return tablero[6] 
  
  else:
    return None



def revisar_columnas():
  
  global juego_continue
  
  columna_1 = tablero[0] == tablero[3] == tablero[6] != "-"
  columna_2 = tablero[1] == tablero[4] == tablero[7] != "-"
  columna_3 = tablero[2] == tablero[5] == tablero[8] != "-"
  
  if columna_1 or columna_2 or columna_3:
    juego_continue = False
  
  if columna_1:
    return tablero[0] 
  elif columna_2:
    return tablero[1] 
  elif columna_3:
    return tablero[2] 
  
  else:
    return None



def revisar_diagonales():
  
  global juego_continue
  
  diagonal_1 = tablero[0] == tablero[4] == tablero[8] != "-"
  diagonal_2 = tablero[2] == tablero[4] == tablero[6] != "-"
  
  if diagonal_1 or diagonal_2:
    juego_continue = False
  
  if diagonal_1:
    return tablero[0] 
  elif diagonal_2:
    return tablero[2]
  
  else:
    return None


# empate
def revisar_empate():
  
  global juego_continue
  
  if "-" not in tablero:
    juego_continue = False
    return True
  
  else:
    return False



def cambiar_jugador():

  global jugador_actual

  if jugador_actual == "X":
    jugador_actual = "O"

  elif jugador_actual == "O":
    jugador_actual = "X"


# empezar el juego
jugar_gato()
