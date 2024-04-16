def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка у форматі даних у рядку: {line.strip()}")

        if count == 0:
            return 0, 0
        else:
            average = total / count
            return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None

total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
