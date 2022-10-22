#!Django Methods
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import TemplateView,ListView,CreateView,DetailView,FormView

#Django models and forms
from .models import *
from .forms import *

# Create your views here.
#!HomeView
class HomeView(TemplateView):
    template_name = 'books/home.html'

#!AuthorListView
class AuthorListView(ListView):#return= => object_list variable if not defined context_object_name in ListView
    model = Author
    context_object_name = 'authors'#if not define context_object_name in ListView,you define => modelname_list or object_list
    template_name = 'books/authors.html'

#!AuthorDetailView
class AuthorDetailView(DetailView):#return => object variable if not defined context_object_name in DetailView 
    model = Author
    context_object_name = 'author'
    template_name = 'books/author_detail.html'

#!AuthorCreateView
class AuthorCreateView(CreateView):
    model = Author
    fields = ['name','last_name']
    context_object_name = 'form'
    #success_url = reverse_lazy('books:authors')#when created Author,then redirect to this url vie reverse_lazy methods or used #! get_absolute_url
    template_name = 'books/author_create.html'
    
    def form_valid(self,form):
        messages.add_message(self.request,messages.SUCCESS,'The author has been added successfully')
        return super(AuthorCreateView,self).form_valid(form)#sending form overridinfv form_valid function

    def get_success_url(self):# or used success_url keyword and combile reverse_lazy keyword
        print('works get_success_url when created author')
        print('returned pk value for created author ', self.object.pk)
        return reverse('books:author',kwargs={'pk':self.object.pk})#if used function based view,adding redirect keyword before this code
    

#!AuthorBooksEditView
class AuthorBooksEditView(SingleObjectMixin,FormView):#Provide the ability to retrieve a single object for further manipulation.
    model = Author
    context_object_name = 'author'
    template_name = 'books/author_edit_book.html'
    
    def get(self,request,*args,**kwargs):
        print('Working get method at AuthorBooksEditView')
        self.object = self.get_object(queryset=Author.objects.all())#Return the object the view is displaying.
        print('self.object value at GET ', self.object.pk)#Find Author match to pk value automatically => For Example => Tolstoy
        print('------------------------------------------------')
        return super(AuthorBooksEditView,self).get(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        print('Working post method at AuthorBooksEditView')
        self.object = self.get_object(queryset=Author.objects.all())
        print('self.object value at POST ', self.object)
        print('------------------------------------------------')
        return super(AuthorBooksEditView,self).post(request,*args,**kwargs)

    def get_form(self,form_class=None):
        print('working get_form')
        print('**self.get_form_kwargs() ', self.get_form_kwargs())
        print('self.object value at POST', self.object)
        print('------------------------------------------------')
        return AuthorBooksFormset(**self.get_form_kwargs(),instance=self.object)

    def form_valid(self,form):
        print('Working form_valid function')
        print('self.object value at FORM', self.object)
        print('------------------------------------------------')
        form.save()
        messages.add_message(self.request,messages.SUCCESS,'Changes were saved')
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        print('self.object value at SUCCESS_URL ', self.object)
        return reverse('books:author',kwargs={'pk':self.object.pk})