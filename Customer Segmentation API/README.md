# Customer-Segmentation-Backend

HOW TO RUN THE PROJECT 
step 1 : git clone https://github.com/letzzBuild/Customer-Segmentation-Backend.git

step 2 : cd Customer-Segmentation-Backend

step 3 : pip install -r requirements.txt

step 3 : create a database customer_segmentation in using any tool

step 4 : python manage.py makemigrations

step 5 : python manage.py migrate

step 6 : python manage.py runserver 


step 7 : go to config.py file and add from email and to email as well as 
        login details from from email . By default google will not allow you to send email from python due to security issue . please go to below link and turn on the permissions. Make sure you again turn if off after showing the demo as it might lead to security risk of your account.