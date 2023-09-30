from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helo(request):
    AVAILABLE_PRODUCT=[
        {"name":"trimmer","price":420,"desc":"this trimmer cut your hair from zero","rating":1},
        {"name":"kainchi","price":40,"desc":"this trimmer cut your hair from zero","rating":2},
        {"name":"blade","price":4,"desc":"this trimmer cut your hair from zero","rating":4},
        {"name":"astura","price":180,"desc":"this trimmer cut your hair from zero","rating":5}
    ]
    return render(request,"home/index.html",context={"AVAILABLE_PRODUCT":AVAILABLE_PRODUCT})
    # return HttpResponse("welcome <em>to ur</em> home <e>page</e>")


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
        {"NAME":"KIE","AGE":18},
        {"NAME":"ISHRE","AGE":23},
        {"NAME":"KIS","AGE":16},
        {"NAME":"KISH","AGE":23},
        {"NAME":"KI","AGE":23},

    ]
    text="""
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio ut debitis culpa explicabo tempore totam, aliquid earum porro dolorum repellat nemo, dolorem necessitatibus, quas ducimus! Saepe amet dicta quasi molestias maxime, odio deserunt itaque quae, eius, veniam sit natus repellat dolor dolore. Cumque veniam vel corporis voluptatibus enim mollitia harum, quam tenetur, totam fugit rerum sit ab autem voluptatum in aliquam dolore minima veritatis aut nobis, voluptas repellendus dolorum. Vitae eveniet quam numquam. Nobis voluptatum reiciendis sunt distinctio. Aliquam qui obcaecati impedit ea rerum a expedita error quibusdam vitae beatae. Laudantium debitis dolore facilis vitae porro nesciunt expedita voluptate dignissimos ipsam incidunt, omnis possimus, maiores eius! Mollitia officia ipsum facere ab magni. Possimus nostrum odit vero qui. Ex aspernatur recusandae nam distinctio commodi, expedita sequi natus tenetur blanditiis ut architecto. Aliquid aut illum, sit temporibus eum saepe nostrum explicabo soluta! Fugit ipsam nemo repellendus at accusantium earum expedita maiores, eligendi officia dolor, eius soluta cum quasi voluptatibus totam sit recusandae id error rem. Voluptatum in tempora ab facere cupiditate quae cumque laborum iusto voluptatibus tenetur culpa impedit placeat recusandae sapiente saepe commodi eius inventore sed perspiciatis animi, velit asperiores deleniti quis. Sint impedit quia exercitationem neque debitis provident cupiditate quas.

        """
    return render(request,"product/index.html",context={"loyal":loyal,"text":text})

def contact(request):
    return render(request,"product/contact.html")

def about(request):
    return render(request,"product/about.html")
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