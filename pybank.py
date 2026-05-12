def validate_email(email):
    isAt = False
    if len(email) < 8:
        return "inavalid email length. it must be at least eight character"
    for char in email:
        if char == "@":
            isAt = True
    if email[0] == "@":
        return "Email cannot start with '@'"    
    if isAt == False:
            return "Character must contain '@' symbol"

    return "Email is valid"

print(validate_email("@gmacom"))


def calculate_balance(transactions):
    account_balance = 0
    if len(transactions) == 0:
        return 0
    for transaction in transactions:
        if transaction < 0:
            account_balance -= transaction
        if transaction > 0:
            account_balance += transaction
        
    return account_balance

print(calculate_balance([6,3,7,-6])) 

def is_strong(password):
    if len(password) >= 8:
        return True
    return False
print(is_strong("mydfgrtyuh"))
        
            
