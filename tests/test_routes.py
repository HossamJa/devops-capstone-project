"""
Account API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from tests.factories import AccountFactory
from service.common import status  # HTTP Status Codes
from service.models import db, Account, init_db
from service.routes import app

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)

BASE_URL = "/accounts"


######################################################################
#  T E S T   C A S E S
######################################################################
class TestAccountService(TestCase):
    """Account Service Tests"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        init_db(app)

    @classmethod
    def tearDownClass(cls):
        """Runs once before test suite"""

    def setUp(self):
        """Runs before each test"""
        db.session.query(Account).delete()  # clean up the last tests
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Runs once after each test case"""
        db.session.remove()

    ######################################################################
    #  H E L P E R   M E T H O D S
    ######################################################################

    def _create_accounts(self, count):
        """Factory method to create accounts in bulk"""
        accounts = []
        for _ in range(count):
            account = AccountFactory()
            response = self.client.post(BASE_URL, json=account.serialize())
            self.assertEqual(
                response.status_code,
                status.HTTP_201_CREATED,
                "Could not create test Account",
            )
            new_account = response.get_json()
            account.id = new_account["id"]
            accounts.append(account)
        return accounts

    ######################################################################
    #  A C C O U N T   T E S T   C A S E S
    ######################################################################

    def test_index(self):
        """It should get 200_OK from the Home Page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_health(self):
        """It should be healthy"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["status"], "OK")

    def test_create_account(self):
        """It should Create a new Account"""
        account = AccountFactory()
        response = self.client.post(
            BASE_URL,
            json=account.serialize(),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Make sure location header is set
        location = response.headers.get("Location", None)
        self.assertIsNotNone(location)

        # Check the data is correct
        new_account = response.get_json()
        self.assertEqual(new_account["name"], account.name)
        self.assertEqual(new_account["email"], account.email)
        self.assertEqual(new_account["address"], account.address)
        self.assertEqual(new_account["phone_number"], account.phone_number)
        self.assertEqual(new_account["date_joined"], str(account.date_joined))

    def test_bad_request(self):
        """It should not Create an Account when sending the wrong data"""
        response = self.client.post(BASE_URL, json={"name": "not enough data"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsupported_media_type(self):
        """It should not Create an Account when sending the wrong media type"""
        account = AccountFactory()
        response = self.client.post(
            BASE_URL,
            json=account.serialize(),
            content_type="test/html"
        )
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    # Tes Read Accounts
    def test_read_account(self):
        """It Should Retrive Account info by ID"""
        test_accounts = self._create_accounts(3)
        response1 = self.client.get(f"{BASE_URL}/{test_accounts[0].id}")
        response2 = self.client.get(f"{BASE_URL}/{test_accounts[1].id}")
        response3 = self.client.get(f"{BASE_URL}/{test_accounts[2].id}")
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)

        resp_data1 = response1.get_json()
        resp_data2 = response2.get_json()
        resp_data3 = response3.get_json()
        self.assertEqual(resp_data1["name"], test_accounts[0].name)
        self.assertEqual(resp_data2["name"], test_accounts[1].name)
        self.assertEqual(resp_data3["name"], test_accounts[2].name)

    def test_read_account_not_found(self):
        """It Should Return 404 ERROR & Not Found Message """
        response = self.client.get(f"{BASE_URL}/0")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        resp_data = response.get_json()
        self.assertIn("was not found", resp_data["message"])

    def test_update_accounts(self):
        """ It Should Update an Existing Account and return 200 status code"""
        # Create a Test account
        test_account = AccountFactory()
        logging.debug("Test account: %s", test_account.serialize())
        response = self.client.post(BASE_URL, json=test_account.serialize())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Update The test account
        new_account = response.get_json()
        new_account["name"] = "test case for update an account"
        update_resp = self.client.put(f"{BASE_URL}/{new_account['id']}", json=new_account)
        self.assertEqual(update_resp.status_code, status.HTTP_200_OK)
        data = update_resp.get_json()
        self.assertEqual(data["name"], "test case for update an account")

    def test_update_account_not_found(self):
        """It should not Updtae an account thats not found"""
        # Create a non existed account
        non_account = {
            "id": 0,
            "name": "name",
            "email": "name@address.com",
            "address": "street 5, town 2, country3",
            "phone_number": "0625315232",
            "date_joined": "08-08-2025"
        }
        response = self.client.put(f"{BASE_URL}/{non_account['id']}", json=non_account)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = response.get_json()
        self.assertIn("was not found", data["message"])
