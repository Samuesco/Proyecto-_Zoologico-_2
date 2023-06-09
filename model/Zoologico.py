

import model.Habitat
import model.Animal
import streamlit as st

class Zoologico:
    def __init__(self,nombre:str):
        self.__nombreZ = nombre
        self._mapaHabitats: dict[int,model.Habitat] = {}
        self.__bodegaA: list[model.Animal] = []
        self.__totalH = 0
        self.__totalA = 0
        self.__creadorKeys = 1
        self.__creadorIds = 1
    def getNombre(self):
        return self.__nombreZ
    def getCreadorId(self):
        return self.__creadorIds
    def modiCreadorId(self):
        self.__creadorIds +=1

    def getCreadorKeys(self):
        return self.__creadorKeys
    def modiCreadorKey(self):
        self.__creadorKeys+=1

    def getTotalAZoo(self):
        return self.__totalA

    def setTotalAZoo(self, accion:int):
        if accion == 1:
            self.__totalA +=1
        else:
            self.__totalA-=1

    def getTotalHZoo(self):
        return self.__totalH
    def getMapa(self):
        return self._mapaHabitats
    def getBodega(self):
        return self.__bodegaA

    def setTotalHZoo(self, accion: int):
        if accion == 1:
            self.__totalH +=1
        else:
            self.__totalH -=1
    def agregarHabitat(self, newHabitat:model.Habitat):
        try:
            self._mapaHabitats[self.getCreadorKeys()] = newHabitat
            if self.getCreadorKeys() in self._mapaHabitats == False:
                raise IndexError("Fallo Ingreso en diccionario")
            else:
                self.modiCreadorKey()
                self.setTotalHZoo(1)
                return 1 # si el proceso salio bien

        except IndexError as e:
            return e.args # si el proceso falla

    def eliminarHabitat(self, keyBusqueda:int):
        res = keyBusqueda in self._mapaHabitats
        if res == True:
            temHabitat: model.Habitat.Habitat = self._mapaHabitats[keyBusqueda]
            if temHabitat.getCantidadAH() == 0:
                del self._mapaHabitats[keyBusqueda]
                self.setTotalHZoo(-1)
                return 1 # Encontro Habitat y esta vacio eliminación, se llevo a cabo la eliminacion
            else:
                return "Hay Animales en el Habitat.\nNo Es Posible Eliminar"
        else:
            return "No se encontro el habitat en el Zoologico"
    def agregarAnimalBodega(self, newAnimal: model.Animal.Animal):
        tamAnte = len(self.__bodegaA)
        self.__bodegaA.append(newAnimal)
        if tamAnte < len(self.__bodegaA):
            if self.__bodegaA[tamAnte] == newAnimal:
                self.setTotalAZoo(1)
                return 1
            else:
               return "Ingreso Invalido no se guardo el correcto"
        else:
             return "No se Agrego correctamente"
    def animalEnBodega(self,idA):
        indice = 0
        tamBodega = len(self.__bodegaA)
        if tamBodega > 0:
            ban = False
            while indice < tamBodega and ban == False:
                temAnimal = self.__bodegaA[indice]
                if temAnimal.getIdAnimal() == idA:
                    ban = True
                    return indice
                else:
                    indice+=1
            if ban == False:
                return "No se encontro Animal en la Bodega"
        else:
            return "No Hay animales en la Bodega"
    def sacarAnimalBodega(self, idAnimal:int):
        indice = self.animalEnBodega(idAnimal)
        if indice >=0:
            guardaA:model.Animal.Animal = self.__bodegaA[indice]
            self.__bodegaA.pop(indice)
            return guardaA
        else:
            return indice
    def eliminarAnimalBodega(self, idAnimal: int):
        indice = self.animalEnBodega(idAnimal)
        ban = None
        if indice>=0:
            try:
                del self.__bodegaA[indice]
                if type(self.animalEnBodega(idAnimal)) == str:
                    self.setTotalAZoo(-1)
                    # procesoExitoso
                    return 1
                else:
                    raise SystemError("Eliminar en Bodega")

            except SystemError as e:
                ban =  e.args # retorna el error
        else:
            ban = indice
        return ban
    def agregarAnimalH(self, animalB : model.Animal.Animal , idHabitat : int):
        banHabitat = idHabitat in self._mapaHabitats
        banGeneral = 0
        if banHabitat:
            banIngreso = self._mapaHabitats[idHabitat].agregarAnimalH(animalB)
            if banIngreso == 1:
                banGeneral = 1
            else:
                banGeneral = banIngreso
        else:
            banGeneral = "Habitat De llegada no encontrado"
        return banGeneral
    def retornarAnimalBodega(self, indA:int):
        return self.__bodegaA[indA]













