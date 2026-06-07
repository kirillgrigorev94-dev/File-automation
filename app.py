import os
from pathlib import Path
import shutil

def sort_files_by_extension(dir_path):
    """
        Сортирует файлы в указанной директории по расширению файла
    
        Args: dir_path (str) - путь до директории для сортировки
    """
    
    directory = Path(dir_path)
    
    if not dir:
        print("Ошибка пути к папке")
        return
        
    if not directory.is_dir():
        print(f"Путь {dir_path} должен быть до папки")
        return
        
    items = directory.iterdir()
    
    files = os.listdir(dir_path)
    files = [entry for entry in files if os.path.isfile(os.path.join(dir_path, entry))]
    
    if len(files) == 0:
        print(f"Нет файлов для сортировки")
        return
    
    for item in items:
        if item.is_file():
            # Получаем расширение файла
            ext = item.suffix.lower()[1:]
            if not ext:
                ext = "no_extension"
                
            target_folder = directory / ext
            target_folder.mkdir(exist_ok=True)
            
            destination = target_folder / item.name
            
            counter = 1
            orig_destination = destination
            
            while destination.exists():
                stem = orig_destination.stem
                suffix = orig_destination.suffix
                destination = orig_destination.parent / f"{stem}_{counter}{suffix}"
                counter += 1
                
            shutil.move(str(item), str(destination))
        else:
            print(f"Не файл {str(item)}")
    
sort_files_by_extension("files")