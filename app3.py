import os
import shutil
from datetime import datetime, timedelta

def archive_old_files(dir_path, day_threshold=30, archive_format='zip'):
    """
        Архивирует файлы в указанной директории, которые не изменялись дольше заданного количества дней.
        
    Args:
        dir_path (str): путь к директории с файлами для архивирования.
        day_threshold (int): количество дней — порог «старости» файла (по умолчанию 30).
        archive_format (str): формат архива ('zip', 'tar', 'gztar', 'bztar', 'xztar').
    """
    
    # Получаем текущую дату и вычесляем порог даты модификации
    current_time = datetime.now()
    threshold_time = current_time - timedelta(days=day_threshold)
    
    # Собираем список файлов, подлежащих архивированию
    files_to_archive = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Получаем время последней модификации файла
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if mod_time < threshold_time:
                files_to_archive.append(file_path)
                
    # Если подходящих файлов нет завершаем работу
    if not files_to_archive:
        print(f"Файлы старше указанного порога не найдены")
        return
    
    # Создаём временную директорию для файлов, которые будем архивировать
    temp_dir = os.path.join(dir_path, "temp_archive")
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Копируем файлы во временную директорию
        for file_path in files_to_archive:
            relative_path = os.path.relpath(file_path, dir_path)
            dest_path = os.path.join(temp_dir, relative_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(file_path, dest_path)
            
        # Формируем имя архива с текущей датой и временем
        timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        archive_name = f"archive_{timestamp}"
        archive_path = os.path.join(dir_path, archive_name)
        
        # Создаём архив
        shutil.make_archive(
            base_name=archive_path,
            format=archive_format,
            root_dir=temp_dir
        )
        print(f"Архив создан: {archive_path}.{archive_format}")
        
        # Удаляем исходные файлы после успешного архивирования
        for file_path in files_to_archive:
            os.remove(file_path)
            print(f"Удалён файл: {file_path}")
            
    except Exception as e:
        print(f"Произошла ошибка при архивировании: {e}")
    finally:
        # Очищаем временную директорию
        shutil.rmtree(temp_dir)
        
archive_old_files(r"C:\Users\User\OneDrive\Desktop\Lesson Python\File automation\files", day_threshold=30, archive_format="zip")