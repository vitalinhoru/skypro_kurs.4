from json import JsonSaver
from src.hh import HeadHunterAPI
from src.sj import SuperJobAPI
from vacancy import Vacancy


def main():
    JsonSaver.remove_file()  # Очистка файла с вакансиями перед поиском
    vacancy = input('ПОИСК ВАКАНСИЙ\n'
                    'Введите поисковый запрос, например "Python":\n'
                    '>>> ')

    platform = input('\n'
                     'Введите цифру для выбора платформы для поиска:\n'
                     '1 - HeadHunter\n'
                     '2 - SuperJob\n'
                     '3 - новый поисковый запрос\n'
                     '0 - выход из программы\n'
                     '>>> ')
    print('')

    def cycle(classAPI):
        total_view = int(input('Введите количество вакансий для вывода:\n'
                               '>>> '))
        print('')
        api = classAPI(vacancy)  # Создаём экземпляр класса для извлечения информации по API
        all_vacancies = api.get_vacancies()  # Получаем список вакансий
        all_vacancies_formated = api.formate_vacancies(all_vacancies)  # Форматируем список по шаблону
        Vacancy.output_final_result(all_vacancies_formated, total_view)  # Выводим результат

    if platform == '1':
        cycle(HeadHunterAPI)  # HH

    elif platform == '2':
        cycle(SuperJobAPI)  # SJ

    elif platform == '3':
        main()  # Повторный запуск программы

    elif platform == '0':
        print('Выход из программы.')

    else:
        print('Неверные данные. Выход из программы.')

    new_search = input('Начать новый поиск? (Y/N)\n>>> ').upper()
    if new_search == 'Y':
        print('')
        main()  # Повторный запуск программы
    else:
        print('Выход из программы.')


if __name__ == "__main__":
    main()
