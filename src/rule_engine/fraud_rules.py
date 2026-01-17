# Rule-based fraud detection

def high_amount_rule(transaction):
    if transaction["amount"] > 100000:
        return True
    return False


def foreign_transaction_rule(transaction):
    if transaction["country"] != "India":
        return True
    return False
