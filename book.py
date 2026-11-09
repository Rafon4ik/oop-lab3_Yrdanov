from datetime import datetime
import math

class Book:
    def __init__(self, title: str, author: str, year: int, pages: int, words_per_page: int = 300, reading_speed: int = 200):    # Добавляю атрибуты
        self.title = title
        self.author = author
        
        self.year = year    # Инициализация через сеттеры для проверки инвариантов
        self.pages = pages
        
        self.words_per_page = words_per_page
        self.reading_speed = reading_speed

    @property       # Добавляю свойства для соблюдения инвариантов
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.now().year
        if not isinstance(value, int) or not (1000 <= value <= current_year):
            raise ValueError(f"Год издания должен быть целым числом от 1000 до {current_year}. Получено: {value}")
        self._year = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"Количество страниц должно быть целым числом больше 0. Получено: {value}")
        self._pages = value

    def get_total_words(self) -> int:       # Добавляю методы
        """Вычисляет примерное общее количество слов в книге."""
        return self.pages * self.words_per_page

    def calculate_reading_time(self) -> dict:

        total_words = self.get_total_words()
        
        minutes = total_words / self.reading_speed      # Время в минутах = общее количество слов / скорость чтения
        hours = minutes / 60
        
        return {
            "minutes": round(minutes, 2),
            "hours": round(hours, 2)
        }

    def add_pages(self, amount: int):
        """Метод изменения состояния: добавление страниц (например, при обнаружении доп. главы)."""
        if amount <= 0:
            raise ValueError("Количество добавляемых страниц должно быть положительным.")
        # Используем сеттер для проверки инварианта
        self.pages = self.pages + amount

    def compare_reading_time(self, other_book: 'Book') -> str:
        if not isinstance(other_book, Book):
            raise TypeError("Ожидается объект класса Book")
        
        time_self = self.calculate_reading_time()["minutes"]
        time_other = other_book.calculate_reading_time()["minutes"]
        
        if time_self < time_other:
            return f"'{self.title}' читается быстрее, чем '{other_book.title}'."
        elif time_self > time_other:
            return f"'{other_book.title}' читается быстрее, чем '{self.title}'."
        else:
            return f"'{self.title}' и '{other_book.title}' читаются за одинаковое время."



    if __name__ == "__main__":      # Демонстрация кода
    print("--- Создание объектов ---")
    book1 = Book("Война и мир", "Л.Н. Толстой", 1869, 1300, words_per_page=400, reading_speed=150)
    book2 = Book("Маленький принц", "А. де Сент-Экзюпери", 1943, 96, words_per_page=200, reading_speed=250)

    print(book1)
    print(book2)
    print()

    print("--- Расчёт времени чтения (Вычислительная задача) ---")
    time1 = book1.calculate_reading_time()
    time2 = book2.calculate_reading_time()
    
    print(f"Время чтения '{book1.title}': {time1['hours']} ч. ({time1['minutes']} мин.)")
    print(f"Время чтения '{book2.title}': {time2['hours']} ч. ({time2['minutes']} мин.)")
    print()

    print("--- Взаимодействие объектов ---")
    print(book1.compare_reading_time(book2))
    print()

    print("--- Изменение состояния ---")
    book2.add_pages(20)
    print(f"После добавления 20 страниц во вторую книгу:")
    print(book2)
    print(f"Новое время чтения: {book2.calculate_reading_time()['hours']} ч.")
    print()

    print("--- Проверка инвариантов ---")
    try:
        book3 = Book("Неизвестная книга", "Неизвестный автор", 999, 100)
    except ValueError as e:
        print(f"Ошибка при создании (год): {e}")

    try:
        book3 = Book("Неизвестная книга", "Неизвестный автор", 2020, 0)
    except ValueError as e:
        print(f"Ошибка при создании (страницы): {e}")