# pythonCA_2Assignment


The application is created with the help of python Flask, HTML and CSS, The postgres is the database to store the application data, which is pre-created Tables and customer is the tabe to store the customer information and users_table to store the login user of the store manager to login, And to see the orders of the customer for the manager to keep the orders ready to collect for customers.
This application is for the people for click and collect where the customers just order on the application and the shop manager and staff will keep our order ready then the customer arrive at shop and collect the order with showing customer ID.
In python we used API's to route the data from html page to page, using @app.route and the function for the action in the form tag from the html to access it inthe python and recognizes it, and triggers it whenever the action is performed inside the html template.
The products are stored inside the .json file  can be accessed to customer and can order by selecting the items using the checkbox, when you click on submit you can see the results on the database aswell as in the home.html where it shows data stored in the database.
The same goes to the manager but the manager has a special feature which is login, when he logins he can see the customer information with items oredered same as the customer but in the different html template called adminhome.html can perform the search, edit, and delete operations aswell, but both the customer and manager can't edit the items purchased.
This is a simple application where customer and manger are the two roles where customer orders the groceries, and manager will process the orders by packing the stuff.
So here's the screenshots below to show the pages how they are designed.


![image](https://github.com/gunasimhareddy72/pythonCA_2Assignment/assets/67228880/22e76736-548e-49ad-bcf4-0118a52a89f8)
![image](https://github.com/gunasimhareddy72/pythonCA_2Assignment/assets/67228880/fd9d2e0b-b8e9-4b80-a106-fd20f1dded1a)
![image](https://github.com/gunasimhareddy72/pythonCA_2Assignment/assets/67228880/92984741-1d2e-4c2a-90eb-9040ee1357c2)
![image](https://github.com/gunasimhareddy72/pythonCA_2Assignment/assets/67228880/f9238837-da5c-47ca-b5a1-ef988a87fc64)
![image](https://github.com/gunasimhareddy72/pythonCA_2Assignment/assets/67228880/67cb583b-7233-4b89-8c5b-ff8508442e5c)
![image](https://github.com/gunasimhareddy72/pythonCA_2Assignment/assets/67228880/c811e481-8c6f-4aaf-a4c5-b1b51cae409e)


Contribution:
Mahendra Vajja(10639742):
* Created the API for editcustomer.html.
* Created the API for get_customer_details.
* Created the API for edit_customer.
* Created the API for searchadmin.
* Created the API for /edit_customer_admin.
* Created the API for get_customer_details_admin.
* Created the API for delete_customer_admin.
* Customer form to enter the customer details.
* Written the html files.
* Correct the errors in html and css with help of my group mate.

Guna Simha Reddy(10628714)
* setting up the project structure.
* connecting the database to the python.
* creating the required files and naming them.
* creating the api for index.html, login.html, adminhome.html.
* creating the API route for submit button in the customer form.
* searching for customer API in the home.html.
* Deleting the customer API in the home.html.
* sql queries to create the tables inside the postgres database.
* written css for the html.








References:
https://www.w3schools.com/html 
https://stackoverflow.com/questions/70585322/i-cant-find-the-correct-syntax-for-select-from
https://medium.com/@premnathm/implementing-login-functionality-in-a-flask-application-64929c6f146e
https://raw.githubusercontent.com/bradtraversy/myflaskapp/master/app.py
https://www.fullstackpython.com/flask-templating-render-template-examples.html
https://pytechacademy.medium.com/user-authentication-with-flask-from-login-to-a-welcome-page-110f685f5e6f
https://flask-ptbr.readthedocs.io/en/latest/quickstart.html
https://raw.githubusercontent.com/MicrosoftDocs/mslearn-python-products/main/app.py
https://www.reddit.com/r/learnpython/comments/15ptdgx/need_help_with_school_project_cant_seem_to_mkae
https://stackoverflow.com/questions/65788900/text-seems-a-bit-blurry-on-a-backdrop-blur-html-css
https://www.answeroverflow.com/m/1224035009459916892/ 
https://youtu.be/v3CSQkPJtAc (youtube video link)





