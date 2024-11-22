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
                    echo "Nome do arquivo carregado: ${UPLOAD_FILE}"
                    echo "Caminho completo do arquivo: <span class="math-inline">\{WORKSPACE\}/</span>{UPLOAD_FILE}"
                }
            }
        }
        stage('Preparar Ambiente') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Check before Workspace') {
            steps {
                script {
                    sh 'ls -lh <span class="math-inline">\{WORKSPACE\}'
\}
\}
\}
stage\('Extract'\) \{
steps \{
script \{
def file\_path \= "</span>{WORKSPACE}/${UPLOAD_FILE}"  // Assuming file goes into workspace root

                    echo "Nome do arquivo carregado: ${UPLOAD_FILE}"
                    echo "Caminho completo: ${file_path}"
                    sh 'ls -lh <span class="math-inline">\{WORKSPACE\}'
sh """
python \-c "
from extract import Extract
extractor \= Extract\(\)
if not os\.path\.exists\('</span>{file_path}'):
                        print('Erro: Arquivo não encontrado!')
                        exit(1)  # Exit with non-zero code to indicate failure

                    try:
                        if params.FILE_TYPE == 'csv':
                            df = extractor.web_one_input_csv('<span class="math-inline">\{file\_path\}'\)
else\:
df \= extractor\.web\_one\_input\_json\('</span>{file_path}')  # Update if needed
                        print('Arquivo processado com sucesso.')
                    except Exception as e:
                        print(f'Erro ao processar o arquivo: {e}')
                        exit(1)
                    "
                    """
                }
            }
        }
        // stage('Executar ETL') {
        //     // ...
        // }
    }

    post {
        success {
            echo 'ETL executado com sucesso!'
        }
        failure {