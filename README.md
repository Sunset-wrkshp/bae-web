
## Web (framework?) for BaeMax

#### Purpose

  * Webpage allows user to input patient information as a backup to the audio input.
  * Webpage allows an admin to access collected data from the database
  * Webpage allows an admin to search collected data from the database
  * Webpage allows an admin to edit collected data from the database

#### Should include

  * **main page**  
      * enter information

  * **/home or /about**
     * info about the project/home screen

  * **admin access:**
      * Provides admin information from database
      * number of patients
      * search for patients
      * directly input to database or edit current fields

#### TO DO:  
- [x] New DB User
- [x] Create DB
- [x] Connect to DB
- [ ] Use Bootstrap for HTML
- [ ] Connect to DB on different computer
- [x] Remove unnecessary entries from form  
- [ ] **Display Page:**
    * Text, Person's name, Their information. Top patient. Refresh on each new member. Image on the left, info on the right.  
    ---EXPO functionality complete--
- [ ] Determine how to connect remotely (what is postgres host, why local host?)
- [ ] Add feedback to patient entry form: "patient entered successfully"
- [ ] **Determine Health Status**
- [ ] Search entries
- [ ] Output page updates automatically
- [ ] Output page has interactive graph.

#### Dependencies  
Flask  
Flask-SQLAlchemy  
FLask_WTF  
psycopg2

### What am I doing today
* [x] Get the query running.  
* [x] Set up the display page to display information  
* [ ] Get Bootstrap CSS working for home  
* [ ] Get bootstrap CSS working for display page.  
* [ ] Upload to that website making website  

**if possible**
* [ ] look into auto updates
* [ ] Python to connect to postgres
