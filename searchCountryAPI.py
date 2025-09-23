import requests

# API de países - sempre funciona

pergunta = ""

while pergunta != "n":
    pergunta = str(input("Queres informações para algum pais? (s-sim/n-sair)"))

    if pergunta == "n":
        break
    else:

        pais = input("Nome do país: ")

        url = f"https://restcountries.com/v3.1/name/{pais}"
        resposta = requests.get(url)

        if resposta.status_code == 200: #codigo 200 (correu bem)
            dados = resposta.json() #dict convert de texto
            pais_info = dados[0] #pega as infos do unico pais da lista ou seja que nos encontramos
            
            print(f"País: {pais_info['name']['common']}")
            print(f"Capital: {pais_info.get('capital', ['N/A'])[0]}")
            print(f"População: {pais_info['population']:,}")
            print(f"Região: {pais_info['region']}")
            print(f"Moeda: {list(pais_info['currencies'].keys())[0]}")
        else:
            print("País não encontrado!") #404
