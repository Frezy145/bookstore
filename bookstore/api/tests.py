from rest_framework.test import APITestCase
from django.urls import reverse_lazy, reverse
from api.models import Book, User

# global test
class BookStoreAPICase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            name = 'Things Fall Appart',
            autors = 'Chinua Achebe',
            number_of_pages = 100,
            summary = 'African social life during the colonisation',
            access = 'ALL',
            active = True
        )
        
        cls.book_2 = Book.objects.create(
            name = 'Fluent Python',
            autors = 'Luciano',
            number_of_pages = 768,
            summary = 'Dive in python programming',
            access = 'ADULTS',
            active = False
        )
        
        cls.user = User.objects.create(
            first_name ='Chinua',
            last_name = 'Achebe',
            username = 'Chin1',
            email = 'chinua127@gmail.com',
            password = 'ache1chin2',
            age = 70,
            gender = 'MALE',
        )
        
        cls.user = User.objects.create(
            first_name ='Yawa',
            last_name = 'Dow',
            username = 'Yadow',
            email = 'yawa127@gmail.com',
            password = 'waya1dow2',
            age = 16,
            gender = 'FEMALE',
        )
    
    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
class TestBook(BookStoreAPICase):

    url = reverse_lazy('books-list') # get book list url

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200) # assert we got in 
        
        # what we are expecting for
        expected = [
            {
                'id': book.id,
                'name' : book.name,
                'autors' : book.autors,
                'number_of_pages' : book.number_of_page,
                'summary' : book.summary,
                'access' : book.access,
                'active' : True,
                'created_at': self.format_datetime(book.created_at),
            } for book in [self.book, self.book_2]
        ]
        self.assertEqual(response.json(), expected) # assert we got the same 
        
    def test_create(self):  
        book_count = Book.objects.count() # let's count our books
        response = self.client.post(self.url, data={'name': 'Nouvelle catégorie'}) # add a new one 
        self.assertEqual(response.status_code, 405) # must return 405 status_code
        self.assertEqual(Book.objects.count(), book_count) # must False

class TestUser(BookStoreAPICase):

    url = reverse_lazy('users-list') # get book list url

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200) # assert we got in 
        
        # what we are expecting for
        expected = [
            {
                'id': user.id,
                'username' : user.username,
                'last_name' : user.last_name,
                'first_name' : user.first_name,
                'age' : user.age,
                'gender' : user.gender,
                'created_at': self.format_datetime(book.created_at),
            } for user in [self.user, self.user_2]
        ]
        self.assertEqual(response.json(), expected) # assert we got the same 
        
    def test_create(self):  
        user_count = User.objects.count() # let's count our users
        response = self.client.post(self.url, data={'name': 'New User'}) # add a new user
        self.assertEqual(response.status_code, 405) # must return 405 status_code
        self.assertEqual(Book.objects.count(), user_count) # must False
    
# In further releases, we'll add more test