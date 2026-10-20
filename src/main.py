from triangleDB import TriangleDB
from userInteraction import ConsoleUserInteraction
from notifier import NotificationServiceStub
from controller import Controller

def main():
    db = TriangleDB('triangle.db')
    ui = ConsoleUserInteraction()
    notifier = NotificationServiceStub()

    controller = Controller(ui, db, notifier)

    try:
        result = controller.process()
        print(f"Результат: {result}")
    finally:
        db.close()

if __name__ == "__main__":
    main()