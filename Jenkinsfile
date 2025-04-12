pipeline {
    agent any

    environment {
        PYTHONPATH = '.'
        VENV_PATH = 'venv'
    }

    stages {
        stage('Set Up Virtual Environment') {
            steps {
                sh 'python3 -m venv $VENV_PATH'
                sh './$VENV_PATH/bin/pip install --upgrade pip'
                sh './$VENV_PATH/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './$VENV_PATH/bin/pytest tests/'
            }
        }

        stage('Run Pipeline') {
            steps {
                sh './$VENV_PATH/bin/python pipeline/main.py'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
