

Тестовое задание на должность Python Backend Developer:



Тестовое задание предполагает создание сервера авторизации и новостей с комментариями и лайками на Django с использованием Django Rest Framework.


- Кастомная модель пользователя User(AbstractBaseUser,PermissionsMixin).

- CustomUserManager (BaseUserManager)

- Счетчик Like под новостью.

- Авторизация: Кастомный класс для JWT авторизации наследуемый от BaseAuthentication.


- Новости: Каждый пользователь может создавать новости, получать списки всех новостей с пагинацией, удалять и изменять свои новости. Админ может удалять и изменять любые новости.


- Комментарии: Автор может удалять комментарии к своим новостям, админ может удалять любые комментарии.


- Контейнеризация: Использование Docker-compose для контейнеризации приложения.


- Gunicorn: Использование gunicorn в качестве WSGI HTTP-сервера для развертывания приложения.


- Nginx для обработки статических файлов и обеспечения эффективной работы приложения.


- Swagger: Использование Swagger для документирования API.


- .env файл: Использование .env файла для хранения информации о подключении к базе данных.

---




  
---

Установка и запуск (Локально)

- Клонировать репозиторий:
>git clone https://github.com/Alexandr-eng/Test.git

- Перейти в директорию проекта:
>cd Test

- Установить зависимости:
>pip install -r requirements.txt

- Запустить миграции: 
>python manage.py migrate

- Запустить сервер:
>python manage.py runserver
___

Сборка Docker образа

- Клонировать репозиторий:
>git clone https://github.com/Alexandr-eng/Test.git

- Перейти в директорию проекта:
>cd Test

- Создать файл .env.dev:

```
DEBUG=0
SECRET_KEY=secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
POSTGRES_DB=имя_твоей_бд
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_USER=имя_твоего_пользователя
POSTGRES_PASSWORD=пароль_бд
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
- В консоли выролните команду:

В будущем для запуска проекта, при первом запуске. Далее контейнр будет собран и --build не пишем
>docker-compose up --build

- Откройте новую консоль, введите команду:
>docker ps

- Зайдите в контейнер с проектом Django:
>docker exec -it ItFox_web bash

- Выполните команды:

python manage.py collectstatic
python manage.py createsuperuser


___

API
Для получения подробной информации о доступных API-endpoint и их
использовании, пожалуйста, обратитесь к Swagger документации.</h5>

Локально http://127.0.0.1:8000/api/swagger/

Docker http://localhost/api/swagger/



