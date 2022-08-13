# tomlconfig
Класс для представлени конфигурации Toml в виде словаря.\
[GitHub](https://github.com/pypi-zedzhen/tomlconfig)

## Установка
> pip install tomlconfig --index-url=https://pypi.zedzhen.ru/simple

## Использование
### TomlConfig(filename)
Объект TomlConfig ведёт себя как словарь.\
Основан на [BaseDictConfig](https://github.com/pypi-zedzhen/dictconfig)
#### filename
путь до файла в виде строки

### .read()
Перечитывает конфигурацию.\
Возвращает успешность операции.
### .save()
Сохраняет конфигурацию.\
Возвращает успешность операции.
