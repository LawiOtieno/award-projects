from django.test import TestCase
from .models import Awwards, Profile,Image,Comments
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTEst(TestCase):
    def setUp(Self):
        '''
        Set up class to create a new profile
        '''
        bernard = User(username = 'bernard',email = 'brobernard.254@gmail.com')
        bernard = Profile(user = Self.bernard,user_id = 1,bio = 'Web design',dpic = 'pic.jpg',info = 'Contact me')

    def test_instance(self):
        '''
        Test class to test instantiation
        '''
        self.assertTrue(isinstance(self.joker,Profile))

    def test_save_profile(self):
        '''
        Test to test if a profile is saved
        '''
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        '''
        Test to see if a profile can be deleted 
        '''
        self.joker.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)

class AwwardsTestCase(TestCase):
    def setUp(self):
     
        self.new_post = Awwards(image = '',title = 'picture',description = 'Good one',link = '')


    def test_save_image(self):
        self.picture.save_image()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        '''
        Test case to test the deletion of an image
        '''
        self.picture.save_image()
        self.picture.delete_image()
        picture_list = Image.objects.all()
        self.assertTrue(len()==0)

    def test_get_all_images(self):
        '''
        Test case to get all images posted
        '''
        self.picture.save_image()
        all_pictures = Image.get_all_images()
        self.assertTrue(len(all_pictures) < 1)

    def test_get_one_image(self):
        '''
        Test to get one image post
        '''
        self.food.save_image()
        one_pic = Image.get_one_image(self.food.id)
        self.assertTrue(one_pic.name == self.picture.name)
