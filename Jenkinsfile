pipeline {
    agent any
    environment {
        DB_USER = "${env.USER}"
        DB_PASSWORD = "${env.PASSWORD}"
        DB_ENDPOINT = "${env.ENDPOINT}"
        DB_PORT = "${env.PORT}"
        DB_NAME = "${env.DATABASE}"
        FLASK_APP_PORT = '5310'  // Flask application port
        SERVER_IP = '18.132.73.146' // Replace with your server's public IP
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
                    // Build the Docker image
                    sh 'docker build -t flask-api-image .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Stop any existing container
                    sh '''
                        docker stop flask-api-container || true
                        docker rm flask-api-container || true
                    '''
                    // Run the Docker container
                    sh '''
                        docker run -d --name flask-api-container \
                        -e ENDPOINT=${DB_ENDPOINT} \
                        -e USER=${DB_USER} \
                        -e PASSWORD=${DB_PASSWORD} \
                        -e PORT=${DB_PORT} \
                        -e DATABASE=${DB_NAME} \
                        -p ${FLASK_APP_PORT}:${FLASK_APP_PORT} flask-api-image
                    '''
                }
            }
        }
    }
    post {
        success {
            script {
                // Output the full URL to access the Flask API
                def apiUrl = "http://${SERVER_IP}:${FLASK_APP_PORT}/data"
                echo "Build succeeded. The Flask API is running at ${apiUrl}"
            }
        }
        failure {
            script {
                echo 'Build failed. Cleaning up Docker resources.'
                sh '''
                    docker stop flask-api-container || true
                    docker rm flask-api-container || true
                    docker rmi flask-api-image || true
                '''
            }
        }
    }
}
