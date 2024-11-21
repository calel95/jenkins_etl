# Dockerfile-jenkins

FROM jenkins/jenkins:lts

# Definir o diretório de trabalho no container
WORKDIR /app

# Use o usuário root para instalar pacotes e configurar permissões
USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copiar o arquivo de requisitos
COPY requirements.txt /app/requirements.txt

# Instalar as dependências do Python dentro do ambiente virtual
RUN /app/venv/bin/pip install -r requirements.txt

# Retornar ao usuário Jenkins
USER jenkins

# Instalar plugins adicionais do Jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"