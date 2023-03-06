The code is designed to keep track of patients at the Nittany University Hospital,
where staff may enter and delete patient names in its database. It uses 3 HTML webpages(main, delete and add) and 
Flask in Python to implement the website functionality. SQLite database file stores all the data entered or deleted
by the user. 

When open the website link, the first thing that you see is the main page from which you can navigate to the
other two webpages to add and delete patient names with 2 buttons “Add Patient Name” and “Delete Patient Name”. 
main.html is used for the implementation of the design and functionality for this page. The code for the dropdown 
button is also there. 

Moving from to the add.html file, the code prompts the user to enter some information that is later submitted with
the “Add” Button to insert a record in the database; otherwise, the “Go Back” button is used to redirect to the 
Main Webpage. Once a newly added patient added, a PID is automatically generated and information of all the 
patients in the database is displayed. Here is where we refer to app.py to be access the database. 

delete.html follows the same logic. There are two buttons: "Delete" and "Go Back". The form is to be submitted 
with the “Delete” button to delete the specified record in the database; otherwise, the “Go Back” button is used 
to redirect to the Main Webpage. Before deletion, the information of all patients in the database is displayed on
the web page in the same format of the HTML table as it done for add page. After deletion, display the information
of all patients in the updated database on the same web page. The page also uses Bootstrap Modals to confirm user's
intention to delete the patient's name from the system. 
