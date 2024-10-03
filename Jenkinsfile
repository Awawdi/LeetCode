pipeline {
    agent any
    stages {
        stage("Install and Run") {
            steps {
                script {
                    sh """
                    python3.10 -m venv venv
                    . venv/bin/activate
                    venv/bin/pip install --upgrade pip
                    venv/bin/pip install -r ${WORKSPACE}/requirements.txt
                    cd ${WORKSPACE}/git_branches/
                    venv/bin/python git_branch.py
                    """
                }
            }
        }
    }
}
