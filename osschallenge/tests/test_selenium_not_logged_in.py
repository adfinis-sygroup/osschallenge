from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.test import Client
from osschallenge.tests.pages.register import RegisterPage
from osschallenge.models import User, Profile, Role


class MydriverTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(self):
        super(MydriverTests, self).setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)

    @classmethod
    def setUp(self):
        self.client = Client()
        self.register_page = RegisterPage(self.driver, self.live_server_url)

        self.role1 = Role.objects.create(
            id=1,
            name="Contributor"
        )

        self.user1 = User.objects.create(
            last_login="2017-10-18 11:55:45.681893+00",
            is_superuser=False,
            username="Test",
            first_name="Test",
            last_name="Test",
            email="example@example.ch",
            is_staff=False,
            is_active=True,
            date_joined="2017-10-13 08:17:36.901715+00"
        )
        self.user1.set_password("12345qwert")
        self.user1.save()

        self.profile1 = Profile.objects.create(
            user=self.user1,
            role=self.role1,
            links="Test",
            contact="Test",
            key="Test1",
            picture="Test.png"
        )

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        super(MydriverTests, self).tearDownClass()

    def test_register_successful(self):
        self.register_page.open()
        self.register_page.register(
            "myuser",
            "foo",
            "bar",
            "abc@example.ch",
            "12345qwert",
            "12345qwert"
        )
        user = User.objects.get(username="myuser")
        self.assertEqual(user.username, "myuser")
        self.assertEqual(user.first_name, "foo")
        self.assertEqual(user.last_name, "bar")
        self.assertEqual(user.email, "abc@example.ch")

    def test_register_name_already_taken(self):
        self.register_page.open()
        self.register_page.register(
            "Test",
            "foo",
            "bar",
            "abc@example.ch",
            "12345qwert",
            "12345qwert"
        )
        self.assertRaises(AssertionError)

    def test_register_email_already_taken(self):
        self.register_page.open()
        self.register_page.register(
            "myuser",
            "foo",
            "bar",
            "example@example.ch",
            "12345qwert",
            "12345qwert"
        )
        self.assertRaises(AssertionError)

    def test_register_passwords_do_not_match(self):
        self.register_page.open()
        self.register_page.register(
            "myuser",
            "foo",
            "bar",
            "example@example.ch",
            "12345qwert",
            "qwert12345"
        )
        self.assertRaises(AssertionError)
