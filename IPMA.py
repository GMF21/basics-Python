import requests

def main():
    idArea = ""

    while idArea != "n":
        idArea = input("Área 3 - Açores | 7 - Portugal Continental (n - para sair): ")

        if idArea == "n":
            print("A sair...")
            break

        URL = f"https://api.ipma.pt/open-data/observation/seismic/{idArea}"
        respostas = requests.get(URL)

        if respostas.status_code == 200:
            dados = respostas.json()

            print(f"Owner: '{dados.get('owner')}'")
            print(f"Country: '{dados.get('country')}'")

            for sismo in dados.get("data"):
                print(f"Local: '{sismo['local']}'")
                print(f"Time: '{sismo['time']}'")
                print(f"Magnitude: '{sismo['magnitud']}'")
                print(f"Latitude: '{sismo['lat']}'")
                print(f"Longitude: '{sismo['lon']}'")
                print("------------------------------------")


if __name__ == '__main__':
    main()
