pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '9bc9dd80-9872-4b37-a2cf-116235365b6f', url: 'https://github.com/roshan-singh-qa/Pytest-web-automation']]])
            }
        }
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'pytest -v -s'
            }
        }
        stage('WithEnv-Script') {
           steps {
               withEnv(["VALUE=${VALUE}", 'FILENAME=foofile']) {
                   echo "$VALUE"
               }
           }
       }
        stage('Generate Report'){
           steps{

           }
       }
       stage('Teams Notification'){
           steps{

           }
       }
    }
}

