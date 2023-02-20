# [Delicious Cafe](https://delicious-site-reva-scpli.ondigitalocean.app/#)
## Introduction
Delicious Cafe is a web application built using the Python Django framework and utilizing HTML, CSS, and Bootstrap. This project was developed as part of our curriculum at Prog Academy and aimed to teach us the fundamentals of building web applications using Django.

## Sections
The web app consists of two main sections - the Home page and Log In page. In addition, there is a hidden Manager section that can only be accessed by users who belong to the 'manager' group. In the Manager section, the manager can process client applications and table reservations.

## Home
The Home section contains the following sub-sections:

> [About](https://delicious-site-reva-scpli.ondigitalocean.app/#about) - providing information about the restaurant <br>
> [Menu](https://delicious-site-reva-scpli.ondigitalocean.app/#menu) - showcasing the restaurant's menu with categories and dishes, including name, price, and ingredients <br>
> [Specials](https://delicious-site-reva-scpli.ondigitalocean.app/#specials) - featuring special dishes with descriptions and photos <br>
> [Events](https://delicious-site-reva-scpli.ondigitalocean.app/#events) - displaying current events <br>
> [Chefs](https://delicious-site-reva-scpli.ondigitalocean.app/#chefs) - showcasing the restaurant's crew <br>
> [Gallery](https://delicious-site-reva-scpli.ondigitalocean.app/#gallery) - a photo gallery of the restaurant <br>
> [Account](https://delicious-site-reva-scpli.ondigitalocean.app/#) - allowing account actions such as login and logout <br>
> [Contact](https://delicious-site-reva-scpli.ondigitalocean.app/#contact) - a contact form <br>
> [Book a Table](https://delicious-site-reva-scpli.ondigitalocean.app/#book-a-table) - a table reservation form <br>

## Styling
The app's front-end is designed using HTML, CSS, and Bootstrap. We have used a simple yet elegant template, which has been customized to match the branding of the restaurant.

## Manager Section
The Manager section is a hidden section only accessible to users belonging to the 'manager' group. In this section, the manager can process client applications and table reservations. Additionally, processed applications are archived and can be deleted if required.

## Conclusion
Delicious Cafe is a simple and elegant web application built using Django. It allows customers to view the restaurant's menu, make table reservations, and contact the restaurant. Meanwhile, the Manager section provides a streamlined way to process client applications and table reservations.

## Installing:
Clone the repository to your local machine using Git. Open your command prompt or terminal and navigate to the directory where you want to install the app. Then, run the following command:
```
git clone https://github.com/your-username/delicious-cafe.git
```
Create a virtual environment for the app. Navigate to the project directory and run the following command to create a virtual environment:
```
python -m venv env
```
Activate the virtual environment. Run the following command to activate the virtual environment:
```
source env/bin/activate
```
Note: If you are using Windows, you can activate the virtual environment by running env\Scripts\activate.

Install the required packages for the app. Run the following command to install the packages:
```
pip install -r requirements.txt
```
Set up the database. Run the following command to create the database tables:
```
python manage.py migrate
```
Create a superuser. Run the following command and follow the prompts to create a superuser:
```
python manage.py createsuperuser
```
Run the server. Finally, run the following command to start the server:
```
python manage.py runserver
```
Now you can open your web browser and navigate to http://localhost:8000 to see the Delicious Cafe app in action.
