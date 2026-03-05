pipeline {
    agent any

    stages {

        stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/KeyPad717/SPE_Scientific_Calculator_with_DevOps.git'
    }
}

        stage('Install Dependencies') {
            steps {
                sh '''
        rm -rf venv
        python3 -m venv venv
        . venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/'
            }
        }

    }

    post {
        success {
            emailext(
                subject: "Build Failed: ${env.JOB_NAME}",
                body: "Build ${env.BUILD_NUMBER} failed. Check ${env.BUILD_URL}",
                to: "keyworkmail2@gmail.com"
            )
        }

        failure {
            emailext(
                subject: "Build Failed: ${env.JOB_NAME}",
                body: "Build ${env.BUILD_NUMBER} failed. Check ${env.BUILD_URL}",
                to: "keyworkmail2@gmail.com"
            )
        }

    }
}