@echo off

set BASE_DIR=%~dp0
echo %BASE_DIR%
cd /d %BASE_DIR%../

mv config.py config.py_

pyinstaller --clean --add-data "templates;templates" --add-data "sample;sample" --add-data "bin/*;." -n flaskcam app.py

mv config.py_ config.py
cp config.py dist/flaskcam/.
