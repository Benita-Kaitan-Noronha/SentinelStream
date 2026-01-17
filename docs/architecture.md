```python
# sample code here
```python
def is_suspicious(transaction):
    if transaction.amount > 50000:
        return True
    if transaction.location != transaction.user_home_location:
        return True
    return False
```python
def validate_transaction(txn):
    assert txn.amount > 0
    assert txn.user_id is not None

