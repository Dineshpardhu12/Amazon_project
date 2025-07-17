pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-repo/amazon-clone.git'
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
                    sh 'docker tag amazon-clone yourdockerhub/amazon-clone'
                    sh 'docker push yourdockerhub/amazon-clone'
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
