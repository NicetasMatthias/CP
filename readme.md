# КриптоПротоколы
## Лабораторная работа по дисциплине "Криптопротоколы"
Это работа демонстирует пример работы криптографического протокола
### Составляющие:
- Симметричный шифр: AES *добавить размерность*
- Асимметричный шифр: RSA *добавить размерность*
- Хеш-функция: SHA-1
- Алгоритм цифровой подписи: RSA *добавить спецификацию*


## Внимание!
Чтобы вносимые изменения в .ui и .rc файлы и файлы переводов оказывали влияние при сборке, необходимо
### Linux:
***mainwindow.py*** содержит строку
```Python
#os.system("./make_ui.sh")
```
ее нужно раскоментить и соответственно создать в каталоге исходного кода файл ***make_ui.sh*** со следующим содержанием:
```bash
    pyside6-uic form.ui -o ui_form.py
    pyside6-uic informationDialog.ui -o informationDialog.py
    pyside6-rcc resources.qrc -o rc_resource.py
    pyside6-lupdate form.ui informationDialog.ui mainwindow.py -ts translation_ru.ts
    pyside6-lrelease translation_ru.ts -qm translation_ru.qm
```
> В случае отличия в версии pyside заменить на свою

### Windows:
Нужно настроить исполнение аналогичного кода:
```bash
    pyside6-uic form.ui -o ui_form.py
    pyside6-uic informationDialog.ui -o informationDialog.py
    pyside6-rcc resources.qrc -o rc_resource.py
    pyside6-lupdate form.ui informationDialog.ui mainwindow.py -ts translation_ru.ts
    pyside6-lrelease translation_ru.ts -qm translation_ru.qm
```
