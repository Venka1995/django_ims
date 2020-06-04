from django.shortcuts import render,redirect,get_object_or_404
from .models import Laptop,Mobile,Desktop
from .forms import LaptopForm,DesktopForm,MobileForm

# Create your views here.


# Index views here.......
def index(request):
    return render(request,'index.html')

def display(request,cls,header):
    items=cls.objects.all()
    context = {
    'items':items,
    'header':header,
    }
    return render(request,'index.html', context)

def display_Laptop(request):
    return display(request,Laptop,'Laptops')

def display_Desktop(request):
    return display(request,Desktop,'Desktops')

def display_Mobile(request):
    return display(request,Mobile,'Mobiles')


# adding new items to lists..........................
def add_device(request,cls,header):
    if request.method=='POST':
        form= cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=cls()
        return render(request, 'add_new.html', {'form':form,'header':header})


def add_laptop(request):
    return add_device(request,LaptopForm,'Laptop')

def add_desktop(request):
    return add_device(request,DesktopForm,'Desktop')

def add_mobile(request):
    return add_device(request,MobileForm,'Mobile')




# editing items inside lists..........................
def edit_device(request,pk,cls,model):
    item= get_object_or_404(model, pk=pk)
    if request.method=='POST':
        form = cls(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)
        return render(request,'edit.html',{'form':form})

def edit_laptop(request, pk):
    return edit_device(request,pk,LaptopForm, Laptop)

def edit_desktop(request, pk):
    return edit_device(request,pk,DesktopForm, Desktop)

def edit_mobile(request, pk):
    return edit_device(request,pk,MobileForm, Mobile)


# deleteing items from the lists..................
def delete(request, pk,cls,header):
    item=cls.objects.filter(id=pk).delete()
    context = {
    'item':cls.objects.all(),
    'header':header,
    }
    return render(request,'index.html',context)

def delete_laptop(request, pk):
    return delete(request, pk,Laptop,'Laptops')

def delete_desktop(request, pk):
    return delete(request, pk,Desktop,'Desktops')

def delete_mobile(request, pk):
    return delete(request, pk,Mobile,'Mobiles')
