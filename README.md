Steps for running project:

1; set up an instance of pgadmin or any DBMS should work, i will be relaying instructions on how to do this in pgAdmin as it is what i know but the proccess should be simmilar if you use something else.    
2; after setting up your instance of pgAdmin clone the git repository.    
3; the database connections string is located i the database.py folder, the format of the string is commented just above it.    
4; after editing the string to include you details for your databse instance the project should be ready to run.    
5; at the bottom of the main folder there isa commented console command (uvicorn CORE.main:app --reload) that must be used to start the application.    
6; at this point the server and app should be running correctly and the endpoints, that are found in the routers folder can be tested.    
7; the front end should also work, run "landingPage.html" and follow the flow to explore the webbapp.    
