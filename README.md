# Разработка прототипа программной системы для создания выкроек по индивидуальным параметрам
Научный руководитель: ст. преподаватель ДПИиИИ Крестникова Ольга Александровна.

Программная система представляет собой сайт [**Your Sewing Pattern**](http://nishigara.pythonanywhere.com/) и состоит из двух подсистем:
- Подсистема пользователя (разрабатывала Агапова Дарья Руслановна)
- Подсистема администратора (разрабатывала Накао Полина Дмитриевна)

## Установка и запуск
1. Установить IDE **PyCharm**: [ссылка на установку](https://www.jetbrains.com/pycharm/)
2. Создать проект: выбрать Get from VCS и в URL вставить ссылку на репозиторий ```https://github.com/dariRusAG/Diploma_Pattern.git```
3. Выбрать интерпретатор Python не ниже версии 3.10
4. Установить окружение: ввести команду в GitBash
```
python -m pip install -r requirements.txt
``` 
4. Запустить проект: в CommandPrompt ввести по-очереди три команды
```
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
5. В браузере ввести ```http://localhocs:5000```
 
## Доступный функционал
Для неавторизованного пользователя часть функционала является ограниченной. Для полного доступа к возможностям подсистем, в соответсвующем пункте будут приведены login и пароль.

### Подсистема пользователя
Login: test
Password: testtest

Подсистема включает в себя такие функции как:
- Построить выкройку по индивидуальным параметрам и скачать PDF-файл, с размещенной выкройкой на листах А4
- Построить детали выкройки по индивидуальным параметрам и скачать PDF-файл, с размещенными деталями выкройки на листах А4
- Сохранить личные параметры для повторного использования в личном кабинете
- Заполнить параметры значениями по выбранному стандартному размеру
- Получить информацию о том, как измеряются параметры
- Отфильтровать выкройки
- Добавить/удалить выкройку в/из списка избранного

### Подсистема администратора
Login: nakao.pd
Password: 1234567

Подсистема включает в себя такие функции как:
- CRUD-операции категорий базы данных
- CRUD-операции формул базы данных
- CRUD-операции деталей базы данных
- CRUD-операции линий базы данных
- CRUD-операции 3D-моделей базы данных
- CRUD-операции выкроек базы данных
- Построить выкройку по встроенному набору параметров
- Построить детали выкройки по встроенному набору параметров

Также сохраняется доступ к главной стрнаице, которая включает себя часть функций пользователя.
