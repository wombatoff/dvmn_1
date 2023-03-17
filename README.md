
# Куда пойти — Москва глазами Артёма
### Описание
Сайта о самых интересных местах в Москве

### Стек технологий:
- Python
- Django
---


## Запуск проекта локально
Клонировать репозиторий и перейти в него:
```
git clone https://github.com/wombatoff/dvmn_1.git
cd dvmn_1
```

Создать и активировать виртуальное окружение, обновить pip и установить зависимости:
```
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Создать файл .env и заполнить его:
```
DEBUG=
DJANGO_SECRET_KEY=
```

Применить миграции
```
cd where_to_go
python manage.py migrate
```

Создать суперпользователя
```
python manage.py createsuperuser
```
Шаблон наполнения .env
```
DEBUG=
DJANGO_SECRET_KEY=
DJANGO_ALLOWED_HOSTS=
```


Заполнить базу данными (список команд static\places\load_places.sh)
```
python manage.py load_place "http://91.235.234.237/static/places/Антикафе Bizone"
...
python manage.py load_place "http://91.235.234.237/static/places/Японский сад.json.json"
```
Шаблон для создания файла с данными о месте:
```
{
    "title": "Название",
    "imgs": [
        "http://url_image_1",
        "http://url_image_2",
        ...
    ],
    "description_short": "Краткое описание",
    "description_long": "Полное описание",
    "coordinates": {
        "lng": 37.620070,
        "lat": 55.753630
    }
```
---
# Сайт проекта - Москва глазами Артёма

[http://91.235.234.237/](http://91.235.234.237/)


    


### Автор:

[Wombatoff](https://github.com/wombatoff/)