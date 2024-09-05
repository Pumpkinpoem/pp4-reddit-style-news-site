### Error Documentation

#### 1\. **Database Configuration Errors**

**Error:**

*   Issues connecting to the database due to misconfiguration.

**Solution:**

*   Ensured that `DATABASES` setting in `settings.py` was correctly configured with the proper credentials and database engine (e.g., PostgreSQL or MySQL).

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your\_db\_name',
        'USER': 'your\_db\_user',
        'PASSWORD': 'your\_db\_password',
        'HOST': 'your\_db\_host',
        'PORT': 'your\_db\_port',
    }
}
```
#### 2\. **Static and Media Files Issues**

**Error:**

*   Static files and media files not being served correctly during development and production.

**Solution:**

*   Configured `STATIC_URL`, `STATICFILES_DIRS`, `MEDIA_URL`, and `MEDIA_ROOT` in `settings.py`.

```python
STATIC\_URL = '/static/'
STATICFILES\_DIRS = \[BASE\_DIR / "static"\]
MEDIA\_URL = '/media/'
MEDIA\_ROOT = BASE\_DIR / "media"
```
#### 3\. **Slug Field Not Populating Automatically**

**Error:**

*   The `slug` field in the `Post` model was not populating automatically from the title.

**Solution:**

*   Added a `save` method in the `Post` model to automatically generate the slug if it is not provided.

```python
def save(self, \*args, \*\*kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super().save(\*args, \*\*kwargs)
```
#### 4\. **Duplicate Username or Email Validation**

**Error:**

*   Users were able to register with duplicate usernames or emails.

**Solution:**

*   Added validation in the `ChangeUsernameForm` and `ChangeEmailForm` to check for existing usernames and emails.

```python
def clean\_username(self):
    username = self.cleaned\_data\['username'\]
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError("Username already exists.")
    return username

def clean\_email(self):
    email = self.cleaned\_data\['email'\]
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("Email already exists.")
    return email
```
#### 5\. **Template Not Found Errors**

**Error:**

*   Django could not find the templates resulting in `TemplateDoesNotExist` errors.

**Solution:**

*   Ensured the templates were correctly placed in the `news/templates/news` directory and verified that `TEMPLATES` setting in `settings.py` included the correct directories.

```python
TEMPLATES = \[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': \[BASE\_DIR / "templates"\],
        'APP\_DIRS': True,
        'OPTIONS': {
            'context\_processors': \[
                ...
            \],
        },
    },
\]
```
#### 6\. **Form Rendering Issues**

**Error:**

*   Forms were not rendering correctly, and widgets were not applied as expected.

**Solution:**

*   Used Django's widget customization in the `Meta` class of the form to apply the `SummernoteWidget`.

```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = \['title', 'content', 'category', 'image'\]
        widgets = {
            'content': SummernoteWidget(),
        }
```
#### 7\. **Authentication and Permission Issues**

**Error:**

*   Users were able to access restricted pages without proper authentication.

**Solution:**

*   Added `@login_required` decorator to views that required user authentication.

```python
from django.contrib.auth.decorators import login\_required

@login\_required
def create\_post(request):
    ...
```
#### 8\. **Deployment Issues**

**Error:**

*   Encountered errors while deploying to Heroku, such as missing dependencies and environment variables.

**Solution:**

*   Ensured all dependencies were listed in `requirements.txt`.
*   Configured environment variables in Heroku settings.
*   Added `Procfile` for Heroku.


web: gunicorn reddit_news.wsgi:application --preload --log-file - --log-level debug

#### 9\. **Cloudinary Configuration Errors**

**Error:**

*   Issues with Cloudinary integration, such as images not uploading correctly or API keys not being recognized.

**Solution:**

*   Configured Cloudinary settings in `settings.py` with proper API keys and ensured the environment variables were set correctly.

```python
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
  cloud\_name = 'your\_cloud\_name', 
  api\_key = 'your\_api\_key', 
  api\_secret = 'your\_api\_secret' 
)

CLOUDINARY\_STORAGE = {
    'CLOUD\_NAME': 'your\_cloud\_name',
    'API\_KEY': 'your\_api\_key',
    'API\_SECRET': 'your\_api\_secret',
}
```
example, the code get imported from env via

```python

CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')

cloudinary.config(
    cloud_name=CLOUDINARY_URL.split('@')[1].split('?')[0],
    api_key=CLOUDINARY_URL.split('//')[1].split(':')[0],
    api_secret=CLOUDINARY_URL.split(':')[2].split('@')[0],
    secure=True,
)
```
and then get fed to the correct place after the split above

```python
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': cloudinary.config().cloud_name,
    'API_KEY': cloudinary.config().api_key,
    'API_SECRET': cloudinary.config().api_secret,
    'SECURE': True,
}
```
DEFAULT\_FILE\_STORAGE = 'cloudinary\_storage.storage.MediaCloudinaryStorage'

*   Added the necessary Cloudinary environment variables to the deployment platform (e.g., Heroku).


heroku config:set CLOUDINARY\_CLOUD\_NAME=your\_cloud\_name
heroku config:set CLOUDINARY\_API\_KEY=your\_api\_key
heroku config:set CLOUDINARY\_API\_SECRET=your\_api\_secret

### Summary

By addressing these errors, we ensured that **Glad Tidings Times** was robust, secure, and functional.
Each solution was implemented to improve the overall stability and user experience of the application.