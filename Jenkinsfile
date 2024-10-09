pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials' // Update with your actual credentials ID
        DOCKER_HUB_USERNAME = 'medkhaled1'                // Your Docker Hub username
        IMAGE_NAME = 'mysite_django'                      // Name of your Docker image
        DOCKER_HUB_REPO = "${DOCKER_HUB_USERNAME}/${IMAGE_NAME}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Medkhaled1/mysite.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_HUB_REPO}:latest")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy Application') {
            steps {
                // Add your deployment steps here
                echo 'Deploying application...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! Docker image pushed to Docker Hub and deployed.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
