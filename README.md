1. Create a virual environment (Optional).

   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment.

   ```bash
   ./venv/Scripts/activate
   ```
3. Install Django and djangorestframework.

   ```bash
   pip install -r requirements.txt
   ```
4. cd into the ```blogsite``` folder.
   
   ```bash
   cd blogsite
   ```
5. Run makemigrations and migrate the blogs app.
   
   ```bash
   python manage.py makemigrations
   python manage.py migrate blogs
   ```
6. Run the server

   ```bash
   python manage.py runserver
   ```
Notes:
| Requirement | Action |
|----------|----------|
| 1.1 User Model   | imported from django.contrib.auth.models  |
| 1.2 BlogPost Model   | in /blogs/models.py   |
| 2.1 Listing blog posts  | go to "localhost:8000/blogs/blogs_list"  |
| 2.2 Creating blog posts | send a post request to (must have correct auth) "localhost:8000/blogs/write" |
| 2.3 Deleting blog posts | send a delete request to (must have correct auth) "localhost:8000/blogs/<int: blogpost_id>/delete" |
| 3.1 Simple User login view | go to "localhost:8000/blogs/accounts/login" |
| 3.2 Restrict creating to authenticated users | 1. login with correct credentials via "localhost:8000/blogs/accounts/login" 2. go to "localhost:8000/blogs/write" (will see default post handler of Django 3. delete "sessionid" cookie from browser, refresh and go to "localhost:8000/blogs/write" (will see authentication details not provided message)|
| 4 Optimizations| No attempts made |
| 5.1 home page and details page| go to "localhost:8000/blogs/" to see list of blogs; "localhost:8000/blogs/<int: blogpost_id>/" to see detailed blog |
| 5.2 Form for new blog posts | Not implemented |
| 6 Frontend | No attempts made |
| 7 Git and gitlab | no gitlab account, published to public github instead. |


   
