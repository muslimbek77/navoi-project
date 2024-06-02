
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View,TemplateView
from .models import Contact,NewsArticle
from .bot import send_message


def home_view(request):
    return render(request, "index.html" )


# def blog_view(request):
#     return render(request, "blog.html")

class Blogview(TemplateView):
    template_name = "blog.html"
    model = NewsArticle
    

    def get_context_data(self,*args, **kwargs):
        context = super(Blogview, self).get_context_data(*args,**kwargs)
        context['NewsArticles'] = NewsArticle.objects.all()
        
        
      

        return context
    


# def blog_single_post_view(request,pk):
#     context={"news_article":NewsArticle.objects.filter(pk=pk)}
#     # print(context)
#     return render(request, template_name="blog-single-post.html",context=context)


class SinglePost(TemplateView):
    template_name = "blog-single-post.html"
    model = NewsArticle
    context_object_name = "NewsArticle"
    
   
    def get_context_data(self,*args,id, **kwargs):
        context = super(SinglePost, self).get_context_data(*args,**kwargs)
        # context['NewsArticles'] = NewsArticle.objects.filter(id=id)
        query = self.request.GET.get('q')
        if query:
            context['NewsArticles'] = NewsArticle.objects.filter(title__icontains=query)
        
        return context
    


def page_about_us_view(request):
    return render(request, "page-about-us.html")   


class ContactView(View):
    template_name = "page-contact.html"
    # form_class = ContactForm
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        subject = request.POST.get('subjact', '')
        contact = Contact(first_name=name,email=email,description=message,subjact=subject)
        # contact["form"] = self.form_class()
       
        contact.save()
        
        send_message(f"Foydalanuvchi ismi : {name}\nEmail: {email}\nyo'nalish {subject}\n Text:{message}")

        return HttpResponseRedirect(reverse('home-page'))


def page_faq_view(request):
    return render(request, "page-faq.html")


def page_agents_view(request):
    return render(request, "page-agents.html")

def page_testimonials_view(request):
    return render(request, "page-testimonials.html")


def page_service_box_view(request):
    return render(request, "page-service-box.html")

def page_partners_view(request):
    return render(request, "page-partners.html")


def page_services_view(request):
    return render(request, "page-services.html")

def page_single_service_view(request):
    return render(request, "page-single-service.html")


def page_turt_view(request):
    return render(request, "page-404.html")

def page_portfolio_list_view(request):
    return render(request, "page-portfolio-list.html")


def single_project_view(request):
    return render(request, "single-project.html")  


