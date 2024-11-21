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
                    // Verifica se o arquivo foi selecionado
                    if (params.FILE) {
                        // Obtém o caminho completo do arquivo
                        def filePath = "${env.WORKSPACE}/${params.FILE.name}"

                        // Executa os scripts Python
                        sh "python extract.py ${filePath}"
                        sh "python transform.py --transformations='${params.TRANSFORMATIONS}' --null_columns='${params.NULL_COLUMNS}' --order_by='${params.ORDER_BY}' --partition_by='${params.PARTITION_BY}'"
                        sh 'python load.py'
                    } else {
                        echo 'Nenhum arquivo foi selecionado.'
                    }
                }
            }
        }
    }
}