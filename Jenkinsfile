pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/muyiwao/APIPython.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    // Run your Python script
                    sh 'python src/pythonPostgress.py'
                }
            }
        }
    }
}
