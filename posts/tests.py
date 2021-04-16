from django.test import TestCase, RequestFactory
from .models import Post
from django.urls import reverse
from .views import posts_list
from django.contrib.auth.models import User


class PostTest(TestCase):
    def test_save_creates_slug(self):
        post = Post.objects.create(title="Hello World")
        self.assertEqual(post.slug, 'hello-world')


class PostsListClientTest(TestCase):
    def setUp(self):
        for i in range(5):
            Post.objects.create(title="Post - " + str(i))

    def test_list_view_works(self):
        response = self.client.get(reverse('posts-list'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_uses_correct_template(self):
        response = self.client.get(reverse('posts-list'))
        self.assertTemplateUsed(response, 'list.html')

    def test_list_view_lists_all_posts(self):
        response = self.client.get(reverse('posts-list'))
        self.assertTrue(len(response.context['posts']) == 5)
        self.assertContains( response, '<li class="text-gray-900"', count=5 )


class PostsListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='dummy', password='dummy')
        for i in range(5):
            Post.objects.create(title="Post - " + str(i))

    def test_list_view_works(self):
        request = self.factory.get(reverse('posts-list'))
        request.user = self.user

        response = posts_list(request)
        self.assertEqual(response.status_code, 200)
