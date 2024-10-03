pipeline {
    agent any
    stages {
        stage("Install and Run") {
            steps {
                script {
                    // Create a virtual environment and install dependencies
                    sh """
                    python3.10 -m venv venv  # Create a virtual environment
                    echo 'Virtual environment created at: ${pwd}/venv'  # Debugging: show where the venv is located
                    ls -l venv/bin/             # Debugging: list contents of venv/bin to check for python
                    venv/bin/pip install --upgrade pip  # Upgrade pip in the virtual environment
                    venv/bin/pip install -r ${WORKSPACE}/git_branches/requirements.txt  # Install requirements
                    cd ${WORKSPACE}/git_branches/
                    ./venv/bin/python git_branch.py  # Run your Python script using the full path
                    """
                }
            }
        }
    }
}
