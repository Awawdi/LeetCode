pipeline {
    agent any
    stages {
        stage("First Step") {
            steps {
                    sh """
                    export PATH=\$PATH:/home/orsan/.local/bin
                    export PYTHONPATH=${WORKSPACE}
                    pip3.10 install -r ${WORKSPACE}/requirements.txt
                    cd ${WORKSPACE}/git_branches/
                    python3.10 ${WORKSPACE}/git_branches/git_branch.py
                    """
            }
        }
    }
}
