#!/bin/bash

PYTHON_VERSION=3.11.3
PYTHON_URL=https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz
INSTALL_DIR=/opt/python

VENV_DIR=/opt/python/venv

# Função para verificar a distribuição Linux
get_distribution() {
    if [ -f /etc/os-release ]; then
        # Obtém o nome da distribuição a partir do arquivo /etc/os-release
        . /etc/os-release
        echo "$NAME"
    elif type lsb_release >/dev/null 2>&1; then
        # Obtém o nome da distribuição usando o comando lsb_release
        lsb_release -si
    elif [ -f /etc/lsb-release ]; then
        # Obtém o nome da distribuição a partir do arquivo /etc/lsb-release
        . /etc/lsb-release
        echo "$DISTRIB_ID"
    elif [ -f /etc/debian_version ]; then
        # Assume Debian se não houver outras opções disponíveis
        echo "Debian"
    else
        # Caso não seja possível determinar a distribuição
        echo "Distribuição não identificada"
    fi
}

# Obtém a distribuição Linux
distribution=$(get_distribution)

# Instala os pacotes necessários de acordo com a distribuição
if [ "$distribution" == "Ubuntu" ] || [ "$distribution" == "Debian" ]; then
    # Instala os pacotes necessários no Ubuntu/Debian
    sudo apt update
    sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl
elif [ "$distribution" == "Fedora" ]; then
    # Instala os pacotes necessários no Fedora
    sudo dnf install -y gcc zlib-devel ncurses-devel gdbm-devel libnsl libffi-devel openssl-devel sqlite-devel readline-devel curl
else
    echo "Gerenciador de pacotes não suportado para a distribuição $distribution"
    exit 1
fi

# Baixa o código-fonte do Python
curl -o python.tar.xz ${PYTHON_URL}

# Extrai o código-fonte do Python
tar -xf python.tar.xz

# Navega para o diretório do código-fonte do Python
# shellcheck disable=SC2164
cd Python-${PYTHON_VERSION}

# Configura e compila o Python
./configure --prefix=${INSTALL_DIR}
# shellcheck disable=SC2046
make -j$(nproc)
sudo make install

# Cria um link simbólico para o Python recém-instalado
sudo ln -sf ${INSTALL_DIR}/bin/python3 /usr/bin/python3

# Instala o pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo ${INSTALL_DIR}/bin/python3 get-pip.py

# Instala o virtualenv
sudo ${INSTALL_DIR}/bin/pip install virtualenv

# Cria o ambiente virtual
${INSTALL_DIR}/bin/python3 -m venv ${VENV_DIR}

echo "Python 3.11.3, pip e virtualenv instalados com sucesso!"
