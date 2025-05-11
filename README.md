<div align="center">
    <h1>
        <b>Gesture Recognition</b>
    </h1>
    <h3>
        Сервис определения жестов рук на видеопотоке
    </h3>
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/alex6712/gesture-recognition?logo=GitHub">
    <img alt="Test and Deploy" src="https://github.com/alex6712/gesture-recognition/actions/workflows/test_and_deploy.yml/badge.svg">
    <a href="https://github.com/psf/black">
        <img alt="Python code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
    <a href="https://github.com/prettier/prettier">
        <img alt="TypeScript code style: Prettier" src="https://img.shields.io/badge/code%20style-prettier-ff69b4.svg">
    </a>
</div>

Код бакалаврской дипломной работы студента НГТУ им. Р.Е. Алексеева, Ванюкова Алексея Игоревича, ИРИТ, НГТУ, 21-ИС.

## Предисловие

В данном проекте я, как студент-разработчик, хотел показать, чему я научился за время обучения
в университете.

- Веб-разработка;
- машинное обучение;
- работа с базами данных;
- составление архитектуры приложения;
- использование паттернов программирования;
- составление документации;
- тестирование и развёртка;
- администрирование серверов;
- соблюдение методологии DevOps. 

Это навыки и знания, которые я получил благодаря замечательному педагогическому составу НГТУ. 
Я постарался интегрировать их в мою выпускную квалификационную работу.

## Описание задачи

### 1. Модель компьютерного зрения

Модель машинного обучения с использованием принципов компьютерного зрения, которая может определять
жесты человека на видеопотоке. Для обучения модели использовался набор данных [HaGRID](https://github.com/hukenovs/hagrid).

Основные использованные технологии и инструменты: **PyTorch**, **OpenCV**, **NumPy**.

### 2. RESTful API

API с использованием принципов REST для предоставления внешнего публичного интерфейса
к модели машинного обучения. Для соблюдения принципов микросервисной архитектуры *RESTful API*
и *модель* являются отдельными независимыми *сервисами*.

Основные использованные технологии и инструменты: **FastAPI**, **pydantic**.

### 3. Межсервисное взаимодействие через gRPC

Установка интерфейса общения между отдельными сервисами внутри приложения с использованием
**gRPC**. Клиентом выступает *сервис RESTful API*, сервером - *модель машинного обучения*.

Основные использованные технологии и инструменты: **gRPC**, **Protobuf**, **Bash**.

### 4. Развёртка приложения на удалённом сервере

Развёртка приложения на арендованном удалённом сервере с использованием систем контейнеризации
и средств *CI/CD*. Настройка веб-сервера, регистрация доменного имени, проброс прокси и администрирование
сервера. Настройка безопасного соединения по протоколу *HTTPS* используя сертификат *Let's Encrypt*.

Основные использованные технологии и инструменты: **GitHub Actions**, **Linux**, **Docker (docker-compose)**, **nginx**.

## Ссылка на приложение

Сервис _RESTful API_ приложения доступен по адресу:

https://api.gesture-recognition-nntu.ru

Документация _API_:

https://api.gesture-recognition-nntu.ru/docs

В дальнейшем предполагается наличие frontend-приложения с user-friendly
интерфейсом для использования обычными пользователями.

Располагаться данное приложение будет по адресу:

https://www.gesture-recognition-nntu.ru
или
https://gesture-recognition-nntu.ru

## Примеры

Примеры запросов на различные _endpoints_.

### *root*

Запрос **curl**:
```
curl -X 'GET' \
  'https://api.gesture-recognition-nntu.ru/api/v1/' \
  -H 'accept: application/json'
```

**Request URL**:
```
https://api.gesture-recognition-nntu.ru/api/v1/
```

Ответ **StandardResponse**:
```json
{
  "code": 200,
  "message": "API works!"
}
```

## Лицензия

Данный проект находится под лицензией [MIT License/X11 License](https://github.com/alex6712/gesture-recognition/blob/master/LICENSE).

## Автор

Ванюков Алексей Игоревич, НГТУ, ИРИТ, группа 21-ИС.

Контакты:
- Telegram: [@ecuripusu](https://t.me/ecuripusu)
- ВКонтакте: [Ванюков Алексей](https://vk.com/zerolevelmath)
- Адрес электронной почты: alexeivanyukov@yandex.ru
