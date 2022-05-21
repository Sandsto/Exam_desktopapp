## Первая проблема 
Если во время запуска (на Windows 7) файла main.py ошибка
> qt.qpa.plugin: Could not find the Qt platform plugin "windows" in ""
> This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem

РЕШЕНИЕ: Найти папку где установлен python, перейти по пути C:\Users\Андрей\AppData\Local\Programs\Python\Python38\Lib\site-packages\PyQt5\Qt\plugins найти тут папку platforms и перенести в папку где находится python

[Источник](https://qna.habr.com/q/920179)

***Дополню: еcли используется виртуальное окружение venv, то искать надо в  \venv\Lib\site-packages\PyQt5\Qt5\plugins 
 и положить в C:\Users\Пользователь\AppData\Local\Programs\Python\Python38***

## Вторая проблема

На windows 7 при запуске main.py как python файл, через консоль всё работает, но при компеляции .exe файла с помощью pyinstaller exe не работает. Снова ошибка 
> qt.qpa.plugin: Could not find the Qt platform plugin "windows" in ""
> This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem

Решение, которое помогло - скопировать папку platforms в папку с .exe, тогда заработает

[Источник](https://stackoverflow.com/questions/47468705/pyinstaller-could-not-find-or-load-the-qt-platform-plugin-windows)
