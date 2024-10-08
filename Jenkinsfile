pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'medkhaled1'                   // Your Docker Hub username
        IMAGE_NAME = 'mysite_django'                         // Name of your Docker image
        REGISTRY_URL = 'docker.io'                           // Docker Hub registry URL
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
                    // Build the Docker image using the Dockerfile in your repository
                    docker.build("${DOCKER_HUB_REPO}:latest")
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub using credentials stored in Jenkins
                    docker.withRegistry("https://${REGISTRY_URL}", 'docker-hub-credentials') {
                        // 'docker-hub-credentials' refers to the credentials ID created in Jenkins
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to your Docker Hub repository
                    docker.image("${DOCKER_HUB_REPO}:latest").push()
                }
            }
        }

        stage('Deploy Application') {
            steps {
                // Add deployment steps here (for example, running docker-compose on the server)
                echo "Deploying application..."
            }
        }
    }
}
