from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get(url="/")

    @task
    def showSummary_SimplyLift(self):
        self.client.post(url="/showSummary", data={
            'email': 'john@simplylift.co'
        })

    @task
    def showSummary_IronTemple(self):
        self.client.post(url="/showSummary", data={
            'email': 'admin@irontemple.com'
        })

    @task
    def showSummary_SheLifts(self):
        self.client.post(url="/showSummary", data={
            'email': 'kate@shelifts.co.uk'
        })

    @task
    def purchasePlaces_SimplyLift_SpringFestival(self):
        self.client.post(url="/purchasePlaces", data={
            'club': 'Simply Lift',
            'competition': 'Spring Festival',
            'places': '1'
        })

    @task
    def purchasePlaces_SimplyLift_FallClassic(self):
        self.client.post(url="/purchasePlaces", data={
            'club': 'Simply Lift',
            'competition': 'Fall Classic',
            'places': '1'
        })

    @task
    def purchasePlaces_IronTemple_SpringFestival(self):
        self.client.post(url="/purchasePlaces", data={
            'club': 'Iron Temple',
            'competition': 'Spring Festival',
            'places': '1'
        })

    @task
    def purchasePlaces_IronTemple_FallClassic(self):
        self.client.post(url="/purchasePlaces", data={
            'club': 'Iron Temple',
            'competition': 'Fall Classic',
            'places': '1'
        })

    @task
    def purchasePlaces_SheLifts_SpringFestival(self):
        self.client.post(url="/purchasePlaces", data={
            'club': 'She Lifts',
            'competition': 'Spring Festival',
            'places': '1'
        })

    @task
    def purchasePlaces_SheLifts_FallClassic(self):
        self.client.post(url="/purchasePlaces", data={
            'club': 'She Lifts',
            'competition': 'Fall Classic',
            'places': '1'
        })
