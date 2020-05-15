#random string generator

import random
import string

def random_string_generator(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#print(random_string_generator())
#print(random_string_generator(size=50))


#slug generator
#in models.py => slug = models.SlugField(unique=True, max_length=80)

from django.utils.text import slugify

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    Pass the Queryset of a model for which you want to create a slug.
    """
    if new_slug is not None: #update_view
        slug = new_slug
    else:
        slug = slugify(instance.title[:60]) #limiting characters for a slug

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
