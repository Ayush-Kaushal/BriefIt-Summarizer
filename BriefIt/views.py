from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from .Summarizer import GenerateSummary

def home(request):
    return render(request, 'BriefIt/home.html')


def about(request):
    return render(request, 'BriefIt/about.html')


def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer


def summary(request):
    if not get_referer(request):
        raise Http404('Nice try!!!')

    if request.method == 'GET':
        # Get User Input
        article = request.GET.get('input_text')
        article = str(article)
        summary = GenerateSummary(article)

        if summary == 'No input':
            messages.error(request, 'Not enough input or Invalid URL')
            return redirect('home')

        context = {
            'article' : article,
            'summary' : summary
        }

        return render(request, 'BriefIt/summary.html', context)
        

    return render(request, 'BriefIt/home.html')


# def abstract_summary(request):
#     if not get_referer(request):
#         raise Http404('Nice try!!!')

#     if request.method == 'GET':
#         # Get User Input
#         article = request.GET.get('input_text')
#         article = str(article)
#         summary = AbstractSummary(article)

#         context = {
#             'article' : article,
#             'summary' : summary
#         }

#         return render(request, 'BriefIt/abstract_summary.html', context)
    
#     return render(request, 'BriefIt/home.html')

