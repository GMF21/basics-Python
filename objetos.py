#(metodos e atributos)
#se quiser fazer a class noutro ficheiro tbm da so meter o nome do ficheiro com o nome da class de letra pequena e usar
#from ex:"car"(nome do ficheiro) import ex:Car(nome da classe)
class Car:
    def __init__(self, modelo, ano, cor):  #construtor
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


#print(car1.modelo)
#print(car1.ano)
#print(car2.modelo)
    
    def drive(self):
        print(f"conduzir {self.modelo}")
    
    def stop(self):
        print(f"paraste {self.modelo}")


if __name__ == "__main__":
    car1 = Car("Ferrari 458", 2014, "red" )
    car2 = Car("Lamborghini huracan", 2020, "preto")

    car1.drive()


    
        
