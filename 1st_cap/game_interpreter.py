import re 
# >>>>>>>>>>>>>>> linguagem <<<<<<<<<<<<<<<<<<<<
#   >>>>>>>>>>>>> estrutura <<<<<<<<<<<<<<<<<<<<
#   (condicao,true_acao,false_acao)
#   ex:
#       (life<10, defense, attack)

life_condicao = re.compile(r'life<(?P<life>\d+)')
condicoes = {
    r"life<\d+" : {
        'eval' : lambda life_ : lambda life : life < life_,
        'pattern' : life_condicao
        }
}

def busca_condicao(condicao):
    for pattern, eval_ in ((condicoes[x]['pattern'], condicoes[x]['eval']) for x in condicoes.keys()):
        m = pattern.match(condicao)
        if m:
            return eval_(int(m.group('life')))
    
all_condicoes = '|'.join(condicoes.keys())
commands = {
    "attack" : lambda : "atacou", 
    "defense" : lambda : "defendeu",
}
all_commands = '|'.join(commands.keys())


# separando os comandos
c = re.compile(r'[(](%s),(%s),(%s)[)](?m)' % (all_condicoes, all_commands, all_commands))


if __name__ == '__main__':
    commands_string = raw_input()
    life = 18
    while commands_string != "exit":
        commands_list = c.findall(commands_string)
        for condicao, true_acao, false_acao in commands_list:
            if busca_condicao(condicao)(life):
                print(commands[true_acao]())
            else:
                print(commands[false_acao]())
        commands_string = raw_input()
