from locust import TaskSet, task, HttpLocust

class ContentTasks(TaskSet):
    @task
    def get_contents(self):
        self.client.get('/content/')

    @task
    def get_content_with_slug(self):
        self.client.get('/content/nike-air/')


class ApiContent(HttpLocust):
    task_set = ContentTasks
    min_wait = 5000
    max_wait = 9000