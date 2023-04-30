import Animal
class SemiAcuatico(Animal):
    def __init__(self, idAnimal: int, edad: int, tipoH: int, tipoHabi: str, nombreEspecie: str, nombre: str,tipoDieta: int, horasD: int):
        super().__init__(idAnimal, edad, tipoH, tipoHabi, nombreEspecie, nombre, tipoDieta, horasD)
        self._adaptacion = "Semi Acuatico"
        self._idAdaptacion = 3

    def getTipoAdapA(self):
        super().getTipoAdapA()
        return self._idAdaptacion

    def getTipoAdapA_str(self):
        super().getTipoAdapA_str()
        return self._idAdaptacion

    def jugar(self):
        super().jugar()
        if self._boolJuego == False:
            self._boolJuego = True
            return "Esta entrando y saliendo del estanque, muy animado."
        else:
            self._boolJuego = False
            return "Esta reposando en medio del agua y la tierra."

    def comer(self):
        super().comer()