from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute_concrete_strategy(self):
        pass
