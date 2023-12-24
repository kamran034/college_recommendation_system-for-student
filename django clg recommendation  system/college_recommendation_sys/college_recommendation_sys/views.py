from django.http import  HttpResponse
from django.shortcuts import render

from  store.models import ReviewRating
from .forms import ReviewForm

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from degree.models import Postd
from degree.models import College

# def home(request):
#    return HttpResponse("helllo")


@login_required(login_url='login')
def Home1(request):
    return render (request,'home.html')


def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('/home')

    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        my_user = User.objects.filter(username = uname)
        if my_user.exists():
            messages.warning(request, 'Username is already taken.')
            return HttpResponseRedirect(request.path_info)
        

        my_user = User.objects.filter(email = email)
        if my_user.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        
        if pass1!=pass2:
             messages.warning(request, 'Your password and confrom password are not Same!!')
             return HttpResponseRedirect(request.path_info)
            # return HttpResponse("Your password and confrom password are not Same!!")
        

        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        



    return render (request,'signup.html')




def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('/home')


    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            # return HttpResponse ("Username or Password is incorrect!!!")
            messages.warning(request, 'Username or Password is incorrect!!!')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('login')



def home1(request):

    allPost = Postd.objects.all()
   
    context = {'posts':allPost}


    return render (request, 'index.html',context)


def aboutus(request):
   
    return render (request, 'about.html')





def degree(request):
    allPost = Postd.objects.all()
   
    context = {'posts':allPost}

    return render(request, 'degree.html',context)


def single_degree(request,slug):
   post = Postd.objects.filter(slug=slug).first()

   allPost = Postd.objects.all()
    
   context = {'post':post,'posts':allPost}

   return render(request, 'single_deg.html',context)





def feedback(request):
    # allPost = Postd.objects.all()
   
    # context = {'posts':allPost}
    return render(request, 'feedback.html')



def submit_review(request):
   
   url = request.META.get('HTTP_REFERER')
   if request.method == 'POST':

        try:
            
            form = ReviewForm(request.POST)
            form.save()
            messages.success(request, 'Thank you! Your review has been submitted.')
            
            # return HttpResponseRedirect("/rating/")
            # return redirect("rating.html")
            return redirect(url)

        except :
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                # data.usermail=form.cleaned_data['usermail']
                # postsno = request.POST.get('validuser')
                # post_data = User.objects.get(User=postsno)
                # maildata = User.objects.filter(usermial = data.usermail )
                # if maildata.exists():
                #  messages.warning(request, 'please write valid mail')
                #  return HttpResponseRedirect(request.path_info)
                data.ip = request.META.get('REMOTE_ADDR')
                
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                # return redirect("rating.html")
                return redirect(url)






def recommendation(request):

    return render(request ,'recommendation.html')







# def college(request):
    
#     clg = College.objects.all()

#     context = {'clg': clg}


#     return render(request, 'college.html',context)



# def single_colg(request,slug):
   
#    post = College.objects.filter(slug=slug).first()

#    clg = College.objects.all()

    
#    context = {'clg': clg ,'post': post}
   

#    return render(request, 'single_colg.html',context)

    