# API для социальной сети Yatube
## Описание
Функционал социальной сети организован в API. Запросы выполняются с помощью методов GET, POST, PUT, PATCH, DEL. Формат передачи данных - JSON.

В API реализованы следующие возможности:
- получить, обновить Token;
- публиковать и удалять свои записи;
- комментировать записи, изменять или удалять свои комметнарии к записи;
- получить список подписок, а также подписываться от авторов.

## Технологии
- Python 3.7
- Django 3.2
- DRF
- JWT + Djoser

## Запуск проекта в dev-режиме
- Клонировать репозиторий и перейти в него в командной строке.
- Установить и активировать виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7), обновить pip:
```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
```
- Установить все зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```
- Применить миграции:
```bash
python manage.py migrate
```
Создать суперпользователя (при необходимости):
```bash
python manage.py createsuperuser
```
Запустить проект:
```bash
python manage.py runserver
```
## Примеры работы с API для всех пользователей
Для неавторизованных пользователей работа с API доступна в режиме чтения.
```bash
GET api/v1/posts/ - получить список всех публикаций (поддержка пагинации при указании параметров limit и offset)
GET api/v1/posts/{id}/ - получение публикации по id

GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
## Примеры работы с API для авторизованных пользователей
```bash
POST /api/v1/posts/ - создание новой публикации

PUT /api/v1/posts/{id}/ - обновление публикации

PATCH /api/v1/posts/{id}/ - частичное изменение публикации

DEL /api/v1/posts/{id}/ - удаление публикации

GET /api/v1/follow/ - получение списка подписок пользователя

POST /api/v1/follow/ - подписка на автора, переданного в body запроса
```

## Работа с JWT-токеном (Joser)
Получить токен:
```bash
POST /api/v1/jwt/create/
```
Передав в body данные пользователя:
```bash
{
"username": "string",
"password": "string"
}
```
Обновить токен:
```bash
POST /api/v1/jwt/refresh/
```
Проверить токен:
```bash
POST /api/v1/jwt/verify/

### Авторы
Давлат Файзиев

e-mail: bodra84@gmail.com
