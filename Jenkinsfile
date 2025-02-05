pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        DOCKER_IMAGE = "ramshaddev/flask-api:latest"
        DOCKER_TAG = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = "587"
        EMAIL_RECIPIENTS = "ramshadei@gmail.com"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Cloning repository from GitHub..."
                    checkout scm  // Automatically detects the correct branch
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "Installing dependencies..."
                    sh 'pip install -r requirements.txt'
                    echo "Building the Python project..."
                    sh 'python setup.py build || echo "No setup.py, skipping build"'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running unit tests..."
                    sh 'pytest --junitxml=report.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_PASSWORD')]) {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u your-dockerhub-username --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    }
                }
            }
        }

        stage('Trigger Downstream Job') {
            steps {
                script {
                    echo "Triggering downstream deployment job..."
                    build job: 'Downstream_Deployment_Job'
                }
            }
        }
    }
<<<<<<< HEAD
    post {
        success {
            // Output the full URL to access the Flask API
            echo "Build succeeded. The Flask API is running at http://${SERVER_IP}:${FLASK_APP_PORT}/data"
        }
    }
}


=======

    post {
        success {
            script {
                echo "Pipeline completed successfully!"
            }
            emailext(
                subject: "Jenkins Build SUCCESS: ${env.JOB_NAME}",
                body: "The Jenkins build ${env.BUILD_NUMBER} for ${env.JOB_NAME} has succeeded.\nView details: ${env.BUILD_URL}",
                to: "${EMAIL_RECIPIENTS}",
                from: "your-email@gmail.com"
            )
        }

        failure {
            script {
                echo "Pipeline failed!"
            }
            emailext(
                subject: "Jenkins Build FAILED: ${env.JOB_NAME}",
                body: "The Jenkins build ${env.BUILD_NUMBER} for ${env.JOB_NAME} has failed.\nCheck logs: ${env.BUILD_URL}",
                to: "${EMAIL_RECIPIENTS}",
                from: "ramshadei@gmail.com"
            )
        }
    }
}
>>>>>>> development
