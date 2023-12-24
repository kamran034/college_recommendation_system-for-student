from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from .models import *
# from blog.models import category
from degree.models import Postd
from django.contrib import messages
# Create your views here.
def college(request):
    all = Collegepost.objects.all()

    # cate = category.objects.all()
    
    context = {'cposts':all}
    

    return render(request,'college/college.html',context)



def single_colg(request, slug):
   
   post = Collegepost.objects.filter(slug=slug).first()
   all = Collegepost.objects.all()
   allPost = Postd.objects.all()

#    cate = category.objects.all()
#    cate = category.objects.all()
   comment = Comment.objects.filter(post=post)
	

   if request.method == "POST":
          name = request.POST['name']
          email = request.POST['email']
          postsno = request.POST.get('postsno')
          message = request.POST['message']
          
          post_data = Collegepost.objects.get(sno=postsno)

          comment = Comment(name=name,email=email,post=post_data,message=message)
          comment.save()
          messages.success(request,"Comment Successfully Submit")
          
          return redirect('/')
          
         
          



   context = {'post':post,'cposts':all,'posts':allPost ,'comment':comment}

   
   return render (request, 'college/single_colg.html',context)
