from django.http import HttpResponse
from debate.models import Statement, ArgumentFor, ArgumentAgainst, Argument
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

# Create your views here.

def index(request):
    return HttpResponse("You're looking at me punk...")

def statement(request, statement_id):
    this_statement = Statement.objects.get(pk=statement_id)
    #TODO: arguements for and against should really be sorted by most correct
    crap = ['f','u']
    context = {'this_statement': this_statement,
               'crap': crap}
    return render(request, 'debate/statement.html', context)
#     return HttpResponse(Statement.objects.get(pk=statement_id).text)

def submitfor(request, statement_id):
    s = get_object_or_404(Statement, pk=statement_id)
    ss = request.POST['argumentfor'].split(".") #TODO: rename varaibles for clarity and justice!
    creationTime =timezone.now()
    a = Argument(pub_date=creationTime)
    a.save()
    for idx, val in enumerate(ss):
        # TODO: normalize whitespace /n and such
        # TODO: deal with the "" case
        # TODO: trim string
        #print (idx, val)
        newS = Statement(text=val, pub_date=creationTime)
        newS.save()
        a.unsorted_parts.create(part=idx, content=newS)
    afor = ArgumentFor(statment=s, argument=a)
    afor.save()
    return HttpResponse(ss)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['argumentfor'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render(request, 'polls/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

# TODO: DRY this out
def submitagainst(request, statement_id):
    s = get_object_or_404(Statement, pk=statement_id)
    ss = request.POST['argumentagainst'].split(".") #TODO: rename varaibles for clarity and justice!
    creationTime =timezone.now()
    a = Argument(pub_date=creationTime)
    a.save()
    for idx, val in enumerate(ss):
        # TODO: deal with the "" case
        # TODO: trim string
        #print (idx, val)
        newS = Statement(text=val, pub_date=creationTime)
        newS.save()
        a.unsorted_parts.create(part=idx, content=newS)
    a_against = ArgumentAgainst(statment=s, argument=a)
    a_against.save()
    return HttpResponse(ss)