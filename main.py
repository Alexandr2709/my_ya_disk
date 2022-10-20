import os
from pathlib import Path, PurePosixPath

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/publish'
        header = {"Authorization": f"OAuth {self.token}"}
        data = {"path": file_path}
        print(data)
        response = requests.put(upload_url, params=data, headers=header)
        print(response.text)
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = str(Path("test.txt").absolute())
    print(PurePosixPath(path_to_file))
    a = path_to_file.replace(os.altsep, os.sep)
    # print(path_to_file.absolute())
    print("a:", a)
    token = "y0_AgAAAABIuY5GAADLWwAAAADRz2Dc85STuxBnSMeSxszA-pWTOpMv9ng"
    my_disk = YaUploader(token)
    result = my_disk.upload(a)

