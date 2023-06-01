"""
9. Класс «Сотрудник компании» Worker Экземпляр класса при инициализации
принимает аргументы: имя, должность и стаж работы сотрудника, метод print_info()
выводит информацию о сотруднике в формате: «Имя: Василий
Должность: Системный администратор Стаж: 3 года» При выводе стажа нужно учитывать,
что «года» должно заменяться на «лет» или «год» в зависимости от числа.
"""

class Worker:
    def __init__(self, name, post, experience):
        self.name = name
        self.post = post
        self.experience = experience

    def print_info(self):
        if self.experience == 1:
            experience_str = "1 год"
        elif self.experience == 2 or self.experience == 3 or self.experience == 4:
            experience_str = f"{self.experience} года"
        else:
            experience_str = f"{self.experience} лет"

        print(f"Имя: {self.name}\nДолжность: {self.post}\nСтаж: {experience_str}\n")

Employee1 = Worker("Арег", "Программист", 10)
Employee2 = Worker("Каплан", "Администратор", 4)
Employee3 = Worker("Арноу", "Аналитик", 1)

Employee1.print_info()
Employee2.print_info()
Employee3.print_info()