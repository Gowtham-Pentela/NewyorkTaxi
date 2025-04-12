pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}" // Add the workspace root to PYTHONPATH
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Prepare Data Directory') {
            steps {
                sh 'mkdir -p data' // Create the 'data' directory if it doesn't exist
            }
        }

        stage('Download Data') {
            steps {
                sh './venv/bin/python -c "import requests; url=\'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet\'; r=requests.get(url); open(\'data/yellow_tripdata_2023-01.parquet\', \'wb\').write(r.content)"'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest tests/'
            }
        }

        stage('Run Pipeline') {
            when {
                expression {
                    currentBuild.result != 'FAILURE'
                }
            }
            steps {
                sh './venv/bin/python pipeline/main.py'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}