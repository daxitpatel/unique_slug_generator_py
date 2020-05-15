#list view

from django.core.paginator import Paginator

def list_view(request):
	obj_list = BlogPost.objects.all()

	paginator = Paginator(obj_list, per_page=5)
	page_number = request.GET.get('page', 1) #by default=1.. so no need to pass page=1 evrytime
	page_obj = paginator.get_page(page_number)

	context = {
	        'page_obj': page_obj, #list of posts
	        'paginator': paginator,
	        'page_number': int(page_number),
	         }
    
	return render(request , 'list.html' , context)


#list.html

{% for i in page_obj %} #PRINT POSTS FROM page_obj
	<h3> <a href="{% url 'detail' i.slug %}">{{ i.name }}</a></h3>
	{% if i.img %}
	<img src="{{ i.img.url }}" alt="">
	{% endif %}
	<p>{{ i.msg }}</p>
	<a href="{% url 'edit' i.slug %}">edit</a> | <a href="{% url 'delete' i.slug %}">delete</a>
	<hr>
{% endfor %}


<ul class="pagination justify-content-center"> #pagination BAR..
{% for i in paginator.page_range %} #page_range=inbuilt query ref:django docs
	<li  class=" page-item {% if i == page_number %} active {% endif %}">
        <span><a class=" page-link" href="?page={{ i }}">{{i}}</a></span> #pass page=value to current view(list_view)
    </li>
{% endfor %}
</ul>
