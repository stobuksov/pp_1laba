import json

class DisplayJson:

    def save_to_json(data, filename):
        try:#Обработка встроенной ошибки
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Все фильмы успешно сохранены в JSON-файл {filename}")
        except IOError as e:
            print(f"Ошибка при записи в JSON-файл: {str(e)}")

    def load_from_json(filename):
        try: #Обработка встроенной ошибки
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"actions": [], "detectives": [], "dramas": [], "militaries": [],"heroes": [],"animations": [],"animes": [],"interactives": []}

        # Добавление фильмов

    # Добавление фильмов
    def add_action(data, action):
        data['actions'].append(action.to_dict())

    def add_detective(data, detective):
        data['detectives'].append(detective.to_dict())

    def add_drama(data, drama):
        data['dramas'].append(drama.to_dict())

    def add_military(data, military):
        data['militaries'].append(military.to_dict())

    def add_heroes(data, heroes):
        data['heroes'].append(heroes.to_dict())

    def add_animation(data, animation):
        data['animations'].append(animation.to_dict())

    def add_anime(data, anime):
        data['animes'].append(anime.to_dict())

    def add_interactive(data, interactive):
        data['interactives'].append(interactive.to_dict())

