from locust import task, TaskSet, between


class SystemManage(TaskSet):

    @task
    def task1(self):
        self.client.get("carRental/sys/toUserManager.action")

    @task
    def task1(self):
        self.client.get("carRental/sys/toRoleManager.action")

    @task
    def task1(self):
        self.client.get("carRental/sys/toLogInfoManager.action")

class BasicManage(TaskSet):
    @task
    def task1(self):
        self.client.get("carRental/sys/toCustomerManager.action")

    @task
    def task1(self):
        self.client.get("carRental/sys/toCarManager.action")

class CarRentalTest:
    wait_time = between(1,3)
    tasks = [BasicManage,SystemManagey]