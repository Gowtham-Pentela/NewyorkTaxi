pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Gowtham-Pentela/NewyorkTaxi.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pipeline') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    python pipeline/main.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    pytest tests/
                '''
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD Pipeline executed successfully.'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}
