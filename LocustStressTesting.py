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
            collectionId = collections[index]['id']
            elements = self.client.get("/api/collection/{}/elements".format(collectionId)).json()

            for elementIndex in elements:
                elementId = elements[elementIndex]['id']
                self.client.get("/api/collection/{}/element/{}".format(collectionId, elementId))

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