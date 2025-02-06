pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/DarshTurakhia/Age-Calculator'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 Age.py'
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
                sh 'scp -o StrictHostKeyChecking=no Age.py darsh@10.0.1.7:~/'
            }
        }
    }
}
