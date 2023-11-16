from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import JsonResponse
from .models import Keyword


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#前端向后端传参

def get_keywords(request):
    term = request.GET.get('term')  # jQuery UI Autocomplete会发送名为'term'的GET参数
    if ',' in term:
        term = term.split(',')[-1].strip()  # 如果输入包含逗号，取最后一个逗号后的字符串作为搜索关键词
    keywords = Keyword.objects.filter(name__icontains=term)  # 假设你的关键词存储在Keyword模型的name字段
    results = []
    for keyword in keywords:
        keyword_dict = {
            'id': keyword.id,
            'label': keyword.name,
            'value': keyword.name
        }
        results.append(keyword_dict)
    return JsonResponse(results, safe=False)

def g(request):
    g = 'a'
    if request.method == 'POST':
        g = request.POST.get('g')
        keywords = g.split(',')  # 分割关键词
        # 在这里你可以对关键词进行进一步的处理
        return render(request, 'blog/g.html', {'keywords': keywords})
    return render(request, 'blog/g.html', locals())

from .forms import AccountIDForm

def upload_account_ids(request):
    if request.method == 'POST':
        form = AccountIDForm(request.POST, request.FILES)
        if form.is_valid():
            account_ids = form.cleaned_data['account_ids']
            file = form.cleaned_data['file']
            if file:
                account_ids = file.read().decode().split('\n')
            return render(request, 'upload.html', {'account_ids': account_ids})
    else:
        form = AccountIDForm()
    return render(request, 'blog/upload.html', {'form': form})

from django.shortcuts import render
from django.http import HttpResponseBadRequest

def index1(request):
    if request.method == 'POST':
        account_ids = request.POST.get('account_ids')
        file = request.FILES.get('file')

        if account_ids and file:
            return HttpResponseBadRequest("不能同时输入账户ID和上传文件")

        if account_ids:
            account_ids = account_ids.split(';')
            if len(account_ids) > 5:
                return HttpResponseBadRequest("最多只能输入5个账户ID")
        elif file:
            account_ids = file.read().decode().split('\n')
        else:
            return HttpResponseBadRequest("请至少输入一个账户ID或上传一个文件")

        return render(request, 'blog/index1.html', {'account_ids': account_ids})

    return render(request, 'blog/index1.html')

from .forms import ProductForm,KeywordForm,AccountForm
def index(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        keyword_form = KeywordForm(request.POST)
        account_form = AccountForm(request.POST)

        if product_form.is_valid() and keyword_form.is_valid() and account_form.is_valid():
            product_name = product_form.cleaned_data['product_name']
            keyword = keyword_form.cleaned_data['keyword']
            account_ids = account_form.cleaned_data['account_ids']

            # 在这里处理提交的数据，可以将数据保存到数据库或进行其他操作

            return render(request, 'blog/result.html', {
                'product_name': product_name,
                'keyword': keyword,
                'account_ids': account_ids.split(';'),
            })
    else:
        product_form = ProductForm()
        keyword_form = KeywordForm()
        account_form = AccountForm()

    return render(request, 'blog/index.html', {
        'product_form': product_form,
        'keyword_form': keyword_form,
        'account_form': account_form,
    })

from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse

def index2(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name', '')
        selected_keywords = request.POST.getlist('selected_keywords')
        account_ids = request.POST.get('account_ids', '')

        return render(request, 'blog/index2.html', {
            'product_name': product_name,
            'selected_keywords': selected_keywords,
            'account_ids': account_ids
        })

    return render(request, 'blog/index2.html')

def get_suggestions(request):
    # 从数据库获取关键词数据并返回
    suggestions = ['keyword1', 'keyword2', 'keyword3']  # 这里仅作示例
    return JsonResponse(suggestions, safe=False)

def get_recommendations(request):
    if request.method == 'POST':
        keywords = request.POST.getlist('keywords[]')
        # 根据输入的关键词从数据库获取推荐关键词数据并返回
        recommendations = ['recommendation1', 'recommendation2', 'recommendation3']  # 这里仅作示例
        return JsonResponse(recommendations, safe=False)
    
from django.shortcuts import render
from .forms import KeywordForm

def fn2_view(request):
    form = KeywordForm()
    return render(request, 'blog/fn2.html', {'form': form})

def index3(request):
    if request.method == 'POST':
        if '联想' in request.POST:
            # 处理联想按钮点击事件
            keyword = request.POST.get('input1', '')
            suggestions = generate_suggestions(keyword)
            return JsonResponse({'suggestions': suggestions})
        elif '确定' in request.POST:
            # 处理确定按钮点击事件
            keywords = request.POST.get('input2', '').split(',')
            add_keywords(keywords)
            return JsonResponse({'success': True})
    return render(request, 'blog/index3.html')

def generate_suggestions(keyword):
    suggestions = []
    for i in range(len(keyword)):
        suggestion = keyword[:i] + keyword[i+1:]
        suggestions.append(suggestion)
    return suggestions

def add_keywords(keywords, new_keywords):
    for keyword in new_keywords:
        if keyword not in keywords:
            keywords.append(keyword)
    return keywords

# def indextest(request):
#     return render(request, 'blog/indextest.html')

# from .forms import MyForm

# def indextest(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST, request.FILES)
#         if form.is_valid():
#             product_id = form.cleaned_data['product_id']
#             keywords = form.cleaned_data['keywords']
#             account_ids = form.cleaned_data['account_ids']
#             file = form.cleaned_data['file']

#             # 在这里处理表单数据，可以将其保存到数据库或执行其他操作

#             return render(request, 'blog/success.html')  # 显示成功页面
#     else:
#         form = MyForm()

#     return render(request, 'blog/indextest.html', {'form': form})

from django.shortcuts import render
from django.http import JsonResponse

# def indextest(request):
#     return render(request, 'blog/indextest.html')

# def submit_form(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST, request.FILES)
#         if form.is_valid():
#             productid = form.cleaned_data['productid']
#             selected_keywords = form.cleaned_data['selected_keywords']
#             account_ids = form.cleaned_data['account_ids']
#             file = form.cleaned_data['file']

#             # 处理你想要的提交内容
#             # ...

#             # 返回JSON响应，可以根据需要进行修改
#             # return render(request,'blog/.html',{
#             #     'productid':productid,
#             #     'selected_keywords':selected_keywords,
#             #     'account_ids':account_ids,
#             #     'file':file})
#             return JsonResponse({'success': True})
#     else:
#         form = MyForm()
    
#     return render(request, 'blog/indextest.html', {'form':form})

from django.http import HttpResponse
from .forms import SubmitForm

def submit_form(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            product_id = form.cleaned_data['productid']
            selected_keywords = form.cleaned_data['selected_keywords']
            account_ids = form.cleaned_data['account_ids']
            file = form.cleaned_data['file']
            
            # 在这里处理表单提交的数据
            
            return HttpResponse('提交成功')
    else:
        form = SubmitForm()
    
    return render(request, 'blog/indextest.html', {'form': form})
