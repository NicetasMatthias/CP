# КриптоПротоколы
## Лабораторная работа по дисциплине "Криптопротоколы"
Это работа демонстирует пример работы криптографического протокола
### Составляющие:
- Симметричный шифр: AES *добавить размерность*
- Асимметричный шифр: RSA *добавить размерность*
- Хеш-функция: *добавить хеш-функцию*
- Алгоритм цифровой подписи: RSA *добавить спецификацию*


## Внимание!
Чтобы вносимые изменения в .ui и .rc файлы оказывали влияние при сборке, необходимо
### Linux:
***mainwindow.py*** содержит строку
```Python
#os.system("./make_ui.sh")
```
ее нужно раскоментить и соответственно создать в каталоге исходного кода ***make_ui.sh*** файл со следующим содержанием:
```bash
    pyside6-uic form.ui -o ui_form.py
    pyside6-uic informationDialog.ui -o informationDialog.py
    sed -i "s/PyQt6/PySide6/" ui_form.py
    sed -i "s/PyQt6/PySide6/" informationDialog.py
    pyside6-rcc resources.qrc -o rc_resource.py>
```
> В случае отличия в версии pyside заменить на свою

### Windows:
Нужно настроить исполнение аналогичного кода:
```bash
    pyside6-uic form.ui -o ui_form.py
    pyside6-uic informationDialog.ui -o informationDialog.py
    sed -i "s/PyQt6/PySide6/" ui_form.py
    sed -i "s/PyQt6/PySide6/" informationDialog.py
    pyside6-rcc resources.qrc -o rc_resource.py>
```
