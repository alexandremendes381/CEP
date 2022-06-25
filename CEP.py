from time import sleep
import requests
import json
continuar = True
while continuar == True:
    sleep(0.3)
    print('\033[1;30m''BUSCADOR DE CEP''\033[m')
    array = ['address_type', 'address_name', 'address', 'state', 'district', 'city', 'ddd', ]

    def buscar_dados_id(buscador):
        request = requests.get("https://cep.awesomeapi.com.br/json/{}".format(buscador))
        todo = json.loads(request.content)

        for n in array:
            print(todo[n])
            sleep(0.2)

    if __name__ == '__main__':

        # buscar_dados()
        buscador = str(input('\033[1;33m''DIGITE O CEP ? ''\033[m'))

        i = 0
        while i < len(buscador):
             i = i + 1
        if i > 8:
            print('\033[1;31m''cep invalido maior que 8 numeros:''\033[m')
        elif i < 8:
            print('\033[1;31m''cep invalido menor que 8 numeros:''\033[m')
        else:
            buscar_dados_id(buscador)

        sleep(0.8)
        recebe = int(input('\033[1;30m''Deseja fazer uma busca novamente:''\033[m''\033[1;32m''\n 1 = (sim)''\033[m''\033[1;31m''\n 2 = (não)''\033[m''\n''\033[1;30m''Qual das opções ? ''\033[m'))
        if recebe == 1:
            sleep(0.5)
            continuar = True
            print('\033[1;32m''ok iremos reiniciar nosso sistema''\033[m')
        if recebe == 2:
            sleep(0.5)
            continuar = False
            print('\033[1;31m''OK, muito obrigado por usar o nosso sitema nos agradecemos!!''\033[m')

