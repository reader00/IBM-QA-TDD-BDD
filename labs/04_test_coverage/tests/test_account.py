"""
Test Cases TestAccountModel
"""
import json
from random import randrange
from unittest import TestCase
from models import db
from models.account import Account, DataValidationError

ACCOUNT_DATA = {}


class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        db.create_all()  # make our sqlalchemy tables
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnext from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        self.rand = randrange(0, len(ACCOUNT_DATA))
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_all_accounts(self):
        """ Test creating multiple Accounts """
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))

    def test_create_an_account(self):
        """ Test Account creation using known data """
        data = ACCOUNT_DATA[self.rand]  # get a random account
        account = Account(**data)
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_represent_as_string(self):
        """ Test representing an account as a string """
        account = Account(name="Qory")
        self.assertEqual(str(account), "<Account 'Qory'>")

    def test_ro_dict(self):
        """ Test account to dictionary """
        account = Account(**ACCOUNT_DATA[self.rand])
        account_dict = account.to_dict()
        self.assertEqual(account_dict["name"], account.name)
        self.assertEqual(account_dict["email"], account.email)
        self.assertEqual(account_dict["phone_number"], account.phone_number)
        self.assertEqual(account_dict["disabled"], account.disabled)

    def test_from_dict(self):
        """ Test account data from dictionary """
        account_data = ACCOUNT_DATA[self.rand]
        account = Account()
        account.from_dict(account_data)

        self.assertEqual(account.name, account_data["name"])
        self.assertEqual(account.email, account_data["email"])
        self.assertEqual(account.phone_number, account_data["phone_number"])
        self.assertEqual(account.disabled, account_data["disabled"])

    def test_add_from_dict(self):
        """ Test add account data from dictionary """
        account = Account(**ACCOUNT_DATA[self.rand])
        additional_attribute = {
            "age": randrange(20, 40),
            "is_married": bool(randrange(0, 1))
        }
        account.from_dict(additional_attribute)

        self.assertEqual(account.age, additional_attribute['age'])
        self.assertEqual(account.is_married,
                         additional_attribute['is_married'])

    def test_account_update(self):
        """ Test Account update """
        account = Account(**ACCOUNT_DATA[self.rand])
        account.create()
        self.assertEqual(len(account.all()), 1)
        account.name = "Qory"
        account.update()
        result = Account.find(account.id)
        self.assertEqual(result.name, account.name)

    def test_account_update_no_id(self):
        """ Test Account update without id (not created yet) """
        account = Account()
        account.id = None
        self.assertRaises(DataValidationError, account.update)

    def test_delete_an_account(self):
        """ Test Account deletion """
        account = Account(**ACCOUNT_DATA[self.rand])
        account.create()
        self.assertEqual(len(account.all()), 1)
        account.delete()
        self.assertEqual(len(account.all()), 0)
