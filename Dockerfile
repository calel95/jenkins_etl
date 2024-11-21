# Dockerfile-jenkins

FROM jenkins/jenkins:lts

# Definir o diretório de trabalho no container
WORKDIR /app

# Use o usuário root para instalar pacotes
USER root

# Atualizar os pacotes e instalar o Python3 e o pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de requisitos
COPY requirements.txt /app/requirements.txt

# Instalar as dependências do Python
RUN pip3 install -r requirements.txt

# Retornar ao usuário Jenkins
USER jenkins

# Instalar plugins adicionais do Jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"