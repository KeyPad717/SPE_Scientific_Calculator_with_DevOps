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
            mail to: "keyworkmail2@gmail.com",
                 subject: "SUCCESS: Calculator Pipeline Update",
                 body: "The latest push to GitHub was successfully built and deployed. Check console output: ${env.BUILD_URL}"
        }
        failure {
            mail to: "keyworkmail2@gmail.com",
                 subject: "FAILURE: Calculator Pipeline Update",
                 body: "The pipeline failed. Please check the console output to debug: ${env.BUILD_URL}"
        }
    }
}