pipeline {
    stages {
        stage("Change license capacity") {
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
