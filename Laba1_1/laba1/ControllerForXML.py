import xml.etree.ElementTree as ET
class DisplayXml:

    # Функция для добавления отступов
    def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                DisplayXml.indent(subelem, level + 1)
            if not subelem.tail or not subelem.tail.strip():
                subelem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def save_to_xml(data, filename):

        root = ET.Element('list')

        actions = ET.SubElement(root, 'actions')
        for action in data['actions']:
            action_element = ET.SubElement(actions, 'action')
            for key, value in action.items():
                child = ET.SubElement(action_element, key)
                child.text = str(value)

        detectives = ET.SubElement(root, 'detectives')
        for detective in data['detectives']:
            detective_element = ET.SubElement(detectives, 'detective')
            for key, value in detective.items():
                child = ET.SubElement(detective_element, key)
                child.text = str(value)

        dramas = ET.SubElement(root, 'dramas')
        for drama in data['dramas']:
            drama_element = ET.SubElement(dramas, 'drama')
            for key, value in drama.items():
                child = ET.SubElement(drama_element, key)
                child.text = str(value)

        militaries = ET.SubElement(root, 'militaries')
        for military in data['militaries']:
            military_element = ET.SubElement(militaries, 'military')
            for key, value in military.items():
                child = ET.SubElement(military_element, key)
                child.text = str(value)

        heroes = ET.SubElement(root, 'heroes')
        for hero in data['heroes']:
            hero_element = ET.SubElement(heroes, 'hero')
            for key, value in hero.items():
                child = ET.SubElement(hero_element, key)
                child.text = str(value)

        animations = ET.SubElement(root, 'animations')
        for animation in data['animations']:
            animation_element = ET.SubElement(animations, 'animation')
            for key, value in animation.items():
                child = ET.SubElement(animation_element, key)
                child.text = str(value)

        animes = ET.SubElement(root, 'animes')
        for anime in data['animes']:
            anime_element = ET.SubElement(animes, 'anime')
            for key, value in anime.items():
                child = ET.SubElement(anime_element, key)
                child.text = str(value)

        interactives = ET.SubElement(root, 'interactives')
        for interactive in data['interactives']:
            interactive_element = ET.SubElement(interactives, 'interactive')
            for key, value in interactive.items():
                child = ET.SubElement(interactive_element, key)
                child.text = str(value)

        DisplayXml.indent(root)
                # Создаем дерево XML и записываем его в файл
        try:
            tree = ET.ElementTree(root)
            tree.write(filename, encoding='utf-8', xml_declaration=True)
            print(f"Все блюда успешно сохранены в файл '{filename}'")
        except IOError as e:
            print(f"Ошибка при записи в XML-файл: {str(e)}")

    #Загрузка блюд из файла
    def load_from_xml(filename):
        try: #Обработка встроенной ошибки
            tree = ET.parse(filename)
            root = tree.getroot()
        except FileNotFoundError:
            return {"actions": [], "detectives": [], "dramas": [], "militaries": [],"heroes": [],"animations": [],"animes": [],"interactives": []}

        data = {"actions": [], "detectives": [], "dramas": [], "desserts": [],"salads": [],"bakeries": [],"soups": [],"breakfastMeals": []}

        # Загрузка боевиков
        actions = root.find('actions')
        if actions is not None:
            for movie in actions:
                action_data = {}
                for child in movie:
                    action_data[child.tag] = child.text
                data['actions'].append(action_data)

        # Загрузка детективов
        detectives = root.find('detectives')
        if detectives is not None:
            for detective in detectives:
                detective_data = {}
                for child in detective:
                    detective_data[child.tag] = child.text
                data['detectives'].append(detective_data)

        # Загрузка драм
        dramas = root.find('dramas')
        if dramas is not None:
            for drama in dramas:
                drama_data = {}
                for child in drama:
                    drama_data[child.tag] = child.text
                data['dramas'].append(drama_data)

        # Загрузка военных фильмов
        militaries = root.find('militaries')
        if militaries is not None:
            for military in militaries:
                military_data = {}
                for child in military:
                    military_data[child.tag] = child.text
                data['militaries'].append(military_data)

        # Загрузка супергеройского кино
        heroes = root.find('heroes')
        if heroes is not None:
            for hero in heroes:
                hero_data = {}
                for child in hero:
                    hero_data[child.tag] = child.text
                data['heroes'].append(hero_data)

        # Загрузка мультфильмов
        animations = root.find('animations')
        if animations is not None:
            for animation in animations:
                animation_data = {}
                for child in animation:
                    animation_data[child.tag] = child.text
                data['animations'].append(animation_data)

        # Загрузка аниме
        animes = root.find('animes')
        if animes is not None:
            for anime in animes:
                anime_data = {}
                for child in anime:
                    anime_data[child.tag] = child.text
                data['animes'].append(anime_data)

        # Загрузка интерактивного кино
        interactives= root.find('interactives')
        if interactives is not None:
            for intaractive in interactives:
                intaractive_data = {}
                for child in intaractive:
                    intaractive_data[child.tag] = child.text
                data['interactives'].append(intaractive_data)

        return data

    #Добавление фильмов
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
