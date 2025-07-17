pipeline {
    agent any

    environment {
        IMAGE_NAME = "amazon-clone:${BUILD_NUMBER}"
    }

    options {
        skipStagesAfterUnstable()
    }

    stages {
        stage('Initialize') {
            steps {
                script {
                    notifyBuild('STARTED')
                }
            }
        }

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                        sh """
                            echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin
                            docker tag $IMAGE_NAME $DOCKERHUB_USER/amazon-clone:$BUILD_NUMBER
                            docker push $DOCKERHUB_USER/amazon-clone:$BUILD_NUMBER
                        """
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }

    post {
        success {
            script {
                notifyBuild('SUCCESSFUL')
            }
        }
        failure {
            script {
                notifyBuild('FAILED')
            }
        }
        unstable {
            script {
                notifyBuild('FAILED')
            }
        }
        aborted {
            script {
                notifyBuild('FAILED')
            }
        }
    }
}

def notifyBuild(String buildStatus) {
    def subject = "${buildStatus}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'"
    def summary = "${subject} (${env.BUILD_URL})"

    if (buildStatus == 'STARTED') {
        bitbucketStatusNotify buildState: 'INPROGRESS'
    } else if (buildStatus == 'SUCCESSFUL') {
        bitbucketStatusNotify buildState: 'SUCCESSFUL'
    } else {
        bitbucketStatusNotify buildState: 'FAILED'
    }
}
