pipeline {
    agent any
    parameters {
         //text(name: 'FILE', defaultValue: '', description: 'Enter some information about the person')
         stashedFile 'large'
    }
    stages {
       
        stage('STAGE 1'){
            steps{
            unstash 'large'
            sh 'cat large'
            }
        }

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
            sh 'python3 teste.py teste.txt blablabla'
            sh 'ls venv/bin'
                
            }    
        }
        stage('Encerrando'){
            steps{
                sh 'exit'
                sh 'echo Encerrou com sucesso'
            }
        }
        stage('Limpando workspace'){
            steps{
                cleanWs()
                sh 'ls'
                sh 'echo Limpou workspace'
            }   
        }
    }
}
