
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
- [ ] ReWrite CSS
- [ ] Connect to DB on different computer
- [ ] Remove unnecessary entries from form
---EXPO functionality complete--
- [ ] Determine how to connect remotely (what is postgres host, why local host?)
- [ ] Add feedback to patient entry form: "patient entered successfully"
- [ ] Determine Health Status
- [ ] Search entries

#### Dependencies  
Flask  
Flask-SQLAlchemy  
FLask_WTF  
psycopg2
