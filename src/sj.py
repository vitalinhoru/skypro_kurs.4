import os
import requests
from abs import GetAPI


class SuperJobAPI(GetAPI):
    """
    Класс для получения вакансий по API SuperJob.ru
    """

    def __init__(self, vacancy):
        self.base_url = 'https://api.superjob.ru/2.0'
        self.SJ_API = 'https://api.superjob.ru/2.0/vacancies/'
        self.vacancy = vacancy
        self.params = {
            'keyword': self.vacancy,
            'count': 100,  # Количество
            'town': 14  # СПб
        }

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.params['keyword']}', '{self.params['town']}', '{self.params['count']}')"

    def get_vacancies(self):
        """
        Получение вакансий с сайта
        """
        url = f'{self.base_url}/vacancies'
        api_key = os.getenv('SJ_API_KEY')
        headers = {'X-Api-App-Id': api_key}
        response = requests.get(url, params=self.params, headers=headers)
        return response.json()

    def formate_vacancies(self, all_vacancies):
        """
        Приведение списка вакансий к необходимой форме
        """
        vacancies_to_dict = {'vacancies': []}
        for vacancy in all_vacancies['objects']:
            if vacancy['payment_from'] and vacancy['payment_to']:
                salary = (int(vacancy['payment_from']) + int(vacancy['payment_to'])) // 2
                # salary = f"от {int(vacancy['payment_from'])} до {int(vacancy['payment_to'])}"
            elif vacancy['payment_from'] is None:
                salary = vacancy['payment_to']
            elif vacancy['payment_to'] is None:
                salary = vacancy['payment_from']
            else:
                salary = 'З/п не указана'
                # salary = vacancy['payment_from']
            my_form_dict = {'name': vacancy['profession'], 'url': vacancy['link'], 'salary': salary,
                            'experience': vacancy['experience']['title']}
            vacancies_to_dict['vacancies'].append(my_form_dict)
        return vacancies_to_dict
