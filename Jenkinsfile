pipeline {
    agent { docker { image 'python:3.9.5' } }
    options {
        ansiColor('xterm')
    }
    stages {
        stage('Initialize') {
            steps {
                script {
                    def dockerHome = tool 'myDocker'
                    env.PATH = '${dockerHome}/bin:${env.PATH}'
                }
            }
        }
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'cd $HOME'
                sh 'mkdir -p shared'
                sh 'chmod 777 shared'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                }
            }
        stage('Test') {
            steps {
                    sh 'ls -l'
                    sh 'ls -l ./shared/'
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        sh 'rm -rf ./shared/* '
                        sh 'pytest -v ./tests/scenarios/ --rootdir=./tests/scenarios/ --alluredir ./shared/'
                    }
                    sh 'cd $HOME'
                    sh 'mkdir -p test-report'
                    sh 'chmod 777 test-report'
            }
        }
    }
    post {
        always {
            sh 'cd $HOME'
        }
    }
}