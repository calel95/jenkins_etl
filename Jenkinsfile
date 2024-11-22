pipeline {
    agent any 
    parameters {
        choice(
            name: 'FILE_TYPE',
            choices: ['csv', 'json'],
            description: 'Escolha o tipo de arquivo para carregar'
        )
        file(
            name: 'UPLOAD_FILE',
            description: 'Faça o upload do arquivo CSV ou JSON'
        )
        booleanParam(
            name: 'remove_duplicates',
            defaultValue: false,
            description: 'Remove dados duplicados'
        )
        booleanParam(
            name: 'remove_nulls',
            defaultValue: false,
            description: 'Remove dados nulos'
        )

        string(
            name: 'TRANSFORM_PARAMS',
            defaultValue: '',
            description: 'Parâmetros adicionais para transformações (JSON format ex: {"null_columns": ["col1", "col2"]})'
        )
    }
    stages {
        stage('Exibir parâmetros') {
            steps {
                script {
                    echo "Removido dados duplicados: ${params.remove_duplicates}"
                    echo "Removido dados nulos: ${params.remove_nulls}"
                }
            }
        }
        stage('Preparar Ambiente') {
            steps {
                    // Instala dependências
                    script {
                    sh 'pip install -r requirements.txt'
                    }
            }
        }
        stage('Check Workspace') {
            steps {
                script {
                sh 'ls -lh ${WORKSPACE}'
                }
            }
        }
        stage('Extract') {
            steps {
                script {
                    echo "Carregando arquivo: ${UPLOAD_FILE}"
                    sh """
                    python -c "
from extract import Extract
extractor = Extract()
df = extractor.web_one_input_${params.FILE_TYPE}('${WORKSPACE}/${UPLOAD_FILE}')
print('Arquivo processado com sucesso.')
"
                    """
                }
            }
        }
        // stage('Executar ETL') {
        //     steps {
        //         script {
        //             // Executar os scripts Python na pasta jenkins
        //             sh "python transform.py --transformations='${TRANSFORMATIONS}' --null_columns='${NULL_COLUMNS}' --order_by='${ORDER_BY}' --partition_by='${PARTITION_BY}'"
        //             sh 'python load.py'
        //         }
        //     }
        // }
    }
    post {
        success {
            echo 'ETL executado com sucesso!'
        }
        failure {
            echo 'Falha na execução do ETL.'
        }
    }
}