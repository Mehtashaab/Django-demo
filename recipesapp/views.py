from django.shortcuts import render, redirect
from .models import recipe,User # Ensure you have imported the Recipe model
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/form/login")
def recipe(request):
    if request.method == 'POST':
        
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_price = request.POST.get('recipe_price')
        recipe_image = request.FILES.get('recipe_image')
       # print(recipe_name)
       # print(recipe_description)
       # print(recipe_price)
       # print(recipe_image)
    #     Recipe=recipe.objects.create(
    #        recipe_name=recipe_name,
    #        recipe_description=recipe_description,
    #        recipe_price=recipe_price,
    #        recipe_image=recipe_image

    #    )
    #     recipe.save()

       
    return render(request, 'recipe.html')
 

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.info(request, "Invalid UserName")
            return redirect('/form/register')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("form/login")
        else:
            login(request, user)
            return redirect("form/recipe")
    
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/form/login')



def register (request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # if User.objects.filter(username = username).first():
        #     messages.error(request, "This username is already taken")
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username is Already Taken")
            return redirect('/form/register')
            
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username =username,
            email =email,
            
)
        user.set_password=password # for encrypt the password use set_password method
        user.save()
        messages.info(request,"Account Created Successfully")

        return redirect("/form/login")

        
        
    return render(request,'register.html')