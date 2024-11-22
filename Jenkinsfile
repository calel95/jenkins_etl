pipeline {
    agent any

    parameters {
        choice(
            name: 'FILE_TYPE',
            choices: ['csv', 'json'],
            description: 'Escolha o tipo de arquivo para carregar'
        )
        string(
            name: 'FILE_NAME',
            defaultValue: 'example',
            description: 'Digite o nome do arquivo (sem extensão)'
        )
        choice(
            name: 'TRANSFORMATIONS',
            choices: ['remove_duplicates', 'remove_nulls', 'last_position', 'first_position'],
            description: 'Escolha uma ou mais transformações (separadas por vírgulas)'
        )
        string(
            name: 'TRANSFORM_PARAMS',
            defaultValue: '',
            description: 'Parâmetros adicionais para transformações (JSON format ex: {"null_columns": ["col1", "col2"]})'
        )
    }

    stages {
        stage('Extract') {
            steps {
                script {
                    echo "Carregando arquivo: ${params.FILE_NAME}.${params.FILE_TYPE}"
                    sh """
                    python -c "
from extract import Extract
extractor = Extract()
df = extractor.web_one_input_${params.FILE_TYPE}('data/${params.FILE_TYPE}/${params.FILE_NAME}.${params.FILE_TYPE}')
df.to_parquet('data/tmp/etl_stage.parquet')"
                    """
                }
            }
        }
        stage('Transform') {
            steps {
                script {
                    echo "Aplicando transformações: ${params.TRANSFORMATIONS}"
                    sh """
                    python -c "
import json
from transform import Transform
import pandas as pd

df = pd.read_parquet('data/tmp/etl_stage.parquet')
transformer = Transform(df)
options = json.loads('${params.TRANSFORM_PARAMS}')
for transformation in '${params.TRANSFORMATIONS}'.split(','):
    if hasattr(transformer, transformation):
        transformer.df = getattr(transformer, transformation)(**options)
transformer.df.to_parquet('data/tmp/etl_transformed.parquet')"
                    """
                }
            }
        }
        stage('Load') {
            steps {
                script {
                    echo "Salvando resultado transformado em Parquet"
                    sh """
                    python -c "
from load import Load
import pandas as pd

df = pd.read_parquet('data/tmp/etl_transformed.parquet')
loader = Load(df)
loader.save_parquet_table('final_result')"
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado!"
        }
    }
}
