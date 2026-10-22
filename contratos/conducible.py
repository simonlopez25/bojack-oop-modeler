from abc import ABC, abstractmethod

class Conducible(ABC):
    @abstractmethod
    def conducir(self):
        pass