pipeline {
    agent any 

    parameters {
        choice(name: 'TRANSFORMATIONS', choices: ['remove_duplicates', 'remove_nulls', 'last_position'], description: 'Escolha as transformações')
        string(name: 'NULL_COLUMNS', defaultValue: '', description: 'Colunas para remover nulos (separadas por vírgula)')
        string(name: 'ORDER_BY', defaultValue: '', description: 'Coluna para ordenar (última posição)')
        string(name: 'PARTITION_BY', defaultValue: '', description: 'Coluna para partição (última posição)')
        file(name: 'FILE', description: 'Caminho do arquivo CSV a ser processado')
    }

    stages {
        stage('Carregando arquivo') {
            steps {
                // Clona o repositório Git
                //sh "python extract.py ${params.FILE}"
                script {
                    // Lê o conteúdo do arquivo CSV
                    def csvContent = readFile(file: params.FILE)
                    echo "Registro: ${csvContent}"
                    // Exemplo de processamento dos dados                      
                    }
                }
            
        }
        stage('Preparar Ambiente') {
            steps {
                script {
                    // Instala dependências
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Executar ETL') {
            steps {
                script {
                    // Executar os scripts Python na pasta jenkins
                    sh "python transform.py --transformations='${params.TRANSFORMATIONS}' --null_columns='${params.NULL_COLUMNS}' --order_by='${params.ORDER_BY}' --partition_by='${params.PARTITION_BY}'"
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