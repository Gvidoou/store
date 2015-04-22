from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from Products.forms import CommentsForm

from Products.models import Product, Comments


class ProductList(ListView):
    """
    View for list of products
    """
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['title'] = 'List of products'
        return context


class ProductDetailView(FormMixin, DetailView):
    """
    View for product page and form for posting comments
    """
    model = Product
    template_name = 'product_detail.html'
    form_class = CommentsForm

    def get_success_url(self):
        return reverse('products_list')

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Product details'
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        try:
            context['comments'] = Comments.objects.filter(product=self.object)
        except:
            pass
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print self.object
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            data = form.cleaned_data
            Comments.objects.create(title=data['title'],
                                    comment=data['comment'],
                                    product=self.object)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super(ProductDetailView, self).form_valid(form)
