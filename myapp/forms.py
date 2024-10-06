from django import forms

from myapp.models import Task

from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):     
    
    class Meta:

        model=Task

        # fields="__all__"
        exclude=("created_date","status")

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),

            "description":forms.Textarea(attrs={"class":"form-control"}),

            "due_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),

            "category":forms.Select(attrs={"class":"form-control form-select"}),

            "user":forms.TextInput(attrs={"class":"form-control"}),
            
               }





# authentication 

class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","password"]

        widgets={
            

            "username":forms.TextInput(attrs={"class":"form-control","style":"width:350px;height:40px;margin-bottom:40px;"}),

            "email":forms.TextInput(attrs={"class":"form-control","style":"width:350px;height:40px;margin-bottom:40px;"}),

            "password":forms.TextInput(attrs={"class":"form-control","style":"width:350px;height:40px;margin-bottom:40px;"})


        }



class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","style":"width:350px;height:40px;margin-bottom:40px;"})
)

    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","style":"width:350px;height:40px;"}))








# #  class TaskForm(forms.ModelForm):     #modelform use cheythal fields automatically populate aakum modelsilum formilum seperate kodukanda

# # from myapp.models import Task      model ivde import cheyyanam

# # class Meta: modelform use cheyyumbol meta class venam

# #  fields="__all__" task modelile ella fieldsum venam so all koduthu illel vendath list aku ko/duthathi

# # created_date auto now koduthitullathukond ath fieldsil venda so orennam mathram vendathond exclude koduthu

# # modelform style cheyyan widgets enna oru dictionary create cheyth key aayi column name koduth values kodukanam 
