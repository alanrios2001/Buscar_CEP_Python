import requests
import json
import os

def get_info_cep(api):
    cep = requests.get(api)
    dict_cep = json.loads(cep.text)
    return dict_cep

def show_info_cep(dicionario,cep):
    print('-'*10,f'cep: {cep}','-'*10)
    print('endereço:', dicionario['address'])
    print('bairro: ', dicionario['district'])
    print('estado:', dicionario['state'])
    print('cidade: ', dicionario['city'])
    print('ddd:', dicionario['ddd'])

def pedir_cep():
    lista_url = list('https://cep.awesomeapi.com.br/json/')
    while True:
        cep = input('digite o cep que deseja buscar: ')
        if len(cep) == 8:
            for numero in cep:
                lista_url.append(numero)
            break
        else:
            print('cep invalido')
    url = ''.join(lista_url)
    return url,cep

def cep_main():
    i = 1
    while i > 0:
        j = 1
        url,cep = pedir_cep()
        try:
            show_info_cep(get_info_cep(url),cep)
        except:
            print('cep inexistente')
        
        while j > 0:
            opc = input('deseja fazer uma nova consulta?(s/n): ')
            if opc == 's':
                j = 0
                os.system('cls')
            elif opc == 'n':
                j = 0
                i = 0
            elif opc != 's' or opc != 'n':
                print('opcao invalida')

cep_main()