from django.db.models import F
from django.shortcuts import get_object_or_404, render
from polls.models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#These views represent a common case of basic web development: getting data from the database according to a parameter passed in the URL,
#  loading a template and returning the rendered template. 
# Because this is so common, Django provides a shortcut, called the “generic views” system.

# Create your views here.
class IndexView(generic.ListView): 
    #This view is designed to return a list of objects.
    # By default, the list of objects it retrieves is passed to the template using the context variable object_list
    #If you want to use a different context name in your template (e.g., latest_questions instead of object_list), you need to define context_object_name.
    queryset=Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    template_name="polls/index.html"

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={"latest_questions":latest_question_list}
    return render(request,"polls/index.html",context)
#The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument.
#It returns an HttpResponse object of the given template rendered with the given context.

class DetailView(generic.DetailView):
    #This view is designed to return a single object, typically the one specified by the pk or slug in the URL
    #By default, the object is passed to the template using the context variable object, but it also automatically creates a context variable named after the model (in lowercase).
    # In your case, this would be question, so you don't need to specify context_object_name manually.

    queryset=Question.objects.filter(pub_date__lte=timezone.now()) #Excludes any questions that aren't published yet.
    template_name="polls/detail.html"

#def detail(request,question_id):
#    question=get_object_or_404(Question,pk=question_id)
#    return render(request, "polls/detail.html",{'question':question})
#The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager.
#It raises Http404 if the object doesn’t exist

def vote (request,question_id):
    question= get_object_or_404(Question,pk= question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form.
        return render(request,"polls/detail.html",{'question':question, "error_message": 'you did not vote.'},)
    else:
        selected_choice.votes=F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))

class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"

#def results(request, question_id):
#    question=get_object_or_404(Question,pk=question_id)
#    return render(request,'polls/results.html',{'question':question})