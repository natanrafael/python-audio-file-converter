from .interface import Strategy


class Context:
    def __init__(self, strategy: Strategy = None):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self) -> None:
        self._strategy.execute_concrete_strategy()
