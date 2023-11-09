from json import JsonSaver


class Vacancy:
    """
    Класс для работы с вакансиями
    """
    list_vacancies = []

    def __init__(self, name, url, salary, exp):
        self.name = name
        self.url = url
        if int == type(salary):
            self.salary = salary
        else:
            self.salary = 0
        self.exp = exp

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.url}', {self.salary}, '{self.exp}')"

    def __str__(self):
        return (f'Профессия: {self.name}\n'
                f'Адрес объявления: {self.url}\n'
                f'Зарплата: {self.salary}\n'
                f'Опыт: {self.exp}')

    @staticmethod
    def instantiate_from_json():
        data = JsonSaver.get_vacancy()  # Берет вакансии из файла

        for vacancy in data['vacancies']:
            Vacancy.list_vacancies.append(Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'], vacancy['experience']))
        return Vacancy.list_vacancies

    @classmethod
    def sort_vacancies(cls):
        """
        Сортировка вакансий по заработной плате.
        """
        cls.list_vacancies.sort(key=lambda vacancy: vacancy.salary, reverse=True)
        return cls.list_vacancies

    @staticmethod
    def get_top_vacancies(top: int, vacancies: list):
        """
        Получаем топ вакансий из списка.
        """
        return vacancies[:top]

    @staticmethod
    def print_vacancies(for_print: list):
        """
        Форма вывода данных о вакансии в консоль
        """
        count = 1
        for vacancy in for_print:
            print(f'Вакансия №{count}:\n'
                  f'Название: {vacancy.name}\n'
                  f"Зарплата: {'{0:,}'.format(vacancy.salary).replace(',', ' ')} ₽\n"  # Разделитель порядков. (Сделать гибким)
                  f'Опыт работы: {vacancy.exp}\n'
                  f'Ссылка: {vacancy.url}\n')
            count += 1

    @staticmethod
    def output_final_result(all_vacancies, total_view):
        """
        Конечный результат вывода информации о вакансиях
        """

        JsonSaver.add_vacancy(all_vacancies)  # Добавляет в файл json список с вакансиями.
        vacancies = Vacancy.instantiate_from_json()  # Создает список экземпляров класса из json файла
        sort_vacancies = Vacancy.sort_vacancies()  # Сортировка по З/П
        top_vacancies = Vacancy.get_top_vacancies(top=total_view, vacancies=sort_vacancies)  # Получает топ вакансий
        Vacancy.print_vacancies(top_vacancies)  # Выводит топ вакансий
