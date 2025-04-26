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
                bat 'docker build -t ai-chatbot .'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests configured yet.'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8501:8501 ai-chatbot'
            }
        }
    }
}
