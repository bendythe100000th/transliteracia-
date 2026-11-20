# Transliteraciä
"Transliteraciä" - это графическое приложение для транслитерации русского языка по лучшей в мире таблице транслитерации!
"Transliteraciä" - ĕto grafičeskoe priloženie dlä transliteracii russkogo äzyka po lučšeĭ v mire tablice transliteracii!
# Таблица транслитерации, которая используется в приложении
| Кириллическая буква | Латинская буква |
|---------------------|-----------------|
| а | a |
| б | b |
| в | v |
| г | g |
| д | d |
| е | e |
| ё | ö |
| ж | ž |
| з | z |
| и | i |
| й | ĭ |
| к | k |
| л | l |
| м | m |
| н | n |
| о | o |
| п | p |
| р | r |
| с | s |
| т | t |
| у | u |
| ф | f |
| х | h |
| ц | c |
| ч | č |
| ш | š |
| щ | ş |
| ъ | y̆ |
| ы | y |
| ь | ÿ |
| э | ĕ |
| ю | ü |
| я | ä |

# Программа в действии

# Установка
Для Ubuntu/Debian/Linux Mint и других дистрибутивов Linux на базе Debian или на базе дистрибутивов на базе Debian : скачать deb-пакет `transliteracia-1.0_all.deb`, открыть его и установить:
```bash
sudo apt install git
git clone https://github.com/bendythe100000th/transliteracia-.git
cd ./transliteracia-/
sudo apt install ./transliteracia-1.0_all.deb
```
Для остальных дистрибутивов Linux:
1. Установить зависимости
   Для Arch-based: ```sudo pacman -S python gtk3 python-gobject git```
   Для Fedora, РОСА ФРЕШ или других дистрибутивов на базе Fedora/RedHat: ```sudo dnf install python3 gtk3 python3-gobject git```
2. Скопировать все файлы в нужные директории
   ```bash
   git clone https://github.com/bendythe100000th/transliteracia-.git
   cd ./transliteracia-/
   sudo cp ./transliteraciä.py /usr/bin/transliteraciä/py/transliteraciä.py
   sudo cp ./transliteraciä.desktop /usr/share/applications/transliteraciä.desktop
   sudo cp ./translitguisvg.svg usr/share/icons/hicolor/scalable/apps/translitguisvg.svg
   ```
   Всё! Система установлена!
