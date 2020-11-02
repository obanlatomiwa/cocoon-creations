import uuid
import random
import string
from django.utils.text import slugify


def scramble_uploaded_image(instance, filename):
    extension = filename.split(".")[-1]
    return f'{uuid.uuid4()}.{extension}'


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, field=None, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        if field is not None:
            slug = slugify(field)
        else:
            slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
