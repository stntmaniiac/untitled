from django.shortcuts import render_to_response

def home(request):
   context ={
       'request':request,
       'user': request.user
   }
   return render_to_response('petition/homepage.html', context)

def index(request):

    context={
        'request':request,
        'user':request.user
    }
    return render_to_response('petition/success.html', context)
    #return render_to_response('petition/index.html', context)
    #return HttpResponse(total)

def done(request):

    return render_to_response('petition/done.html', context={})




