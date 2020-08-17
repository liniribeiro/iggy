from src.planet import Mars

print("***Iniciando Iggy**")
print("***Insira seus comandos separados por enter**")
print("***Exemplo: \n>>>PLACE 0,0,SOUTH \n>>>LEFT \n>>>REPORT")
print("Digite seu primeiro comando:")


def start_app():
    has_element = True
    mars = Mars()
    can_move = False
    while has_element:
        user_input = input()
        command_list = user_input.split(" ")
        major_command = command_list[0].lower()
        if major_command == 'place':
            mars.change_mars_robbot_position(command_list[1])
            can_move = True
        elif major_command in ['left', 'right', 'move'] and can_move:
            mars.move(major_command)
        elif major_command == 'report':
            print(mars.robbot_report())
        elif not can_move:
            print("Iggy apenas pode se movimentar, se for posicionada no chão!")

        elif major_command == 'exit':
            has_element = False


start_app()
