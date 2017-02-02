__author__ = 'RAJ'
from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
class SimpleTest(TestCase):
    fixtures = ['test_data.json','user.json']

    def test_create_auction(self):
        response = self.client.post('/auction/create/', {'title': 'title','category': 'cate','description': 'desc', 'price': 'price', 'startdate':'sdate', 'enddate':'edate', 'status':'status', 'seller':'seller'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"Login to your YAAS account")

        response = self.client.post('/register/',{'username':'raj','password1':'raj','password2':'raj','email':'raj@raj.fi'})
        loggedin = self.client.login(username='raj', password='raj')
        self.assertTrue(loggedin)

        response = self.client.post('/auction/create/', {'title': '','category': 'cate','description': 'desc', 'price': '12', 'enddate':'2014-12-12', 'status':'active', 'seller':'raj'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"This field is required.")

        response = self.client.post('/auction/create/', {'title': 'tits','category': 'cate','description': 'desc', 'price': '0', 'enddate':'2014-12-12', 'status':'active', 'seller':'raj'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"Price should not be less than 0.")

        response = self.client.post('/auction/create/', {'title': 'tits','category': 'cate','description': 'desc', 'price': '12', 'enddate':'20141212', 'status':'active', 'seller':'raj'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"This field is required. And should be in 'YYYY-MM-DD HH:MM' format.")

        response = self.client.post('/auction/create/', {'title': 'tits','category': 'cate','description': 'desc', 'price': '12', 'enddate':'2014-11-02 11:11', 'status':'active', 'seller':'raj'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"End Date should not be less the 72 hours from now.")

        response = self.client.post('/auction/create/', {'title': 'tits','category': 'cate','description': 'desc', 'price': '12', 'enddate':'2014-11-20 11:11', 'status':'active', 'seller':'raj'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"Option:")

        response = self.client.post('/auction/saveauction/', {'title': 'tits','category': 'cate','description': 'desc', 'price': '12', 'enddate':'2014-11-20 11:11', 'status':'active', 'seller':'raj','option':'no'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"Auction was discarded")

        response = self.client.post('/auction/saveauction/', {'title': 'tits','category': 'cate','desc': 'desc', 'price': '12','edate':'2014-11-20 11:11','option':'yes'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"Auction was saved")
