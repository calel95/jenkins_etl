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
                    echo "Remover dados duplicados: ${params.remove_duplicates}"
                    echo "Remover dados nulos: ${params.remove_nulls}"
                }
            }
        }
        stage('ETL Process') {
            steps {
                script {
                    // Usar withFileParameter para acessar o arquivo temporário
                    withFileParameter('UPLOAD_FILE') {
                        def tempFile = env.UPLOAD_FILE // Caminho do arquivo temporário
                        echo "Caminho do arquivo temporário: ${tempFile}"
                        
                        // Executar o Python script com o caminho correto do arquivo
                        sh """
                        python -c "
from extract import Extract
from transform import Transform
extractor = Extract()
file_path = '${tempFile}'
df = extractor.web_one_input_${params.FILE_TYPE}(file_path)
transform = Transform(df)
"
                        """
                    }
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