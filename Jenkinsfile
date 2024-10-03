pipeline {
    agent any
    stages {
        stage("First Step") {
            steps {
                    sh """
                    export PYTHONPATH=${WORKSPACE}
                    pip3.10 install --user -r ${WORKSPACE}/requirements.txt
                    cd ${WORKSPACE}/git_branches/
                    python3.10 ${WORKSPACE}/git_branches/git_branch.py
                    """
            }
        }
    }
}
