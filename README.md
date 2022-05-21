# Exam_desktopapp
## Приложение для подготовки к экзаменам. Вносишь вопросы и варианты ответов, а затем проходишь тест

В программе 2 режима:

![изображение](https://user-images.githubusercontent.com/83036107/169650753-f4cdd77b-66fd-4b8e-a3d0-31033cccc885.png)

**Учитель** - для создания теста. В тесте возможно до 8 вариантов ответа. Файл сохраняется в формате JSON.
Рекомендуется сначала заполнить вопросами первый столбик, затем второй. Иначе будет пустой вопрос во время сдачи теста.

![изображение](https://user-images.githubusercontent.com/83036107/169650894-ec0b817e-1947-4eea-922c-0243379c8e6d.png)

Так же в режиме учитель можно редактировать существующий тест файл. Для этого есть кнопка "Загрузить".

**Студент** - режим сдачи теста. Все просто - нужно загрузить файл с вопросами, затем отвечать на вопросы, выбирая галочками правильные ответы и подтвердить ответ.
В случае ошибки - программа покажет правильный ответ, но засчитает ошибку. Вопросы показываются в случайном порядке.

![изображение](https://user-images.githubusercontent.com/83036107/169651141-cc1cadd9-5cdc-480f-9f4b-243e1c84c166.png)


*******************************************************************
Если во время запуска (на Windows 7) файла main.py ошибка
> qt.qpa.plugin: Could not find the Qt platform plugin "windows" in ""
> This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem

РЕШЕНИЕ: Найти папку где установлен python, перейти по пути C:\Users\Андрей\AppData\Local\Programs\Python\Python38\Lib\site-packages\PyQt5\Qt\plugins найти тут папку platforms и перенести в папку где находится python

[Источник](https://qna.habr.com/q/920179)

***Дополню: еcли используется виртуальное окружение venv, то искать надо в  \venv\Lib\site-packages\PyQt5\Qt5\plugins 
 и положить в C:\Users\Пользователь\AppData\Local\Programs\Python\Python38***
