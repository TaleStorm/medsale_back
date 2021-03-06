# PARKS API BACKEND
## О проекте
Backend сервис проекта __Medsales_. 
## Структура и Конфиги

### Конфиги
В директории `envfiles` находятся файлы с переменными среды, которые необходимо определить для корректной работы сервисов.

Файлы  `.dev` и `.prod` с переменными содержат девовские и продовские конфиги соответственно, которые автоматически подхватываются при запуске docker образов.

В файлах `.env.[dev | prod]` содержатся переменные для rest-api сервиса, в файлах `.env.db.[dev | prod]` для сервиса БД PostgreSQL.

### Nginx
Прод конфиг так же содержит nginx сервис, настройки по которому находятся в отдельной директории `/nginx/` в корне проекта.

### REST API
Rest-api сервис написан на python + DRF. Приложения джанги расположены в директории `apps` (соответственно новые приложения помещать в эту же директорию).

Конфиги джанги(`config/settings`) разделены на базовые(base.py), дев(dev.py) и прод(prod.py). Основой для дев и прод настроек является базовый конфиг, куда выносится общая для этих сред конфигурация.

В директории `utils` находится различный вспомогательный код.

### Зависимости

Зависимости проекта находятся в директории `/requrements`, разделенные на базовые(base.txt), дев(dev.txt) и прод(prod.txt).

Базовые зависимоти являются общими для дев и прод зависимостей.
## Запуск

1. ### Через docker-compose

    Для запуска prod-версии:
    ```
    docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Для запуска dev-версии:
    ```
    docker-compose  up -d --build
    ```

2. ### Вне контейнера
    Рабочая БД в системе - PostgreSQL. Необходимо установить и настроить среду в соответсвии с конфигами в файлах .env. Если переменные среды не установлены, дефолтная БД будет SQLite.
    
    После импорта переменных среды и утсановки СУБД, необходимо создать БД, указанную в .env файле.
     
    Перед первым запуском необходимо создать таблицы в БД:
    ```shell
    python manage.py migrate
    ``` 
    
    Запуск rest-api сервиса:
    ```shell
    python manage.py runserver 0.0.0.0:8000
    ```
