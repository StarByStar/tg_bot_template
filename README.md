# Шаблон Телеграмм бота

Данный проект содержит шаблон телеграмм бота с примерами реализации популярных базовых сценариев, таких как:
Обработка комманд, обработка сообщений, работа с атрибутами сообщений, отправка сообщений, отправка изображений.

## Список используемых библиотек
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- requests
- python-dotenv

## Порядок установки
#### 1. Клонируем проект
#### 2. Создаем виртуальное окружение
```bash
python -m venv env
```
#### 3. Активируем виртуальное окружение
Windows:
```powershell
.\env\Scripts\activate
```
#### 4. Устанавливаем зависимости
```bash
pip install -r requirements.txt
```
#### 5. Регистрируем бота
В клиенте телеграмм находим бота **@BotFather**, вызываем команду /newbot
- Придумываем название(любое)
- Придумываем имя (должно обязательно заканчиваться на _bot)

Сохраняем токен созданного бота

#### 6. Готовим.env файл
Создаем файл, присваимваем переменной BOT_TOKEN значение ранее полученного токена


#### 7. Конец
Находим вашего бота в клиенте телеграмм и экспериментируем.