### Описание
Тестовое задание. Проект сервиса API для социальной сети, в которой пользователи могут делиться новостями, оставлять комментарии и ставить лайки.

#### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```python
git clone https://github.com/.../test_sochi
```
```python
cd test_sochi
```

#### Шаблон наполнения ENV файла:

ENV файл с переменными окружения имеет вид:
```python
SECRET_KEY==........... # указывать секретный код
DB_ENGINE=........... # тут необходимо указывать, что работаем с postgresql
DB_NAME=........... # указываем имя базы данных
POSTGRES_USER=........... # логин для подключения к базе данных
POSTGRES_PASSWORD=........... # указать пароль для подключения к БД
DB_HOST==........... # название сервиса (контейнера)
DB_PORT==........... # порт для подключения к БД
```

#### Команды для запуска приложения в контейнерах:

После подготовки файла необходимо поднять проект с 
имеющейся базой данных командой:
```python
docker-compose up -d --build
```
Далее необходимо выполнить миграции и создать суперпользователя 
(команды выполняются поочередно, одна за другой):
```python
docker-compose exec web python manage.py migrate
```
```python
docker-compose exec web python manage.py createsuperuser
```
```python
docker-compose exec web python manage.py collectstatic --no-input
```

Проект будет доступен по ссылке http://localhost/admin/


Также проект работает на виртуальной машине Yandex.Cloud по адресу http://51.250.16.163/admin/
Тестовые учетные данные для входа:  
User - Alex  
Password - 12345678
