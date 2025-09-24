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
                print(f"Local: '{sismo.get('local')}'")
                print(f"Time: '{sismo.get('time')}'")
                print(f"Magnitude: '{sismo.get('magnitud')}'")
                print(f"Latitude: '{sismo.get('lat')}'")
                print(f"Longitude: '{sismo.get('lon')}'")
                print("------------------------------------")


if __name__ == '__main__':
    main()
