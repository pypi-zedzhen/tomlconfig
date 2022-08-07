from setuptools import setup

setup(
    name='tomlconfig',
    version='1.0',
    py_modules=['tomlconfig'],
    url='https://github.com/pypi-zedzhen/tomlconfig',
    license='zlib/libpng License',
    license_files='LICENSE',
    author='Ярыкин Евгений',
    description='Класс для представлени конфигурации Toml в виде словаря.',
    python_requires='>=3.7',
    install_requires=[
        'dictconfig',
        'tomli',
        'tomli_w',
    ]
)
