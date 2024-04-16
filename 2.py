def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_data = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_data)
                except ValueError:
                    print(f"Помилка у форматі даних у рядку: {line.strip()}")

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

cats_info = get_cats_info("cats_file.txt")
if cats_info is not None:
    for cat in cats_info:
        print(cat)
