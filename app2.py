import os
from pathlib import Path

def rename_files(dir_path, old_pattern, new_pattern):
    """
        Переименовать файлы в директории, имеющий в имени файла old_pattern
        
    Args:
        dir_path (str): путь до директории для переименования
        old_pattern (str): шаблон для поиска в имени файла (подстрока)
        new_pattern (str): новая подстрока ддля замены old_pattern
    """
    
    directory = Path(dir_path)
    
    # Проверка существования пути
    if not directory.exists():
        print(f"Ошибка: путь '{dir_path}' не существует")
        return
    
    # Проверка что это директория
    if not directory.is_dir():
        print(f"Ошибка: '{dir_path}' должен быть директорией")
        return
    
    # Получение списка файлов
    files = [f for f in directory.iterdir() if f.is_file()]
    
    # Проверка на пустоту директории
    if not files:
        print(f"Папка пустая или не содержит файлов")
        return
    
    renamed_count = 0
    
    for file_path in files:
        # Проверяем содержит ли имя файла old_pattern
        if old_pattern.lower() in file_path.name.lower():
            # Создаём новое имя
            new_name = file_path.name.replace(old_pattern, new_pattern)
            new_path = file_path.parent / new_name
            
            # Проверка на конфликт имён
            if new_path.exists():
                print(f"Предупреждение: файл '{new_name}' уже существует, пропускаем '{file_path.name}'")
                continue
            
            try:
                # Переименовываем файл
                file_path.rename(new_path)
                print(f"Переименован: '{file_path.name}' -> '{new_name}'")
                renamed_count += 1
            except Exception as e:
                print(f"Ошибка при переименовании '{file_path.name}': {e}")
                
    print(f"Завершено. Переименовано файлов: {renamed_count}")
    
rename_files("files", "order", "orders")