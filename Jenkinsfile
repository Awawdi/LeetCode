pipeline {
    agent any
    stages {
        stage("First Step") {
            steps {
                    sh """
                    export PYTHONPATH=${WORKSPACE}
                    cd ${WORKSPACE}/git_branches/
                    python3.9 ${WORKSPACE}/git_branches/git_branch.py"
                    """
            }
        }
    }
}
