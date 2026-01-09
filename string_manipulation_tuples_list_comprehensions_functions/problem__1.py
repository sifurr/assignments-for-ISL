def email_validator(email_address):
    if len(email_address) > 4 and "@" in email_address:
        (username, domain) = email_address.strip().lower().split("@")
        
        return username, domain
    
    return "Please provide a valid email address!"


user_input = input("Enter email address: ")
extracted_email = email_validator(user_input)
print(extracted_email)
