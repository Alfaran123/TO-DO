from django.core.checks import messages
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.shortcuts import redirect, render
from .models import Data

# Create your views here.
def index(request):
    
    todo=Data.objects.all()
    

    if request.method == 'POST':
        new_data=Data(
            work=request.POST['title']
        )
        new_data.save()
        return redirect('/')
        
        
            
    return render(request,'index.html',{'todos':todo})


def delete (request,pk):
    todo=Data.objects.get(id=pk)
    todo.delete()
    return redirect('/')



