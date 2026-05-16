from locust import HttpUser, task, between

class SREAppUser(HttpUser):
    wait_time = between(0.5, 2)

    @task(3)
    def get_home(self):
        self.client.get("/")

    @task(1)
    def get_health(self):
        self.client.get("/health")
