# WEB_HW_10

poetry init
poetry add django
poetry shell      
django-admin startproject quotes
cd quotes
docker run --name noteapp-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres
# Change settings.py - set db
poetry add psycopg2
python manage.py migrate
python manage.py createsuperuser

# add midels to quote/models.py
python manage.py startapp quote
python manage.py makemigrations
python manage.py migrate
# quote/admin.py - register models
# add main page to quote/templates/quote
# quote/views.py - implement function 'main' to process requests to app
# web_hw_10/urls.py - register routes
# quote/urls.py - create urls file with routes
# web_hw_10/quote/templates/quote/base.html - create templates
# web_hw_10/quote/static/quote/style.css - create styles
# web_hw_10/quote/templates/quote/tag.html - add template for tags
# web_hw_10/quote/forms.py - add form, responsible for validation and data storing
# quote/views.py - add function which will be responsible for process POST requests for creation of new tags
# quote/urls.py - add a route with a processor: path('tag/', views.tag, name='tag'),
# web_hw_10/quote/templates/quote/quote.html - template for creation of a quote
# forms.py - creation of a form for quotes
# quote/views.py - add function of representation for a quote
# quote/urls.py - add route for processing of quotes
# quote/views.py - add function 'detail' to output template of a quote
# quote/urls.py - add new route to represent content of a quote
# web_hw_10/quote/templates/quote/details.html - add template for content of a quote
# web_hw_10/quote/templatetags/extract_tags.py - add mechanism for creation of individual tags
# quote/views.py - change func main to process custom tags, add funcs: 'set_done', 'delete_note'
# quote/urls.py - add routes to call previously added functions
# web_hw_10/quote/templates/quote/index.html - update to manage quotes and tags

# python manage.py startapp users - to create app for registration of users
# web_hw_10/web_hw_10/settings.py - add app users
# web_hw_10/web_hw_10/urls.py - add route to the new app 'users'
# web_hw_10/users/forms.py - create file and add model of registration
# web_hw_10/users/views.py - create processor of a route 'sign_up_user'
# web_hw_10/users/templates/users/sign_up.html - add html
# web_hw_10/users/urls.py - add route of users registration
# web_hw_10/users/forms.py - add model of login
# web_hw_10/users/templates/users/login.html - add html file login
# web_hw_10/users/views.py - create processor of a route 'login_user'
# web_hw_10/users/urls.py - add route of users login
# web_hw_10/users/views.py - create processor of a route 'logout_user'
# web_hw_10/users/urls.py - add route of users logout
# web_hw_10/quote/models.py - add relation user-quote
# "python manage.py makemigrations" - execute command
# "python manage.py migrate" - execute command
# quote/views.py - add processing of users with (
#   change functions: 'main', 'tags', 'quote', 'detail', 'set_done', 
#       'delete_quote'
# )
# web_hw_10/users/views.py - add profile's representation
# web_hw_10/users/urls.py - add route of users profile
# web_hw_10/users/templates/users/profile.html - add template for a profile
# web_hw_10/users/models.py - extend User model
poetry add pillow
# web_hw_10/users/admin.py - register Profile model
python manage.py makemigrations
python manage.py migrate
# web_hw_10/web_hw_10/settings.py - change setting for availability to save files locally
# web_hw_10/web_hw_10/urls.py - configure urls.py to process uploaded  media files by users under developer mode (debug=True)
# web_hw_10/users/signals.py - create file for availability of creation and saving of profiles
# web_hw_10/users/apps.py - update file for connection of receivers in this file though the import of signals
# web_hw_10/users/forms.py - create form to update and display users info in a template
# web_hw_10/users/views.py - update representations to add created forms
# web_hw_10/quote/templates/quote/base.html - add to a main page's menu a link to a profile

# pwd: qwertyhgfdsa / azsxdc321



# from django.contrib.auth.models import User
# from users.models import Profile  # Replace 'your_app' with the actual name of your app

# users_without_profiles = User.objects.filter(profile__isnull=True)

# for user in users_without_profiles:
#     Profile.objects.create(user=user)





# run server: python manage.py runserver
# stop server: CTRL + C
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/admin
