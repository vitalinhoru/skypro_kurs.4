import requests
from abs import GetAPI


class HeadHunterAPI(GetAPI):
    HH_API = 'https://api.hh.ru/vacancies'

    def __init__(self, vacancy):
        self.vacancy = vacancy
        self.params = {
            'text': vacancy,  # Название
            'per_page': 100,  # Количество
            'area': 2  # СПб
        }

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.params['text']}', '{self.params['area']}', '{self.params['per_page']}')"

    def get_vacancies(self):
        """
        Получает список вакансий
        """
        response = requests.get(self.HH_API, self.params)
        return response.json()

    def formate_vacancies(self, all_vacancies):
        """
        Форматирование списка вакансий
        """
        vacancies_to_dict = {'vacancies': []}
        for vacancy in all_vacancies['items']:

            # if vacancy['salary']['from'] and vacancy['salary']['to']:
            #     salary = f"от {int(vacancy['salary']['from'])} до {int(vacancy['salary']['to'])}"
            # elif vacancy['salary']['from'] is None:
            #     salary = vacancy['salary']['to']
            # elif vacancy['salary']['to'] is None:
            #     salary = vacancy['salary']['from']
            # else:
            #     salary = 'З/п не указана'

            if vacancy['salary'] is None:
                salary = 'З/п не указана'
            elif vacancy['salary']['from'] is None:
                salary = vacancy['salary']['to']
            elif vacancy['salary']['to'] is None:
                salary = vacancy['salary']['from']
            else:
                # salary = f"от {int(vacancy['salary']['from'])} до {int(vacancy['salary']['to'])}"
                salary = (int(vacancy['salary']['from']) + int(vacancy['salary']['to'])) // 2

            my_form_dict = {'name': vacancy['name'], 'url': vacancy['alternate_url'], 'salary': salary,
                            'experience': vacancy['experience']['name']}
            vacancies_to_dict['vacancies'].append(my_form_dict)
        return vacancies_to_dict
