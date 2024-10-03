
from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import TaskForm

from django.contrib import messages

from myapp.models import Task

from django import forms

from django.db.models import Q



class TaskCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=TaskForm()

        return render(request,"task_create.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=TaskForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()    #model form anu use cheythekunnath

            messages.success(request,"task created successfully")

            return redirect("task_list")
        else:

            messages.error(request,"error in creation")

            return render(request,'task_create.html',{"form":form_instance})





class TaskListView(View):
    def get(self,request,*args,**kwargs):

        

        selected_category=request.GET.get("category","all")


        search_text=request.GET.get("search_text")

       
           
        if selected_category=="all":

             qs=Task.objects.all()
            
        else:

            qs=Task.objects.filter(category=selected_category)

        

        if search_text!=None:

            qs=Task.objects.filter(Q(title__icontains=search_text)|Q(description__icontains=search_text))



        return render(request,"task_list.html",{"tasks":qs,
                                             "selected":selected_category })




class TaskDetailView(View):

    def get(self,request,*args,**kwargs):

        # extract id from url

        id=kwargs.get("pk")

        # fetching task with id

        qs=Task.objects.get(id=id)

        return render(request,"task_detail.html",{"task":qs})



class TaskUpdateView(View):

    def get(self,request,*args,**kwargs):

    # extract id from kwargs

        id=kwargs.get("pk")

    # fetch data with id

        task_obj=Task.objects.get(id=id)

    # modelform use cheythathukond instance use cheyth kodukam illel dictionary cretae vheyyanam

        form_instance=TaskForm(instance=task_obj)


        # add status field in form_instance

        form_instance.fields["status"]=forms.ChoiceField(choices=Task.status_choices,widget=forms.Select(attrs={"class":"form-control form-select"}),initial=task_obj.status)

        return render(request,'task_update.html',{"form":form_instance})

    # def post(self,request,*args,**kwargs):

    #     # extract id from kwargs

    #     id=kwargs.get("pk")

    #     #initialize form with request.post

    #     form_instance=TaskForm(request.POST)

    #     # check form is valid

    #     if form_instance.is_valid():

    #     # fetch valid data

    #         data=form_instance.cleaned_data

    #     # extract status from request.post(karanam taskformil nammal status koduthitilla athkond ivde seperate fetch cheyth edukanam)

    #         status=request.POST.get("status")

    #         # task update

    #         Task.objects.filter(id=id).update(**data,status=status)

    #         # redirect to task_list

    #         return redirect("task_list")

    #     else:

    #         return render(request,"task_update.html",{"form":form_instance})






# better form


    def post(self,request,*args,**kwargs):

        # extract id from kwargs

        id=kwargs.get("pk")


        task_obj=Task.objects.get(id=id)

        #initialize form with request.post

        form_instance=TaskForm(request.POST,instance=task_obj)

        # check form is valid

        if form_instance.is_valid():

     
            form_instance.instance.status=request.POST.get("status")


            form_instance.save()

       

            # redirect to task_list

            return redirect("task_list")

        else:

            return render(request,"task_update.html",{"form":form_instance})





class TaskDeleteView(View):

    def get(self,request,*args,**kwargs):

        # extract id and delete task object with this id

        Task.objects.get(id=kwargs.get("pk")).delete()

        return redirect("task_list")

from django.db.models import Count

class TaskSummaryView(View):

    def get(self,request,*args,**kwargs):

        qs=Task.objects.all()

        total_task_count=qs.count()

        category_count=Task.objects.all().values("category").annotate(cat_count=Count("category"))
        print(category_count)


        status_summary=Task.objects.all().values("status").annotate(stat_count=Count("status"))
        print(status_summary)

        context={
            "total_task_count":total_task_count,
            "category_summary":category_count,
            "status_summary":status_summary


        }

        return render(request,"task_summary.html",context)











