from abc import ABC, abstractmethod

class UserInteraction(ABC):
    @abstractmethod
    def get_input(self, userInput) -> float | None:
        pass

    @abstractmethod
    def show_result(self, triangle_type: str, coordinates: list) -> None:
        pass


class ConsoleUserInteraction(UserInteraction):
    def get_input(self, userInput) -> float | None:
        try:
            return float(input(userInput))
        except ValueError:
            return None

    def show_result(self, triangle_type, coordinates) -> None:
        print(f"Результат вычислений: тип: {triangle_type}, координаты: {coordinates}")