from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('add_post/',AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>',EditPostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete-post'),
    path('add_category',AddCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),

    # path('contact/',views.contact, name = 'contact'),
    # path('register/', views.register, name = 'register')
]
