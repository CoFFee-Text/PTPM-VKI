from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_result(self, triangle_type: str, coordinates: list[tuple[int, int]]):
        pass


class NotificationServiceStub(NotificationService):
    def send_result(self, triangle_type, coordinates):
        print(f"Отправка результата вычислений: Тип: {triangle_type}, координаты: {coordinates}")