# SaverBot

<details>
  <summary>Содержание</summary>
  <ol>
    <li>
      <a href="#описание">Описание</a>
      <ul>
        <li><a href="#возможности">Возможности</a></li>
        <li><a href="#технологии">Технологии</a></li>
      </ul>
    </li>
    <li>
      <a href="#установка-и-запуск">Установка и запуск</a>
      <ul>
        <li><a href="#зависимости">Зависимости</a></li>
        <li><a href="#установка">Установка</a></li>
        <li><a href="#запуск-docker">Запуск (Docker)</a></li>
        <li><a href="#запуск-локально">Запуск (Локально)</a></li>
      </ul>
    </li>
    <li><a href="#использование">Использование</a></li>
    <li>
      <a href="#дополнительная-информация">Дополнительная информация</a>
      <ul>
        <li><a href="#переменные-окружения">Переменные окружения</a></li>
      </ul>
    </li>
    <li><a href="#авторы">Авторы</a></li>
  </ol>
</details>

<a name="описание"></a>

> **Note**:
> Тестовое задания ([описание](./docs/test_task.pdf)) для вакансии "Младший разработчик python".

Telegram-бот, который помогает быстро и удобно добавлять новые ресурсы для парсинга.
Таким образом, бот облегчает работу с crawler без UI.

### Возможности

* Быстрое и удобное добавление новых ресурсов для парсинга.

### Технологии

[![aiogram][aiogram-badge]][aiogram-url]
[![SQLAlchemy][SQLAlchemy-badge]][SQLAlchemy-url]
[![Docker][Docker-badge]][Docker-url]
[![pre-commit][pre-commit-badge]][pre-commit-url]

## Установка и Запуск

Набор инструкций, необходимых для запуска приложения.

### Зависимости

* [Python 3.10+](https://www.python.org/)
* [Docker Compose](https://www.docker.com/) – *необязательно

### Установка

1. Клонировать репозиторий.

    ```shell
    git clone https://github.com/tvules/SaverBot.git
    cd SaverBot
    ```

2. Переименовать файл `.env.example` в `.env` и задать переменные окружения.

    ```dotenv
    BOT_TOKEN=<Токен аутентификации бота>
    ```

### Запуск (Docker)

1. Выполнить сборку и запуск контейнера Docker.

    ```shell
    docker compose up -d
    ```
    
    > **Note**:
    > В старый версиях Docker используется команда `docker-compose`.

### Запуск (Локальный)

1. Установить зависимости.

    ```shell
    pip install -r requirements.txt
    ```

2. Применить миграции базы данных.

    ```shell
    alembic upgrade head
    ```

3. Выполнить запуск модуля.

    ```shell
    python -m tgbot
    ```

## Использование

Пользователь может прислать боту Exel файл с полями:

* title – Описание
* url – URL-адрес ресурса
* xpath – X-Path селектор для поиска цены

После загрузки файла бот сохранит содержимое файла в базу данных.

## Дополнительная Информация

Информация полезная для использования и разработки.

### Переменные окружения

* BOT_TOKEN – Токен авторизации tg-бота, выданный [BotFather](https://t.me/BotFather).
* DB_URL – URL-адрес для подключения к базе данных. По умолчанию: `sqlite+aiosqlite:///db.sqlite3`.

## Авторы

- **Илья Петрухин** (*Разработчик*) — **[GitHub](https://github.com/tvules)**

<!-- Markdown badges & links -->

[aiogram-url]: https://aiogram.dev/
[aiogram-badge]: https://img.shields.io/badge/aiogram-2CA5E0?style=for-the-badge

[SQLAlchemy-url]: https://www.sqlalchemy.org/
[SQLAlchemy-badge]: https://img.shields.io/badge/sqlalchemy-fbfbfb?style=for-the-badge

[Docker-url]: https://www.docker.com/
[Docker-badge]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white

[pre-commit-url]: https://pre-commit.com/
[pre-commit-badge]: https://img.shields.io/badge/pre--commit-1f2d23?style=for-the-badge&logo=pre-commit&logoColor=FAB040
