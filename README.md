# RB_Config
![](https://img.shields.io/badge/license-GPLv3-blue) ![](https://img.shields.io/badge/python-3.11.3-blue) 

RB_Config é uma ferramenta com o intuito de facilitar a configuração de um roteador Mikrotik RouterOS.

[Documentação detalhada 📃.](http://henriquesebastiao.com/RB_Config/)
### Funcionalidades

- [x] Adicionar IP Address
- [x] Configuração de Servidor DHCP
- [x] Configuração de Servidor DNS
- [x] Configuração de NTP Client
- [x] Configuração de Access Point (Conexão DHCP)
- [x] Configuração de CPE Client (Conexão PPPoE)
## Como usar

### Instalação de dependências

#### Windows

1. Instale o [Python](https://www.python.org/downloads/) (versão testada 3.11.3)
2. Instale o virtualenv com o comando `pip install virtualenv`
3. DICA: Execute o arquivo `install.bat` para instalar o Python v3.11.3 e o virtualenv

#### Linux (Ubuntu)

1. Instale o [Python](https://www.python.org/downloads/) (versão testada 3.11.3) com o comando `sudo apt install python`
2. Instale o virtualenv com o comando `sudo apt install virtualenv`
3. DICA: Execute o arquivo `install.sh` para instalar o Python v3.11.3 e o virtualenv de acordo com sua distribuição caso não seja baseada Ubuntu

### Configuração do ambiente

1. Clone o repositório com o comando `git clone https://github.com/henriquesebastiao/RB_Config.git`
2. Entre na pasta do projeto com o comando `cd RB_Config`
3. Crie um ambiente virtual com o comando `virtualenv venv`
4. Ative o ambiente virtual com o comando `venv\Scripts\activate.bat` (Windows) ou `source venv/bin/activate` (Linux)
5. Instale as dependências com o comando `pip install -r requirements.txt`

### Execução

1. Execute o arquivo `main.py` com o comando `python main.py`

### Contribua com o projeto :)
Esta ferramenta foi desenvolvida para facilitar a configuração de roteadores Mikrotik RouterOS, porém, ainda existem muitas funcionalidades que podem ser adicionadas e modelos de roteadores que podem ser suportados.
Se você é um desenvolvedor ou administrador de redes (ou até mesmo um amador) que também manja de Python e roteadores Mikrotik, você pode contribuir com o projeto adicionando novas funcionalidades e modelos de roteadores suportados.

Este projeto é open source, então sinta-se livre para contribuir com o mesmo. Para isso, basta seguir os passos abaixo:

1. Faça um fork do projeto
2. Crie uma branch com a sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionando uma feature'`)
4. Faça um push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request
6. Depois que o merge da sua pull request for feito, você pode deletar a sua branch

### Licença
Este repositório está licenciado sob a GPL3, o que dá a você liberdade para usar, modificar e distribuir os scripts, desde que você siga as regras estabelecidas na [LICENÇA](LICENSE).

### Autor
Henrique Sebastião - [site](https://www.henriquesebastiao.com)
