from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import SuggestQuestionForm
from .models import Choice, Question, SuggestQuestion


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def home_view(request):
    if request.method == 'POST':
        val_form = SuggestQuestionForm(request.POST)
       
        if val_form.is_valid():
            val_form.save()
        else:
            print(val_form.errors)
            return HttpResponse(val_form.errors)

    val_form=SuggestQuestionForm()
    return render(request,'polls/home.html',{'forms': val_form})
  
    # context ={}
    # context['forms']= SuggestQuestionForm()
    # return render(request, "polls/home.html", context) 

