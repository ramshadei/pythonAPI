pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        ENDPOINT = credentials('DB_ENDPOINT')
        USER = credentials('DB_USER')
        PASSWORD = credentials('DB_PASSWORD')
        PORT = credentials('DB_PORT')
        DATABASE = credentials('DB_NAME')
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/muyiwao/APIPython.git', branch: 'main'
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    // Create and activate virtual environment, then install dependencies
                    sh 'python3 -m venv $VENV_DIR'
                    sh '. $VENV_DIR/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    // Run your Python script with the virtual environment activated
                    sh '. $VENV_DIR/bin/activate && python src/dbapi.py'
                }
            }
        }
    }
    post {
        always {
            script {
                // Clean up the virtual environment (optional)
                sh 'rm -rf $VENV_DIR'
            }
        }
    }
}
