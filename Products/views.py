import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
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

    def get_queryset(self):
        queryset = super(ProductList, self).get_queryset()
        if 'order_by' in self.request.GET:
            if self.request.GET['order_by'] == 'asc':
                messages.success(self.request, 'Products ordered by most rated')
                return queryset.order_by('-like_counter')
            elif self.request.GET['order_by'] == 'desc':
                messages.success(self.request,
                                 'Products ordered by least rated')
                return queryset.order_by('like_counter')
        return queryset


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
        time = datetime.datetime.now() - datetime.timedelta(days=1)
        try:
            context['comments'] = Comments.objects.filter(
                product=self.object,
                created_at__gte=time).order_by('-created_at')
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
            messages.success(request, 'Your comment successfully added!')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super(ProductDetailView, self).form_valid(form)


def like(request, pk):
    """
    simple view to save like requests
    """
    product = Product.objects.get(pk=pk)
    product.like_counter += 1
    product.save()
    messages.success(request, 'Your like  successfully added!')
    return redirect(reverse('product', args=[product.slug]))