from django.shortcuts import render, get_object_or_404
from .forms import PostForm, EditForm, AddCommentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from django.urls import reverse_lazy, reverse


# Create your views here.

# def index(request):
#     return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error(request, *args, **kwargs):
    return render(request,'pages/error.html')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked= False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context    

# ---------------Post-----------------------
class AddPostView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'add_post.html'

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm 
    template_name = 'update_post.html'
    # fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
# ---------------Category-----------------------
class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm 
    template_name = 'add_category.html'
    fields ='__all__'

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',{'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html',{'cats':cats.title(),'category_posts':category_posts})

#  --------comment--------
class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    # fields ='__all__'
    
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')

    