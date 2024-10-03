pipeline {
    agent any
    stages {
        stage("First Step") {
            steps {
                    sh """
                    export PYTHONPATH=${WORKSPACE}
                    pip3 install -r ${WORKSPACE}/requirements.txt
                    cd ${WORKSPACE}/git_branches/
                    python3.12 ${WORKSPACE}/git_branches/git_branch.py
                    """
            }
        }
    }
}
