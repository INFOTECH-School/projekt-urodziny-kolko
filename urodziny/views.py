from django.shortcuts import render
from .models import Solenizant
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
# Create your views here.

class Czas(APIView):
    def get(self, request, strefa_czasowa):

        return Response({"data": datetime.now() + timedelta(hours=strefa_czasowa)}, status=200)

    #def post(self,request):
    #    pass
    #def put(self,request):
    #    pass
    #def delete(self,request):
    #    pass
















def niespodzianka(request,id):
    cword = Solenizant.objects.get(id=id)
    zdjecie = ""
    if cword.stan_upojenia == "1":
        zdjecie = cword.zdjecie1.image.url
    elif cword.stan_upojenia == "2":
        zdjecie = cword.zdjecie2.image.url
    elif cword.stan_upojenia == "3":
        zdjecie = cword.zdjecie3.image.url
    elif cword.stan_upojenia == "4":
        zdjecie = cword.zdjecie4.image.url

    return render(request,"cos.html",context={"cword": cword, "zdjecie": zdjecie})

