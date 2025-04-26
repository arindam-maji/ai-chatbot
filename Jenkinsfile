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
                    echo Stopping and removing existing container if it exists...
                    docker rm -f chatbot-container || echo "No existing container"

                    echo Running new container...
                    docker run -d --name chatbot-container -p 8501:8501 ai-chatbot

                    echo Showing running containers...
                    docker ps
                '''
            }
        }
    }
}
