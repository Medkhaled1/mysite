pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'  // Your Docker Hub credentials ID
        DOCKER_HUB_USERNAME = 'medkhaled1'                 // Docker Hub username
        IMAGE_NAME = 'mysite_django'                       // Name of your Docker image
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
                sshagent(['server-ssh-credentials']) {  // Your SSH credentials ID
                    sh '''
                    ssh -o StrictHostKeyChecking=no user@your_server_ip << EOF
                        cd /path/to/your/deployment

                        # Pull the latest Docker image from Docker Hub
                        docker-compose down  # Stop running containers
                        docker-compose pull  # Pull the latest image
                        docker-compose up -d --build  # Start the new containers
                    EOF
                    '''
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    def response = sh(script: "curl -s -o /dev/null -w '%{http_code}' http://your_domain_or_ip", returnStdout: true)
                    if (response != '200') {
                        error "Deployment failed! Health check returned ${response}"
                    }
                }
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
