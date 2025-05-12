pipeline {
    agent any
    stages {
        stage('Instalar dependências') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Executar testes') {
            steps {
                sh 'pytest'
            }
        }
    }
}
