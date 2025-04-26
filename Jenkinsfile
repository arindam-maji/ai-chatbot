pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/arindam-maji/ai-chatbot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    echo Building Docker image...
                    docker build -t ai-chatbot .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests configured yet.'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    echo Checking if container is already running...
                    docker ps -a

                    echo Removing existing container if it exists...
                    docker rm -f chatbot-container || echo "No container to remove"

                    echo Attempting to run new Docker container...
                    docker run -d --name chatbot-container -p 8501:8501 ai-chatbot

                    echo List of running containers:
                    docker ps
                '''
    }
}

    }
}
