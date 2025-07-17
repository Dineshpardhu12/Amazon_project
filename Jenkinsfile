pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Dineshpardhu12/Amazon_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t amazon-clone:latest .'
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    sh 'docker tag amazon-clone dineshpardhu1/java'
                    sh 'docker push dineshpardhu1/java'
                }
            }
        }

        stage('Deploy to Kind') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
