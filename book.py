from datetime import datetime
import math

class Book:
    def __init__(self, title: str, author: str, year: int, pages: int, words_per_page: int = 300, reading_speed: int = 200):
        self.title = title
        self.author = author
        
        self.year = year    # Инициализация через сеттеры для проверки инвариантов
        self.pages = pages
        
        self.words_per_page = words_per_page
        self.reading_speed = reading_speed

    @property
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

    def get_total_words(self) -> int:
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

    def __str__(self):
        return (f"Книга: '{self.title}' | Автор: {self.author} | Год: {self.year} | "
                f"Страниц: {self.pages}")