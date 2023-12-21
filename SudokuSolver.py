# Trabalho 1 de PAA 
# Grupo: Lucas Antônio Nogueira Silva e Tayna Rios Espinosa

import numpy as np

def posicao_valida(matrix, num, lin, col):
    #calculando os numeros do quadrado 3x3
    quad = 3
    if(col == 3 or col == 4 or col == 5):   
        quad = 6
    elif(col == 6 or col == 7 or col == 8):
        quad = 9
    #verificando a linha e a coluna
    if num in matrix[lin] or num in matrix[:,col]:
        #verificando o quadrado
        return False
    #verificando as outras linhas antes da penultima
    if (lin == 0 or lin == 3 or lin == 6) and (num in matrix[lin][(quad-3):quad] or num in matrix[lin+1][(quad-3):quad] or num in matrix[lin+2][(quad-3):quad] ) :
        return False
    #verificando a penultima linha dos quadrados
    elif (lin == 1 or lin == 4 or lin == 7)  and (num in matrix[lin-1][(quad-3):quad] or num in matrix[lin][(quad-3):quad] or num in matrix[lin+1][(quad-3):quad] ) :
        return False
    #verificando a ultima linha dos quadrados
    elif (lin == 2 or lin == 5 or lin == 8) and (num in matrix[lin-2][(quad-3):quad] or num in matrix[lin-1][(quad-3):quad] or num in matrix[lin][(quad-3):quad] ) :
        return False
    
    return True

def sudoku_solver(matrix, lin, col):
    if (lin < 0 or col < 0) :
        return False
    if (lin > 8 or col > 8):
        return True
    if not (0 in matrix):
            return True
    
    num = 0
    #REPRESENTAR CANDIDATOS PARCIAIS
    while(num < 9):
        num += 1
        if matrix[lin][col] == 0:
            # ------- verificando os possiveis candidatos -----------
            if posicao_valida(matrix,num,lin,col):
                #colocando o candidato na matriz
                matrix[lin][col] = num
                #chamando recursivo a proxima posição da matriz
                if col < 8:
                    if sudoku_solver(matrix,lin,col+1):
                        return True
                else:
                    if sudoku_solver(matrix,lin+1,0):    
                        return True            
                # --------- se nao achar um numero valido na matriz, fazer backtrack -----------
                #colocando o numero da matriz de volta como zero
                matrix[lin][col] = 0
                continue

        # -------- se a posição ja estiver preenchida ir pra proxima casa -----------
        else:
            if col < 8:
                col += 1
            else:
                lin += 1
                col = 0
            num -= 1
            continue
    # -------------- nao foi encontrado uma candidato valido --------------
    return False

#função para verificar se a matrix de entrada é valida para jogar ou não
def validar_sudoku(matrix):
    for lin in range(9):
        for col in range(9):
            #verifica se encontra o mesmo número na linha, coluna ou no quadrante 3x3
            if matrix[lin][col] >= 1 and matrix[lin][col] <= 9:
                num = matrix[lin][col]
                matrix[lin][col] = 0
                
                #chama a função posicao_valida para verificar se eé valida a posição, se for retorna falso
                if not posicao_valida(matrix, num, lin, col):
                    return False
                
                matrix[lin][col] = num

    return True

#função para imprimir o sudoko editado bonitinho 
def print_matrix(matrix):
    for lin in range(9):
        for col in range (9):
            
            if col == 3 or col == 6:
                print(" |", end='')

            print(f' {matrix[lin][col]}', end='')

        print("\n", end='')

        if lin == 2 or lin == 5:
            print("-" * 7 + "|" + "-" * 7 + "|" + "-" * 7)

if __name__ == '__main__':
    exemplo = input("Digite o exemplo que deseja resolver (exemplo: s01a.txt): ")

    matrix = []
    #abrindo o arquivo 
    with open('exemplos/' + exemplo, 'r') as arquivo:
        for linha in arquivo:
            #removendo todos os espaços brancos e divide as linhas nos elementos de acordo com os espaços em branco
            elementos = linha.strip().split()  

            #convertendo os elemntos em inteiros 
            linha_convertida = [int(elemento) for elemento in elementos] 

            #adicionando a linha convertida na matrix
            matrix.append(linha_convertida)

    matrix = np.array(matrix)

    print("O Sudoku não resolvido: ")
    print_matrix(matrix)

    print("-" * 23)

    if validar_sudoku(matrix):
        a = sudoku_solver(matrix, 0, 0)
        if a:
            print("O Sudoku resolvido: ")
            print_matrix(matrix)
        else:
            print("Não foi possível encontrar uma solução.")
    else:
        print("Matriz Invalida")
        