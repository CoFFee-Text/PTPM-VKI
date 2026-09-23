import logging
import sys
import triangle

# Шаблон строки лога (аналог template в Serilog)
# Содержит: время, уровень (до 7 символов для выравнивания), имя логгера и сообщение
log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Базовая настройка корневого логгера
logging.basicConfig(
    level=logging.DEBUG,  # Минимальный уровень логирования (аналог MinimumLevel.Debug)
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),  # Настройка логирования в консоль
        logging.FileHandler("logs/file_txt.log", encoding="utf-8")  # Настройка логирования в файл
    ]
)
logging.getLogger('matplotlib').setLevel(logging.WARNING)
logging.getLogger('PIL').setLevel(logging.WARNING)

def main():
    logging.info("Логгер успешно сконфигурирован")
    logging.info("Приложение запущено")

    try:
        a = triangle.check_input("1-ая сторона: ")
        b = triangle.check_input("2-ая сторона: ")
        c = triangle.check_input("3-ая сторона: ")

        if a is None or b is None or c is None:
            triangle_type = ""
            coordinates = [(-2, -2)] * 3
            logging.warning(f"Нечисловые данные: a={a}, b={b}, c={c}."f"Тип: '{triangle_type}', координаты вершин: {coordinates}")
            return triangle_type, coordinates

        triangle_type = triangle.check_triangle(a, b, c)
        logging.info(f"Тип треугольника: {triangle_type}")

        coordinates = triangle.vertices_coordinates(a, b, c)
        logging.info(f"Координаты вершин: {coordinates}")

        if triangle_type == "Не треугольник":
            logging.warning(f"Невалидные числовые данные: a={a}, b={b}, c={c}. "f"Тип: '{triangle_type}'. Координаты: {coordinates}")
            return triangle_type, coordinates

        triangle.draw_triangle(coordinates)
        return triangle_type, coordinates

    except Exception:
        logging.error("Что-то пошло не так")
        logging.exception("Заход в блок обработки исключения:")
        return

    #try:
    #     a = 10
    #     for b in range(0, 3):
    #         logging.info(f"Итерация b = {b}")
    #
    #         if b == 0:
    #             logging.warning("Внимание, переменная b инициализирована нулем!")
    #
    #         logging.debug(f"Выполнение деления {a} на {b}")
    #         result = a / b
    #         logging.info(f"Деление {a} на {b} равно {result}")
    #
    # except ZeroDivisionError as ex:
    #     # Метод logging.exception() автоматически прикрепляет traceback (стек ошибки)
    #     logging.error("Что-то пошло не так...")
    #     logging.exception("Заход в блок обработки исключения:")

if __name__ == "__main__":
    main()