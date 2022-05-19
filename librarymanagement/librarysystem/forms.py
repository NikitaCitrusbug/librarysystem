from dataclasses import fields
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Author, Category, User , Book , IssuedBooks





class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_librarian = True
        if commit:
            user.save()
        return user


class CustomMemberCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_member = True
        if commit:
            user.save()
        return user



class LoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username' , 'password']



class AddForm(forms.ModelForm):
    authorname = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), required=False)
    
    widget=forms.CheckboxSelectMultiple()
    class Meta:
        model = Book
        fields = ['name' , 'discription' , 'quantity' , 'category' , 'authorname']
        
                
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'discription':forms.TextInput(attrs={'class':'form-control','placeholder':'Discription'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'quantity'}),
            'category':forms.Select(attrs={'class':'form-control form-select','placeholder':'select category'}),
            'authorname':forms.Select(attrs={'class':'form-control form-select','placeholder':'select author'}),
            
           
        }


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class IssuedBooksForm(forms.ModelForm):
    class Meta:
        model = IssuedBooks
        fields = '__all__'
        widgets = {
        'return_date' : DateInput(),
        'issued_date': DateInput(),
        'issued_date' : forms.HiddenInput()
        }
class UpdateIssueBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBooks
        fields = '__all__'
