from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from myapp.forms import RegistrationForm,LoginForm,TodoForm

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from myapp.models import Todo

from myapp.decorators import signin_required

from django.utils.decorators import method_decorator


class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=RegistrationForm()

        return render(request,'register.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=RegistrationForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"account created successfully")

            return redirect('signin')
            
        else:

            messages.error(request,'failed to create account')

            return render(request,'register.html',{"form":form_instance})
        

class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=LoginForm()

        return render(request,'login.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=LoginForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            user_obj=authenticate(request,**data)

            if user_obj:

                login(request,user_obj)

                messages.success(request,"login success")

                return redirect('todo-add')

        messages.error(request,"failed to login")
            
        return render(request,'login.html',{"form":form_instance}) 


@method_decorator(signin_required,name="dispatch")
class TodoCreateView(View):

    def get(self,request,*args,**kwargs):

        if not request.user.is_authenticated:

            messages.error(request,"invalid session")

            return redirect('signin')
        
        form_instance=TodoForm()

        return render(request,'todo_add.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        if not request.user.is_authenticated:

            messages.error(request,"invalid session")

            return redirect("signin")

        form_instance=TodoForm(request.POST)

        if form_instance.is_valid():

            form_instance.instance.owner=request.user
                
            form_instance.save()

                # data=form_instance.cleaned_data

                # Category.objects.create(**data)

            return redirect("todo-add")

        else:

            return render(request,"todo_add.html",{"form":form_instance})
        
        
@method_decorator(signin_required,name="dispatch")
class TodoDetailsView(View):

    def get(self,request,*args,**kwargs):

        if not request.user.is_authenticated:

            messages.error("invalid session")

            return redirect("signin")
        
        form_instance=TodoForm()

        qs=Todo.objects.filter(status=False,owner=request.user)

        return render(request,"todo_details.html",{"form":form_instance,"todolist":qs})
    

@method_decorator(signin_required,name="dispatch")
class TodoCompletedView(View):

    def get(aelf,request,*args,**kwargs):

        if not request.user.is_authenticated:

            messages.error("invalid session")

            return redirect("signin")
        
        form_instance=TodoForm()

        qs=Todo.objects.filter(status=True,owner=request.user)

        return render(request,"todo_status.html",{"completed":qs})
    

class TodoIndexView(View):

    def get(self,request,*args,**kwargs):

        form_instance=TodoForm()

        qs=Todo.objects.filter(owner=request.user)

        return render(request,"todo_index.html",{"todo":qs})

        
@method_decorator(signin_required,name="dispatch")
class TodoUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        todo_object=Todo.objects.get(id=id)

        form_instance=TodoForm(instance=todo_object)

        return render(request,"todo_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        todo_obj=Todo.objects.get(id=id)

        form_instance=TodoForm(request.POST,instance=todo_obj)

        if form_instance.is_valid():

            form_instance.save()

            return redirect('todo-list')
        
        else:

            return render(request,"todo_edit.html",{"form":form_instance})
        

@method_decorator(signin_required,name="dispatch")        
class TodoDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Todo.objects.get(id=id).delete()

        return redirect("todo-list")




@method_decorator(signin_required,name="dispatch")
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")


        


    









    


