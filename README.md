Iggy é uma interface via linha de comando que, recebe instruções e se move ao redor de um terreno.
Ela aceita os comandos:

- Place;
- move;
- left;
- right.

## Testando a Iggy
Para iniciar os testes e fazer a iggy andar, ela precisa receber primeiramente um comando, informando qual o local na tela ela estará posicionada:
'''
PLACE 0,0,SOUTH
'''
Onde PLACE é o comando que a Iggy reconhece ser de posicionamento e 0,0,SOUTH indica que a iggy eestará no mapa em x = 0, y = o com a orientação para o Sul.

Orientações válidas:
- SOUTH: Sul
- NORTH: Norte
- EAST: Leste
- WEAST: Oeste

E o comando MOVE, faz com que a iggy avance uma casa, de acordo com a orientação que ela está posicionada, e o comando REPORT, nos retorna qual o posicionamento da Iggy.
Input:
PLACE 1,2,EAST
MOVE
MOVE
RIGHT
MOVE
REPORT

OOutput:
3,3,SOUTH

## Setup
- Ter o python 3+ instalado
- Na pasta raiz do projeto, rodar o comando: python main.py
