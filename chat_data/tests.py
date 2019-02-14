from django.test import TestCase
from django.test import Client
from django.contrib import auth
from django.contrib.auth import get_user_model, authenticate

class Setup_Class(TestCase):

	def setUp(self):
		self.client = Client()
		self.User = get_user_model()
		
	def loginSuperUser(self):
		self.userInstance = self.User.objects.create(username ='superUser001', password = '12345PW', is_active = True, is_staff=True, is_superuser=True)
		self.userInstance.set_password('111Super$')
		self.userInstance.save()
		self.userInstance = authenticate(username='superUser001', password = '111Super$')
		login = self.client.login(username='superUser001', password = '111Super$')
		return self.userInstance
	

class TestViews(Setup_Class):
	"Testing views behave as expected."
	
	def test_redirect_to_index_for_anonymous_user_to_login(self):
		response = self.client.get("/")
		user = auth.get_user(self.client)
		
		if not user.is_authenticated :
			self.assertEqual(response.status_code, 302)
			self.assertEqual(response.url,"/account/login")
		else :
			self.assertFalse(True,"user is logged in so no redirect")
	
		
	def test_redirect_to_chat_index_when_user_authenticates(self):
		
		self.loggedInSuperUser = self.loginSuperUser()
		response = self.client.get("/")
		user = auth.get_user(self.client)
		
		if user.is_authenticated :
			self.assertEqual(response.status_code, 200)
		else :
			self.assertTrue(False,"Could not login user for test.")
		
		
	#def test_profile_and_chat_text_box_render(self):
	

# Create your tests here.


