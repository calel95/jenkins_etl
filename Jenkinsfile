pipeline {
    agent any 

    parameters {
        // ... outros parâmetros ...
        file(name: 'FILE', description: 'Selecione o arquivo CSV')
    }

    stages {
        stage('Executar ETL') {
            steps {
                script {
                    // Obtém o caminho completo do workspace
                    def workspace = "${env.WORKSPACE}"

                    // Obtém o nome do arquivo (pode ser personalizado)
                    def fileName = params.FILE.name

                    // Concatena o caminho do workspace com o nome do arquivo
                    def filePath = "${workspace}/${fileName}"

                    sh "python extract.py ${filePath}"
                    sh "python transform.py --transformations='${params.TRANSFORMATIONS}' --null_columns='${params.NULL_COLUMNS}' --order_by='${params.ORDER_BY}' --partition_by='${params.PARTITION_BY}'"
                    sh 'python load.py'
                }
            }
        }
    }
}