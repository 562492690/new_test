from test_wechat.adressBook import AddressBook
from test_wechat.importContacts import ImportContacts
from test_wechat.index import Index


class TestAddMenber:
    def setup(self):
        self.index = Index()
        self.address = AddressBook()
        self.importContact = ImportContacts()

    def test_AddMember(self):
        self.index.goto_addMember().add_Member()

    def test_AddressAddMember(self):
        self.address.goto_addMember().add_Member()

    def test_ImportContacts(self):
        self.index.goto_importContacts().importContacts()

    def test_importContacts(self):
        self.address.goto_ImportContacts().importContacts()

