def call(Map config = [:]) {
    def email_address = config.email_address

    if (!isValidEmail(email_address)) {
         error "Invalid email format: ${email_address}"
         }
    }


def isValidEmail(String email) {

    def emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    return email ==~ emailPattern
}