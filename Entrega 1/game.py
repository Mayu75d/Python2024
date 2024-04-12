import random

# Lista de palabras posibles

words = ["python", "programacion", "computadora", "codigo", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar

secret_word = random.choice(words)

# Número máximo de intentos permitidos

fails = 0
max_fails = 10
# Lista para almacenar las letras adivinadas

guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")

dificulty = int(input('''Seleccione la dificultad
1.FACIL
2.MEDIA
3.DIFICIL

 -> '''))


print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

word_displayed  = ""

match dificulty:
    case 1:
        for i in secret_word:
            if i  in "aeiou":
                word_displayed += i
            else:
                word_displayed += "_"   
    case 2:
        word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
    case 3:
        word_displayed = "_" * len(secret_word)
                                    

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")


while(fails < max_fails):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    #si el usario no pone nada informa un ERROR
    if(letter == ""):
        print('ERROR, no ha ingresado ninguna letra')
        continue

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta

    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fails += 1
    
    match dificulty:
        case 1:
            # Mostrar la palabra parcialmente adivinada
            letters = []

            guessed_letters += "a", "e", "i", "o", "u" 

            for letter in secret_word:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            word_displayed = "".join(letters)


            print(f"Palabra: {word_displayed}")   
            # Verificar si se ha adivinado la palabra completa
            if word_displayed == secret_word:
                print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
                break
        case 2:
            # Mostrar la palabra parcialmente adivinada
            letters = []

            word_displayed = secret_word[0]
            for letter in secret_word[1:-1]:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            word_displayed += "".join(letters)
            word_displayed += secret_word[-1]
            print(f"Palabra: {word_displayed}")
            # Verificar si se ha adivinado la palabra completa
            if word_displayed == secret_word:
                print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
                break
        case 3:
            # Mostrar la palabra parcialmente adivinada
            letters = []

            for letter in secret_word:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            word_displayed = "".join(letters)
            print(f"Palabra: {word_displayed}")
            # Verificar si se ha adivinado la palabra completa
            if word_displayed == secret_word:
                print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
                break
else:
    print(f"¡Oh no! Has fallado {max_fails} veces superando el limite de fallos permitidos")
    print(f"La palabra secreta era: {secret_word}")