## Organizational Design Web App

MVP Приложения для управления организационным дизайном

### Используемые технологии

- [Django 3.2.9](https://www.djangoproject.com/)
- [Django REST Framework 3.12.4](https://www.django-rest-framework.org/)
- [React 17.0.2](https://reactjs.org/)
- [BALKAN OrgChartJS](https://balkan.app/OrgChartJS/Docs/Edit)
- [Font Awesome](https://fontawesome.com/)

### Запуск разработческого сервера

Клонируем репозиторий

    git clone git@github.com:ramis-khasianov/orgdes.git

Устанавливаем зависимости для Django

    pip install -r requirements.txt

Проводим миграции

    python manage.py migrate

Устанавливаем зависимости для React, включая библиотеку Balkan graph и Font Awesome

    cd orgchart
    npm install

Запускаем сервер Django

    python manage.py runserver

Запускаем сервер React

    cd orgchart
    npm start

### Тестовые данные
    
Для этой версии подготовлены тестовые данные, сгенерированные библиотекой faker.

Для загрузки используем

    python manage.py loaddata empapp/fixtures/*.json
