# Создание файла calculator.py
class Calculator:
    def add(self, a, b):
        """Возвращает сумму a и b."""
        return a + b

    def subtract(self, a, b):
        """Возвращает разность a и b."""
        return a - b

    def multiply(self, a, b):
        """Возвращает произведение a и b."""
        return a * b

    def divide(self, a, b):
        """Возвращает частное от деления a на b.
        
        Если b == 0, вызывает исключение ZeroDivisionError.
        """
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
________________________________________________________________________________

#Создание файла с тестами
#test_calculator.py
import unittest
from calculator import Calculator  # Импортируем класс из файла calculator.py

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Инициализация тестируемого объекта перед каждым тестом."""
        self.calc = Calculator()

    def test_add(self):
        """Тест для метода сложения."""
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-3, -5), -8)

    def test_subtract(self):
        """Тест для метода вычитания."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(5, -5), 10)

    def test_multiply(self):
        """Тест для метода умножения."""
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_divide(self):
        """Тест для метода деления."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_divide_by_zero(self):
        """Проверка деления на ноль."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
  
#Запуск тестов
python -m unittest test_calculator.py













