pipeline {
    agent any
    stages {
        stage("Install and Run") {
            steps {
                script {
                    sh """
                    python3.10 -m venv venv
                    source venv/bin/activate
                    pip install -r ${WORKSPACE}/requirements.txt
                    cd ${WORKSPACE}/git_branches/
                    python git_branch.py
                    """
                }
            }
        }
    }
}
