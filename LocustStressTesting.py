from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task
    def index(self):
        self.client.get("/")

class MobileBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task
    def collections(self):
        self.client.get("/api/collections")

class ManagerBehavior(TaskSet):
    @task
    def collection(self):
        collections = self.client.get("/api/collections").json()
        for index in collections:
            self.client.get("/api/collection/{}".format(collections[index]['id']))

class UserTesting(HttpLocust):
    task_set = MobileBehavior
    min_wait = 1000
    max_wait = 2000

class AndroidTesting(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 8000

class BlackberryTesting(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 20000

class ManagerTesting(HttpLocust):
    task_set = ManagerBehavior
    min_wait = 3000
    max_wait = 20000

# locust -f LocustStressTesting.py --host=http://lte.try
# http://lte.try:8089/