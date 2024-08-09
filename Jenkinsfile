pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        // Environment variables are now taken directly from the global properties
        DB_USER = env.USER
        DB_PASSWORD = env.PASSWORD
        DB_ENDPOINT = env.ENDPOINT
        DB_PORT = env.PORT
        DB_NAME = env.DATABASE
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/muyiwao/APIPython.git', branch: 'main'
            }
        }
        stage('Set Up Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv ${VENV_DIR}'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate virtual environment, upgrade pip, and install dependencies
                    sh '''
                        source ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Application') {
            steps {
                script {
                    // Activate virtual environment and run the application
                    sh '''
                        source ${VENV_DIR}/bin/activate
                        export ENDPOINT=${DB_ENDPOINT}
                        export USER=${DB_USER}
                        export PASSWORD=${DB_PASSWORD}
                        export PORT=${DB_PORT}
                        export DATABASE=${DB_NAME}
                        python3 src/dbapi.py
                    '''
                }
            }
        }
    }
}
