pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        DB_USER = "${env.USER}"
        DB_PASSWORD = "${env.PASSWORD}"
        DB_ENDPOINT = "${env.ENDPOINT}"
        DB_PORT = "${env.PORT}"
        DB_NAME = "${env.DATABASE}"
        DOCKER_IMAGE = 'muyiwao/flask-api:latest'
        FLASK_APP_PORT = '5310'
        SERVER_IP = '18.132.73.146' // Replace with your server's public IP
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
        stage('Run Tests') {
            steps {
                script {
                    // Activate virtual environment and run pytest
                    sh '''
                        source ${VENV_DIR}/bin/activate
                        pytest test_app.py --junitxml=test-results.xml
                    '''
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'muyiwa-hub', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh 'echo ${DOCKER_HUB_PASSWORD} | docker login -u ${DOCKER_HUB_USERNAME} --password-stdin'
                    }
                    // Push the image
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
        /*stage('Deploy to Kubernetes') {
            steps {
                script {
                    //sh '''
                    //kubectl apply -f k8s/deployment.yaml
                    //kubectl apply -f k8s/service.yaml
                    //'''
                }
            }
        }*/
    }
    post {
        always {
            script {
                // Clean up Docker images
                sh 'docker rmi ${DOCKER_IMAGE}'
            }
        }
        success {
            script {
                // Output the full URL to access the Flask API
                def apiUrl = "http://${SERVER_IP}:${FLASK_APP_PORT}/data"
                echo "Build succeeded. The Flask API is running at ${apiUrl}"
            }
        }
    }
}
