pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t log-monitor .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag log-monitor itstechutsav/log-monitor'
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh 'docker push itstechutsav/log-monitor'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh '''
                    docker stop $(docker ps -q) || true 
                    docker rm $(docker ps -aq) || true
            '''
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 itstechutsav/log-monitor'
            }
        }
    }
}
