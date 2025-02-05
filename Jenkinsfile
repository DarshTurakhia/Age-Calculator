pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/DarshTurakhia/Age-Calculator.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 age_calculator.py'
            }
        }

        stage('Security Scan') {
            steps {
                sh './dependency-check/bin/dependency-check.sh --scan ./ --format HTML --out report.html'
                archiveArtifacts 'report.html'
            }
        }

        stage('Deploy to Target VM') {
            steps {
                sh 'scp -o StrictHostKeyChecking=no age_calculator.py darsh@10.0.1.7:~/'
            }
        }
    }
}
