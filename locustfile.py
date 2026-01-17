from locust import HttpUser, task, between

class TransactionUser(HttpUser):
    wait_time = between(0.01, 0.02)

    @task
    def send_transaction(self):
        self.client.post(
            "/transaction",
            params={"user_id": 1, "amount": 100.0}
        )
