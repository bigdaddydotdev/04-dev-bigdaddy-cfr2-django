from django.shortcuts import get_object_or_404, render

from . import paginator
from .models import BlogPost
from django.conf import settings




# Create your views here.
def your_view(request):
  image_url = settings.CLOUDFLARE_R2_STATIC_URL + 'background.png'
  # ... other logic for your view
  return render(request, 'main.html', {'image_url': image_url})

def blog_post_detail_view(request, id=None):
    object = get_object_or_404(BlogPost, id=id)
    return render(request, "blog/detail.html", {"object": object, "instance": object})


def blog_post_list_view(request, *args, **kwargs):
    queryset = BlogPost.objects.all()
    pagination_data = paginator.paginate_queryset(request, queryset, per_page=5)
    object_list = pagination_data["object_list"]
    return render(
        request, "blog/list.html", {"object_list": object_list, **pagination_data}
    )
