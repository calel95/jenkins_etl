import duckdb 
import os
import pandas as pd
import logging

class Extract:
    def __init__(self) -> None:
        self.df = None
        # Configurar logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def web_one_input_csv(self, file):
        """Carrega dados de um arquivo CSV em memória."""
        try:
            self.logger.info(f"Tentando carregar arquivo CSV: {file}")
            
            # Verificar se o arquivo existe
            if not os.path.exists(file):
                raise FileNotFoundError(f"O arquivo {file} não foi encontrado.")
            
            # Verificar se o arquivo está vazio
            if os.path.getsize(file) == 0:
                raise ValueError(f"O arquivo {file} está vazio.")
            
            # Tentar ler o arquivo
            self.df = duckdb.read_csv(file)
            self.logger.info(f"Arquivo CSV carregado com sucesso: {file}")
            print(self.df)
            return self.df
            
        except Exception as e:
            self.logger.error(f"Erro ao carregar o arquivo CSV {file}: {str(e)}")
            raise

    def web_one_input_json(self, file):
        """Carrega dados de um arquivo JSON em memória."""
        try:
            self.logger.info(f"Tentando carregar arquivo JSON: {file}")
            
            # Verificar se o arquivo existe
            if not os.path.exists(file):
                raise FileNotFoundError(f"O arquivo {file} não foi encontrado.")
            
            # Verificar se o arquivo está vazio
            if os.path.getsize(file) == 0:
                raise ValueError(f"O arquivo {file} está vazio.")
            
            # Tentar ler o arquivo
            self.df = duckdb.read_json(file)
            self.logger.info(f"Arquivo JSON carregado com sucesso: {file}")
            return self.df
            
        except Exception as e:
            self.logger.error(f"Erro ao carregar o arquivo JSON {file}: {str(e)}")
            raise