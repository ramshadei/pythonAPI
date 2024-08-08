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
                        python3 src/dbapi.py
                    '''
                }
            }
        }
    }
}
