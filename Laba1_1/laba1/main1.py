from ControllerForJSON import DisplayJson
from ControllerForXML import DisplayXml
from list import action, detective, drama, military, heroes, animation, anime, interactive

def get_good_number(x): # Валидация  и проверка данных на ввод
    while True:
        try:
            rating = int(input(x))
            if rating <= 0:
                raise ValueError
            return rating
            break
        except ValueError:
            print("Параметры введены неверно, исправьте это... пожалуйста <\_/>.")

# Вывод информации
def print_data(data, file_format):
    if file_format == 'json':
        print("\nДанные из JSON:")
    elif file_format == 'xml':
        print("\nДанные из XML:")

    # Вывод Боевиков
    print("\nБоевики:")
    for action in data['actions']:
        print(f"Название: {action['title']}, Рейтинг: {action['rating']}, Продолжительность: {action['duration']}")

    # Вывод Детективов
    print("\nДетективы:")
    for detective in data['detectives']:
        print(f"Название: {detective['title']}, Рейтинг: {detective['rating']}, Продолжительность: {detective['duration']} ")

    # Вывод Драм
    print("\nДрамы:")
    for drama in data['dramas']:
        print(
            f"Название: {drama['title']}, Рейтинг: {drama['rating']}, Продолжительность: {drama['duration']}")

    # Вывод военных фильмов
    print("\nВоенные фильмы:")
    for military in data['militaries']:
        print(f"Название: {military['title']}, Рейтинг: {military['rating']}, Продолжительность: {military['duration']}")

    # Вывод супергеройских фильмов
    print("\nСупергеройские фильмы:")
    for heroes in data['heroes']:
        print(
            f"Название: {heroes['title']}, Рейтинг: {heroes['rating']}, Продолжительность {heroes['duration']}")

    # Вывод мультфильмов
    print("\nМультфильмы:")
    for animation in data['animations']:
        print(f"Название: {animation['title']}, Рейтинг: {animation['rating']}, Продолжительность: {animation['duration']}")

    # Вывод аниме
    print("\nАниме:")
    for anime in data['animes']:
        print(
            f"Название: {anime['title']}, Рейтинг: {anime['rating']}, Продолжительность: {anime['duration']}")

    # Вывод интерактивных кино
    print("\nИнтерактивное кино:")
    for interactive in data['interactives']:
        print(f"Название: {interactive['title']}, Рейтинг: {interactive['rating']} ")
        print(f"Режисер кино: {interactive['main_course']}")
        print(f"Программист: {interactive['side_dish']}")


def main(): # Въетнамские флешбэки подъехали
    dataFromXml = DisplayXml.load_from_xml("list.xml")
    dataFromJson = DisplayJson.load_from_json("list.json") # данные туда-сюда
    

    while True:

        choice = input("\nВыберите действие:\n"
                        "1. Добавить Боевик\n"
                        "2. Добавить Детективы\n"
                        "3. Добавить Драмы\n"
                        "4. Добавить Военное фильмы\n"
                        "5. Добавить Супергеройские фильмы\n"
                        "6. Добавить Мультфильмы\n"
                        "7. Добавить Аниме\n"
                        "8. Добавить Интерактивное кино\n"
                        "9. Сохранить в JSON\n"
                        "10. Сохранить в XML\n"
                        "11. Читать из JSON\n"
                        "12. Читать из XML\n"
                        "13. Выход\n")

        if choice == '1':
            title = input("Введите название Боевика: ")
            rating = get_good_number("Введите рейтинг: ")
            duration = input("Введите продолжительность: ")
            action_ = action(title, rating, duration)
            DisplayJson.add_action(dataFromJson, action_)
            DisplayXml.add_action(dataFromXml, action_)
        elif choice == '2':
            title = input("Введите название Детектива: ")
            rating = get_good_number("Введите рейтинг: ")
            duration = get_good_number("Введите продолжительность: ")
            detective_ = detective(title, rating, duration)
            DisplayJson.add_detective(dataFromJson, detective_)
            DisplayXml.add_detective(dataFromXml, detective_)
        elif choice == '3':
            title = input("Введите название Драмы: ")
            rating = get_good_number("Введите рейтинг: ")
            duration = get_good_number("Введите продолжительность: ")
            drama_ = drama(title, rating, duration)
            DisplayJson.add_drama(dataFromJson, drama_)
            DisplayXml.add_drama(dataFromXml, drama_)
        elif choice == '4':
            title = input("Введите название Военного кино: ")
            rating = get_good_number("Введите рейтинг: ")
            duration = input("Введите продолжительность: ")
            military_ = military(title, rating, duration)
            DisplayJson.add_military(dataFromJson, military_)
            DisplayXml.add_military(dataFromXml, military_)
        elif choice == '5':
            title = input("Введите название Супергеройского кино: ")
            rating = get_good_number("Введите рейтинг: ")
            duration = input("Введите продолжительность: ")
            heroes_ = heroes(title, rating, duration)
            DisplayJson.add_heroes(dataFromJson, heroes_)
            DisplayXml.add_heroes(dataFromXml, heroes_)
        elif choice == '6':
            title = input("Введите название Мультфильма: ")
            rating = get_good_number("Введите рейтинг: ")
            duration = input("Введите продолжительность: ")
            animation_ = animation(title, rating, duration)
            DisplayJson.add_animation(dataFromJson, animation_)
            DisplayXml.add_animation(dataFromXml, animation_)
        elif choice == '7':
            title = input("Введите название Аниме: ")
            rating = get_good_number("Введите рейтинг: ")
            duration = input("Введите продолжительность: ")
            anime_ = anime(title, rating, duration)
            DisplayJson.add_anime(dataFromJson, anime_)
            DisplayXml.add_anime(dataFromXml, anime_)
        elif choice == '8':
            title = input("Введите название интерактивного кино: ")
            rating = get_good_number("Введите рейтинг: ")
            director = input("Введите режиссёра: ")
            programmer = input("Введите программиста: ")
            interactive_ = interactive(title, rating, director, programmer)
            DisplayJson.add_interactive(dataFromJson, interactive_)
            DisplayXml.add_intaractive(dataFromXml, interactive_)
        elif choice == '9':
            DisplayJson.save_to_json(dataFromJson, "list.json")
            print(f"Данные сохранены в list.json ")
        elif choice == '10':
            DisplayXml.save_to_xml(dataFromXml, "list.xml")
            print(f"Данные сохранены в list.xml ")
        elif choice == '11':
            print_data(dataFromJson, 'json')
        elif choice == '12':
            print_data(dataFromXml, 'xml')
        elif choice == '13':
            break

if __name__ == "__main__":
    main()