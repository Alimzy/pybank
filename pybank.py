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

def apply_interest(balance,rate,years):
    if rate < 0 and year < 1:
        raise ValueError("This is invalid input")
    interest = balance * (1 +rate)**years
    return interest

print(apply_interest(5000,123,1))


def get_transaction_summary(transactions):
    total_credits = 0
    total_debits = 0
    for transaction in transactions:
        if transaction[0] == "credit":
            total_credits += transaction[1]
        if transaction[0] == "debit":
            total_debits += transaction[1]
    net_balance = total_credits - total_debits
    transaction_count = len(transactions)
    output = [["total_credits", total_credits],["total_debits", total_debits],["net_balance",net_balance], ["transaction_count",transaction_count]]
    return output

transactions = [
["credit", 2000],
["debit", 500],
["credit", 300],
]
print(get_transaction_summary(transactions))

   


        

        
            
