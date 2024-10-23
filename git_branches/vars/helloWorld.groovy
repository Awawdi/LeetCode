def call(String name, String email_address) {
    if (isValidEmail(email_address)) {
        sh "echo hi ${name}, email is ${email_address}"
    }
    else {
        sh "echo Invalid email format: ${email_address}"
    }
}

def isValidEmail(String email) {

    def emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    return email ==~ emailPattern
}