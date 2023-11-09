from abc import ABC, abstractmethod


class GetAPI(ABC):
    """
    Создаём абстрактный класс для получения и обработки данных по API
    """

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def formate_vacancies(self, all_vacancies):
        pass
