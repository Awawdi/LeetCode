pipeline {
    agent any
    stages {
        stage("First Step") {
            steps {
                    sh """
                    export PYTHONPATH=${WORKSPACE}
                    cd ${WORKSPACE}/LeetCode/
                    python3.9 ${WORKSPACE}/LeetCode/git_branch.py"
                    """
            }
        }
    }
}
