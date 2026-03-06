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
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t key717/scientific-calculator:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push key717/scientific-calculator:latest'
            }
        }
        stage('Deploy with Ansible') {
    steps {
        sh 'ansible-playbook -i ansible/inventory ansible/deploy.yml'
    }
}

    }

   post {
    success {
        mail to: "keyworkmail2@gmail.com",
             subject: "SUCCESS: Scientific Calculator CI Pipeline",
             body: """

The Jenkins CI pipeline for the Scientific Calculator project has completed successfully.

Build Details:
Job Name      : ${env.JOB_NAME}
Build Number  : ${env.BUILD_NUMBER}
Build Status  : SUCCESS
Build URL     : ${env.BUILD_URL}

All automated unit tests passed and the latest code from the GitHub repository has been validated.

You can view the full build logs and test execution details at the link above.

"""
    }

    failure {
        mail to: "keyworkmail2@gmail.com",
             subject: "FAILURE: Scientific Calculator CI Pipeline",
             body: """

The Jenkins CI pipeline for the Scientific Calculator project has FAILED.

Build Details:
Job Name      : ${env.JOB_NAME}
Build Number  : ${env.BUILD_NUMBER}
Build Status  : FAILURE
Build URL     : ${env.BUILD_URL}

One or more stages in the pipeline failed during execution.
Please review the console output at the link above to identify the cause of the failure.

"""
    }
}
}