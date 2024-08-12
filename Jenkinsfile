pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        DB_USER = "${env.USER}"
        DB_PASSWORD = "${env.PASSWORD}"
        DB_ENDPOINT = "${env.ENDPOINT}"
        DB_PORT = "${env.PORT}"
        DB_NAME = "${env.DATABASE}"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/muyiwao/APIPython.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flask-api-container .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any existing container
                    sh '''
                        docker stop flask-api-container || true
                        docker rm flask-api-container || true
                    '''

                    // Run the Docker container with environment variables for database credentials
                    sh '''
                        docker run -d \
                            -p 5000:5000 \
                            --name flask-api-container \
                            -e DB_USER=${DB_USER} \
                            -e DB_PASSWORD=${DB_PASSWORD} \
                            -e DB_ENDPOINT=${DB_ENDPOINT} \
                            -e DB_PORT=${DB_PORT} \
                            -e DB_NAME=${DB_NAME} \
                            flask-api-container
                    '''
                }
            }
        }
    }
}
