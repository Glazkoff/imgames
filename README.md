# ImGames (2.0) - геймификационная веб-платформа

Дипломная работа.

<a href="https://github.com/Glazkoff/imgames">
    <img src="https://img.shields.io/static/v1?label=%D0%92%D0%B5%D1%80%D1%81%D0%B8%D1%8F&message=2.0&color=green" />
</a>

## Технологии

- Vue
- Webpack
- Django
- Sentry
- Docker
- Docker-Compose
- Nginx
- Git (Github)
- Mailhog
- Graphql

## Использование

Установите [Docker](https://docs.docker.com/install/) и [Docker-Compose](https://docs.docker.com/compose/). Запустите виртуальные контейнеры с помощью следующей команды:

`docker-compose up --build`

Если всё работает отлично, вам необходимо создать суперпользователя для админпанели с помощью следующей команды:

`docker-compose run backend python manage.py createsuperuser`

## Деплой

Для production вам необходимо заполнить файл `.env` и использовать файл `docker-compose-prod.yml`

`docker-compose -f docker-compose-prod.yml up --build -d`

---

## Ход игры и мутации

| Действие                                    | Приложение   | Название мутации       | Готово |
| ------------------------------------------- | ------------ | ---------------------- | ------ |
| Зарегистрироваться                          | users        | register               | [x]    |
| Авторизоваться                              | users        | login                  | [x]    |
| Создать организацию                         | organization | create_organization    | [x]    |
| Создать комнату, раунд и месяцы             | rooms        | create_room            | [x]    |
| Добавить пользователя в комнату             | rooms        |                        | [ ]    |
| Сделать раунд активным                      | rooms        |                        | [ ]    |
| Отправить пользователю текущие показатели   |              |                        | [ ]    |
| Записать выбор карточек                     |              |                        | [ ]    |
| Просчитать изменения и вернуть показатели   |              |                        | [ ]    |
|                                             |              |                        | [ ]    |
|                                             |              |                        | [ ]    |
| Создать ещё один новый раунд в комнате      | rooms        |                        | [ ]    |
| Разлогиниться                               | users        | logout                 | [x]    |
| Запрос сброса пароля по почте               | users        | reset_password         | [x]    |
| Сброс пароля по почте через ссылку в письме | users        | reset_password_confirm | [x]    |

## Экраны

| Название                                       | Готово |
| ---------------------------------------------- | ------ |
| Авторизация                                    | [ ]    |
| Регистрация                                    | [ ]    |
| Создание комнаты                               | [ ]    |
| Комната (ожидание подключения создателем)      | [ ]    |
| Комната (ожидание подключения игроком)         | [ ]    |
| Комната (активная фаза игры, ожидание хода)    | [ ]    |
| Комната (активная фаза игры, не сделанный ход) | [ ]    |
| Комната (активная фаза игры, сделанный ход)    | [ ]    |
| Комната (раунд завершён)                       | [ ]    |
|                                                | [ ]    |
|                                                | [ ]    |
|                                                | [ ]    |
|                                                | [ ]    |
|                                                | [ ]    |
|                                                | [ ]    |

https://django-graphql-jwt.domake.io/
