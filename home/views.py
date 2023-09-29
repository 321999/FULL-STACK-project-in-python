from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helo(request):
    return HttpResponse("welcome <em>to ur</em> home <e>page</e>")

def sucess(request):
    print("sucess route running"+"*"*10)
    return HttpResponse("<h1>perseverence and being with the technology is the key to success</h1>")
def blog(request):
    print("blog page is creating")
    # similarly like homewe can have  product  ka page,user ka page and  aa sakta hi 
    return render(request,"home/index.html")

def samaan(request):
    loyal=[
        {"NAME":"KISHRE","AGE":23},
        {"NAME":"KIE","AGE":23},
        {"NAME":"ISHRE","AGE":23},
        {"NAME":"KIS","AGE":23},
        {"NAME":"KISH","AGE":23},
        {"NAME":"KI","AGE":23},

    ]
    return render(request,"product/index.html",context={"loyal":loyal})



#     return HttpResponse("""
# <div>
#                         <article>
#                         <header>welocme to the e-commerce website</header>
#                         <nav>
#                         <ul>
#                         <li>home</li>
#                         <li>search</li>
#                         <li>location</li>
#                         <li>city</li>

#                         </ul>
#                         </nav>
#                         </article>
#                         </div>
                        
# """)