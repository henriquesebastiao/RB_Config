@echo off

set PYTHON_VERSION=3.11.3
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
set PIP_URL=https://bootstrap.pypa.io/get-pip.py

set INSTALL_DIR=C:\Python
set VENV_DIR=C:\Python\venv

echo Baixando o instalador do Python...
curl -o python-installer.exe %PYTHON_URL%

echo Instalando o Python...
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 TargetDir=%INSTALL_DIR%

echo Baixando o instalador do pip...
curl -o get-pip.py %PIP_URL%

echo Instalando o pip...
"%INSTALL_DIR%\python.exe" get-pip.py

echo Instalando o virtualenv...
"%INSTALL_DIR%\Scripts\pip.exe" install virtualenv

echo Criando o ambiente virtual...
"%INSTALL_DIR%\python.exe" -m venv "%VENV_DIR%"

echo Python 3.11.3, pip e virtualenv instalados com sucesso!