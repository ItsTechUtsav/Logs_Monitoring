pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t log-monitor .'
            }
        }

        stage('Tag Image') {
            steps {
                bat 'docker tag log-monitor itstechutsav/log-monitor'
            }
        }

        stage('Push to DockerHub') {
            steps {
                bat 'docker push itstechutsav/log-monitor'
            }
        }

        stage('Remove Old Container') {
            steps {
                bat '''
                    for /f %%i in ('docker ps -q') do docker stop %%i
                    for /f %%i in ('docker ps -aq') do docker rm %%i
            '''
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 itstechutsav/log-monitor'
            }
        }
    }
}