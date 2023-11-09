import json


class JsonMaker:
    """
    Класс для работы с файлом *.json*
    """

    @staticmethod
    def remove_file(file_name='vacancies.json'):
        """
        Метод для очистки файла перед запросом к серверу
        """
        with open(file_name, 'w'):
            pass

    @staticmethod
    def add_vacancy(vacancies, file_name='vacancies.json'):
        """
        Запись вакансий полученных с сервера в файл
        """
        with open(file_name, 'a', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    @staticmethod
    def get_vacancy():
        """
        Запрос вакансий из файла
        """
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
