from django.http import HttpResponse
from debate.models import Statement, ArgumentFor, ArgumentAgainst, Argument
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
#from django.contrib.auth.decorators import login_required

#@login_required
def index(request):
    return HttpResponse("You're looking at me punk...") #TODO: list top level arguments

def statement(request, statement_id):
    this_statement = Statement.objects.get(pk=statement_id)
    #TODO: arguements for and against should really be sorted by most correct
    context = {'this_statement': this_statement}
    return render(request, 'debate/statement.html', context)
#     return HttpResponse(Statement.objects.get(pk=statement_id).text)

# TODO: the ballot stuff might be suficiently different enough, that it  should be in it's own django app
def ballot(request):
    return render(request, 'debate/ballot_prototype.html')

def submitfor(request, statement_id):
    s = get_object_or_404(Statement, pk=statement_id)
    ss = request.POST['argumentfor'].split(".") #TODO: rename varaibles for clarity and justice!
    creationTime =timezone.now()
    a = Argument(pub_date=creationTime)
    a.save() # TODO: this is a very slight bug with "" input
    
    idx = 0 # TODO: this feels bad, I would rather filter with lambdas
    for val in ss:
        # TODO: normalize whitespace /n and such within string
        #print (idx, val)
        # deal with the "" case
        t=val.strip()
        if t:
            newS = Statement(text=t, pub_date=creationTime)
            newS.save()
            a.unsorted_parts.create(part=idx, content=newS)
            idx = idx +1
    if a.unsorted_parts.all():
        afor = ArgumentFor(statment=s, argument=a)
        afor.save()
        return statement(request, statement_id)
    else:
        return HttpResponse("cannot add an empty argumnet")
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
    
    idx = 0 # TODO: this feels bad, I would rather filter with lambdas
    for val in ss:
        # TODO: normalize whitespace /n and such within string
        #print (idx, val)
        # deal with the "" case
        t=val.strip()
        if t:
            newS = Statement(text=t, pub_date=creationTime)
            newS.save()
            a.unsorted_parts.create(part=idx, content=newS)
            idx = idx +1
    if a.unsorted_parts.all():
        a_against = ArgumentAgainst(statment=s, argument=a)
        a_against.save()
        return statement(request, statement_id)
    else:
        return HttpResponse("cannot add an empty argumnet")