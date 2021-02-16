from django.shortcuts import render

def homepageview(request):
    return render(request,'testapp/home.html')
def sportsinfo(request):
    msg_head="Sports Information"
    msg1="India won the T20 series on NewZealand tour"
    msg2="Kohli is the captain of India Team"
    msg3="Wait for update latest series"
    my_dict={'msg_head':msg_head,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/sports.html',context=my_dict)

def moviesinfo(request):
    msg_head="Movies Information"
    msg1="Gangotri is the first movie of ALLUARJUN"
    msg2="Chiranjeevi successfully completed his 150 movies"
    msg3="Wait for update latest movies"
    my_dict={'msg_head':msg_head,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/movies.html',context=my_dict)

def politicalinfo(request):
    msg_head="Politics Information"
    msg1="Anna Raambabu is the second majority person in MLA's."
    msg2="Jagan is the first majority person(CM)"
    msg3="Wait for update latest one"
    my_dict={'msg_head':msg_head,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/politics.html',context=my_dict)