pipeline {
    agent any 
    parameters {
        choice(
            name: 'FILE_TYPE',
            choices: ['csv', 'json'],
            description: 'Escolha o tipo de arquivo para carregar'
        )
        base64File(
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
                    echo "Nome do arquivo carregado: ${UPLOAD_FILE}"
                    echo "Caminho completo do arquivo: ${WORKSPACE}/${UPLOAD_FILE}"
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
        stage('Check before Workspace') {
            steps {
                script {
                sh 'ls -lh ${WORKSPACE}'
                sh "mv ${WORKSPACE}/${UPLOAD_FILE} ${WORKSPACE}/uploaded_file.${params.FILE_TYPE}"
                }
            }
        }
        stage('teste stage') {
            steps {
                script {
                    // Mover ou copiar o arquivo para a pasta workspace
                    withFileParameter('UPLOAD_FILE') {
                    sh 'cat $UPLOAD_FILE'
                    }
                }
            }
        }
        stage('Extract') {
            steps {
                script {
                    echo "Nome do arquivo carregado: ${UPLOAD_FILE}"
                    echo "Caminho completo: ${WORKSPACE}/${UPLOAD_FILE}"
                    sh 'ls -lh ${WORKSPACE}'
                    sh """
                    python -c "
from extract import Extract
extractor = Extract()
file_path = '${WORKSPACE}/${UPLOAD_FILE}'
print(f'Carregando o arquivo: {file_path}')
df = extractor.web_one_input_${params.FILE_TYPE}(file_path)
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