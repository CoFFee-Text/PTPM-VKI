from triangle import Triangle

class Controller:
    def __init__(self, userInter, db, notifier):
        self.userInter = userInter
        self.db = db
        self.notifier = notifier

    def process(self):
        # ввод
        a = self.userInter.get_input("1-ая сторона: ")
        b = self.userInter.get_input("2-ая сторона: ")
        c = self.userInter.get_input("3-ая сторона: ")

        if a is None or b is None or c is None:
            self.userInter.show_result("Некорректный ввод")
            return "", [(-2, -2)] * 3

        # бдшка
        cached = self.db.get(a, b, c)
        if cached is not None:
            triangle_type, _ = cached
            triangle = Triangle(a, b, c)
            _, coordinates = triangle.calculate()
        else:
            triangle = Triangle(a, b, c)
            triangle_type, coordinates = triangle.calculate()
            self.db.add(a, b, c, triangle_type)

        self.notifier.send_result(triangle_type, coordinates)
        self.userInter.show_result(triangle_type, coordinates)

        return triangle_type, coordinates