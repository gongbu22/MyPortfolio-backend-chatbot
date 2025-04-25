pipeline {
    agent any

    environment {
        DOCKER_IMAGE_OWNER = 'dangdang42'
        DOCKER_PWD = credentials('dockerhub')
    }

    stages {
        stage('clone from SCM') {
            steps {
                sh '''
                rm -rf MyPortfolio-backend-chatbot
                git clone https://github.com/gongbu22/MyPortfolio-backend-chatbot.git
                '''
            }
        }

        stage('Docker Image Building') {
            steps {
                dir('MyPortfolio-backend-chatbot') {
                    sh '''
                    docker build -t ${DOCKER_IMAGE_OWNER}/myportfolio-backend-chatbot:latest .
                    '''
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USR', passwordVariable: 'DOCKER_PWD')]) {
                sh "echo $DOCKER_PWD | docker login -u $DOCKER_USR --password-stdin"}
            }
        }

        stage('Docker Image pushing') {
            steps {
                sh '''
                docker push ${DOCKER_IMAGE_OWNER}/myportfolio-backend-chatbot:latest || true
                '''
            }
        }

        stage('Wait for Push Completion') {
            steps {
                script {
                    echo 'Waiting for Docker push to complete...'
                    sleep(30)
                }
            }
        }

        stage('Docker Logout') {
            steps {
                sh '''
                docker logout
                '''
            }
        }
    }
}