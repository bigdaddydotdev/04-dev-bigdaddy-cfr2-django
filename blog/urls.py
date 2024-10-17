#blog/urls.py

from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    #path('', views.landing_page_view, name='home'),  # Landing page view
    #path('blog/', include('blog.urls')),  # Include sub-urls for blog
    path("", views.blog_post_list_view, name="post-list"),
    path("<int:id>/", views.blog_post_detail_view, name="post-detail"),
]


