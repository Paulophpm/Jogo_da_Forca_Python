# Criando primeiro código POO
# autor: Paulo H

import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word: list, letter: str, status: int, erro: int, board: list):
        self.board = board #quadro do jogo
        self.status = status #Andamento do jogo
        self.word = word #Palavra utilizada
        self.erro = erro #Total de erros
        self.letter = letter #letra digitada


    # Método para adivinhar a letra
    def guess(self, letter, erro, word):
        self.erro = erro
        self.letter = letter
        self.word = word
        print(list(filter(lambda letra, word: letter in word )))
        for self.letter in self.word:
            if self.letter == 0:
                print(self.letter)
            else:
                self.erro += 1
                for self.erro in self.word:
                    print()


    # Método para verificar se o jogo terminou
    def hangman_over(self,erro):
        self.erro = erro
        while self.erro < 5:
            if self.erro == 4:
                print("Resta apenas 1 chute, pense bem!")
            elif self.erro == 3:
                print("Restam 2 chutes")
            break

    # Método para verificar se o jogador venceu
    def hangman_won(self, status):
        self.status = status
        if self.status == 0:
            

    # Método para não mostrar a letra no board
    def hide_word(self, board, erro):
        self.board = board
        self.erro = erro
        list(filter(lambda x : x ,range(board)))

        # filter


    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):



# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word(),)
    print('\nHello!!')
    print('\nWelcome to the game!')

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    if game.hangman_won():
    # continue

    # Verifica o status do jogo
    game.print_game_status()
    if game.hangman_over():
        print("Game Over")
            # continue

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print ('\nParabéns! Você venceu!!')
    else:
        print ('\nGame over! Você perdeu.')
        print ('A palavra era ' + game.word)

    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
    main()


