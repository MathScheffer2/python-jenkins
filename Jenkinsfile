pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps{
            checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MathScheffer2/python-jenkins.git']])    
            sh 'ls'
            }
        }
        stage("start environment") {
            steps{
            sh 'python3 -m venv venv'
            sh '. venv/bin/activate'
            sh 'pip install -r requirements.txt'
            sh 'python3 teste.py blablabla'
            sh 'ls venv/bin'
            sh 'exit'
                
            }    
        }
    }
}
