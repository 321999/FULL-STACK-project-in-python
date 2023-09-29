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
    return render(request,"index.html")





#     return HttpResponse("""
# <div>
#                         <article>
#                         <header>welocme to the e-commerce website</header>
#                         <nav>
#                         <ul>
#                         <li>home</li>
#                         <li>serach</li>
#                         <li>location</li>
#                         <li>city</li>

#                         </ul>
#                         </nav>
#                         </article>
#                         </div>
                        
# """)