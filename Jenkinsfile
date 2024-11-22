pipeline {
    agent any 

    // parameters {
    //     choice(name: 'TRANSFORMATIONS', choices: ['remove_duplicates', 'remove_nulls', 'last_position'], description: 'Escolha as transformações')
    //     string(name: 'NULL_COLUMNS', defaultValue: '', description: 'Colunas para remover nulos (separadas por vírgula)')
    //     string(name: 'ORDER_BY', defaultValue: '', description: 'Coluna para ordenar (última posição)')
    //     string(name: 'PARTITION_BY', defaultValue: '', description: 'Coluna para partição (última posição)')
    //     file(name: 'FILE', description: 'Caminho do arquivo CSV a ser processado')
    // }

    parameters {
        choice(
            name: 'FILE_TYPE',
            choices: ['csv', 'json'],
            description: 'Escolha o tipo de arquivo para carregar'
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
        stage('Carregando arquivo') {
            steps {
                // Clona o repositório Git
                sh " echo ${FILE}.${params.FILE_TYPE}"
                }           
        }
        stage('Preparar Ambiente') {
            steps {
                    // Instala dependências
                    sh 'pip install -r requirements.txt'
            }
        }
        stage('Executar ETL') {
            steps {
                script {
                    // Executar os scripts Python na pasta jenkins
                    sh "python transform.py --transformations='${TRANSFORMATIONS}' --null_columns='${NULL_COLUMNS}' --order_by='${ORDER_BY}' --partition_by='${PARTITION_BY}'"
                    sh 'python load.py'
                }
            }
        }
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