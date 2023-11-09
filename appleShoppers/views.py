from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog_list(request):
    return render(request,'blog_list.html')

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request, 'products/product.html')
def testimonial(request):
    return render(request,'testimonial.html')