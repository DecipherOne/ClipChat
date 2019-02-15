from django.test import TestCase , Client
from django.contrib import auth
from django.contrib.auth import get_user_model, authenticate
from chat_data import forms as chatForm
from django.utils import timezone


class Setup_Class(TestCase):

	def setUp(self):
		self.client = Client()
		self.User = get_user_model()
		
	def loginUser(self):
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
			self.assertEqual(response.url, "/account/login")
		else :
			self.assertFalse(True,"user is logged in so no redirect")
	
		
	def test_redirect_to_chat_index_when_user_authenticates(self):
		
		self.loggedInUser = self.loginUser()
		response = self.client.get("/")
		user = auth.get_user(self.client)
		
		if user.is_authenticated :
			self.assertEqual(response.status_code, 302)
			self.assertEqual(response.url, "messages/")
			
		else :
			self.assertTrue(False,"Could not login user for test.")
	
	def test_display_messages_renders(self):
		
		self.loggedInUser = self.loginUser()
		response = self.client.get("/messages/feed/")
		user = auth.get_user(self.client)
		
		if user.is_authenticated :
			self.assertEqual(response.status_code, 200)
			
		else :
			self.assertTrue(False,"Could not login user for test.")

class TestForms(Setup_Class):
	"Testing form submissions."
	
	def loginUserForTests(self):
		self.loggedInUser = self.loginUser()
		response = self.client.get("/")
		return auth.get_user(self.client)
		
		
	def test_post_message_successful_when_form_is_valid(self):
		
		user = self.loginUserForTests()
		
		if user.is_authenticated :
			form = chatForm.PostMessage(data={ 'message_body':"This is a message test."})
			self.assertTrue(form.is_valid())

		else :
			self.assertTrue(False,"Could not login user for test.")
	
	
	def test_invalid_form_data(self):
	
		user = self.loginUserForTests()
		
		if user.is_authenticated :
			form = chatForm.PostMessage(data={ 'message_body':""})
			self.assertFalse(form.is_valid())
			

		else :
			self.assertTrue(False,"Could not login user for test.")

# Create your tests here.


