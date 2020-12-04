from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'
#     paginate_by = 3

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'

def HomePage(request):
    return render(request, 'index.html')

def PostList(request):
    title = 'Blog'
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # Jika variabel page bukan Integer, tampilkan halaman pertama
        post_list = paginator.page(1)
    except EmptyPage:
        # Jika variabel page melebihi, tampilkan halaman terakhir
        post_list = paginator.page(paginator.num_pages)
    finally:
        return render(request,
                    'blog/index.html',
                    {'page': page,
                    'title': title,
                    'post_list': post_list})

def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Buat objeck Comment tanpa disimpan di database
            new_comment = comment_form.save(commit=False)
            # Menghubungkan post yang sekarang ke komentar
            new_comment.post = post
            # Simpan komentar ke database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'title': post.title,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, template_name, context)