from datetime import date
users=[
    {'email':'juan@gmail.com',
    'first_name':'juan',
    'last_name':'lazo',
    'password':'fdf334',
    'is_Admin':True,
    'birthdate':date(1996,12,12),
    'bio':"todo el mundo esta loco",
    },
    {'email':'victor@gmail.com',
    'first_name':'Victor',
    'last_name':'Perez',
    'password':'12323424',

    },
    {'email':'laura@gmail.com',
    'first_name':'laura',
    'last_name':'saldaña',
    'password':'4435345',
    'birthdate':date(1990,11,25),
    },
    {'email':'steven@gmail.com',
    'first_name':'steven',
    'last_name':'Pin',
    'password':'3434344',
    'is_Admin':True,
    'birthdate':date(200,2,23),
    'bio':"steven el loco",
    },
]
from posts.models import user
for usuario in users:
    obj=user(**usuario)
    obj.save()
    print(obj.pk, ':', obj.email)