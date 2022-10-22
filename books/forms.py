from django.forms.models import inlineformset_factory
from .models import *

#!AuthorBooksFormset
AuthorBooksFormset = inlineformset_factory(Author,Book,fields=('title',),extra=1)