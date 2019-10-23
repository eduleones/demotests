## **Load Testing**

Load testing is a kind of Performance Testing which determines a system's performance under real-life load conditions.

### Lacust

`https://docs.locust.io/en/stable/`


Locust is an easy-to-use, distributed, user load testing tool. It is intended for load-testing web sites (or other systems) and figuring out how many concurrent users a system can handle.

The idea is that during a test, a swarm of locusts will attack your website. The behavior of each locust (or test user if you will) is defined by you and the swarming process is monitored from a web UI in real-time. This will help you battle test and identify bottlenecks in your code before letting real users in.


**Install:**

`pip install locustio`


**locust_script.py**
```
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
```

**Run Locust:**

`locust -f locust_script.py --host http://localhost:8000`

**Locust instance runs locally at:**

`http://localhost:8089/`

---
***[Next: Challenges](012_challenges.md)***