from abc import ABC, abstractmethod
"""
abc significa Abstract Base Classes
(Clases Base Abstractas). Es un módulo de la biblioteca 
estándar de Python cuya función principal es permitir la creación
de contratos o interfaces estrictas.
"""
class Presentable(ABC):
    @abstractmethod
    def presentar(self):
        pass

