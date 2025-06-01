pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pytest-framework ./docker'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm -v $(pwd)/logs:/app/logs -v $(pwd)/reports:/app/reports pytest-framework'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*.txt', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}
