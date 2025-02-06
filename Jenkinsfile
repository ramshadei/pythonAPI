pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        VENV_DIR = 'venv'
        DOCKER_IMAGE = "ramshaddev/flask-api"
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
                    echo "Building Docker image..."
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials-rams', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                        sh "docker push ${IMAGE_NAME}"
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

    post {
        success {
            script {
                echo "Pipeline completed successfully!"
            }
            emailext(
                subject: "Jenkins Build SUCCESS: ${env.JOB_NAME}",
                body: "The Jenkins build ${env.BUILD_NUMBER} for ${env.JOB_NAME} has succeeded.\nView details: ${env.BUILD_URL}",
                to: "${EMAIL_RECIPIENTS}",
                from: "ramshadei@gmail.com"
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
