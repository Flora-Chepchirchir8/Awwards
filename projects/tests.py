from django.test import TestCase
from .models import Rating,Projects,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Sareto')
        self.project = Project.objects.create(id=1, title='Awwards', description='A web application where users can view the latest news from different sources. It uses the News API to fetch the news and display it on the web page ',technologies_used='Python',post_date='2021,12,12',project_image='https://cloudinary url', repo_link='http://github.com',live_link='http://heroku.com',user=self.user)



    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_post(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_display_projects(self):
        self.project.save()
        projects = Project.get_projects()
        self.assertTrue(len(projects) > 0)

    def test_search_projects(self):
        self.project.save()
        project = Project.search_projects('random_project')
        self.assertTrue(len(project) >= 0)

   

    def test_delete_post(self):
        self.project.delete_project()
        project = Project.search_projects('random_project')
        self.assertTrue(len(project) < 1)


class RatingTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Sareto')
        self.project = Project.objects.create(id=1, title='Pitch Perfect', description='Its a Python-based web application that allows a user to post and interact with other pitches submitted by other users. A user must first signup and then login to the application for use',technologies_used='HTML',post_date='2021,6,19',project_image='https://cloudinary url', repo_link='http://github.com',live_link='http://heroku.com',user=self.user)
        self.rating = Rating.objects.create(id=1, design_wise=8, usability_wise=8, content_wise=7, user=self.user, project=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)


class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Sareto', password='1234')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
        

