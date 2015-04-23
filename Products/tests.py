import decimal
import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from Products.models import Product, Comments


class ProductTest(TestCase):
    def setUp(self):
        self.octopus = Product.objects.create(
            name='octopus',
            slug='prod',
            description='some text',
            price=2.30,
        )

    def test_product_page(self):
        """
        test product page info
        """
        response = self.client.get(reverse('product', args=['prod']))
        self.assertEqual(response.status_code, 200)
        self.assertIn('octopus', response.content)
        self.assertIn('some text', response.content)

    def test_like(self):
        """
        test like button
        and success message
        """
        likes = self.octopus.like_counter
        response = self.client.get(reverse('like',
                                           args=[self.octopus.pk]), follow=True)
        product_counter = Product.objects.get(pk=self.octopus.pk).like_counter
        likes += 1
        self.assertEqual(likes, product_counter)
        self.assertIn('Your like  successfully added!', response.content)

    def test_add_comments(self):
        """
        test comments form and success message
        """
        response = self.client.post(reverse('product', args=['prod']), {
            'title': 'Nice one!',
            'comment': 'I  like that',

        }, follow=True)
        self.assertIn('Your comment successfully added!', response.content)
        response_two = self.client.get(reverse('product', args=['prod']))
        self.assertIn('Nice one!', response_two.content)
        self.assertIn('I  like that', response_two.content)

    def test_comments_list(self):
        """
        test list of comments on page
        it should shows only last comments for 24 hours
        """
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1,
                                                                 hours=1)
        comment = Comments.objects.create(title='one more',
                                          comment='Some comment',
                                          product=self.octopus)

        comment.created_at = yesterday
        comment.save()
        response = self.client.get(reverse('product', args=['prod']))
        self.assertNotIn('one more', response.content)
        self.assertNotIn('Some comment', response.content)