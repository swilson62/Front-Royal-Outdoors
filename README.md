# CS50W 2020 Final Capstone Submission - Front Royal Outdoors
 
The Django application "frontroyaloutdoors" is to be my submission for the final "Capstone" project in the CS50W 2020 class. It is my adaptation of the [https://frontroyaloutdoors.com/](https://frontroyaloutdoors.com/) website. This website is owned by a friend of mine who runs a local river outfitting business. The pictures were used with permission of [frontroyaloutdoors.com](https://frontroyaloutdoors.com/), and cannot be used without written permission. The web site allows users to reserve boats of various available types, for a given trip, on a given date.

This application is designed to be installed in any Docker environment. Loading can be accomplished on any machine with Docker installed, by running the command `docker-compose up -d` from the Django root directory. This will create 2 applications in Docker, a Django Web server, and a PostgreSQL server. Then you simply wait until the output from the command `docker-compose logs` indicates both Docker applications have started up successfully, and browse to the address `0.0.0.0:8000` in your favorite browser.

Included with this Django application is the `docker-compose.yml` file. This file defines the settings for both applications, as well as how to get everything started. A couple of interesting things to point out about this file include:

    - Django super user is automatically created with the credentials {username:admin, password:Pass@123}. Recommend changing this after load.
    - Defines PostgreSQL environment that uses a more secure password encryption (scram-sha-256) than default, as well as an environment variable which contains the "postgres" user password to be used.
    - Defines commands run to start the Django server. This includes:
        - The `wait-for-it.sh db:5432` script to control the startup order. This makes Django wait to start until the PostgreSQL server is up. This was discovered on the following sites:
            [https://docs.docker.com/compose/startup-order/](https://docs.docker.com/compose/startup-order/)
            [https://github.com/Eficode/wait-for](https://github.com/Eficode/wait-for)
        - The `startFrontRoyalOutdoors.sh` script, which defines how the Django web server is to start.
        
The `startFrontRoyalOutdoors.sh` script runs the following commands:
    
    - Runs `python3 manage.py migrate` to migrate the database from the `models.py` file, into the now running PostgreSQL database (DB) server.
    - Runs `python3 manage.py createsuperuser --noinput --username admin --email anonymous@example.com` to create the super user. This command uses a password supplied to the environment by the previous `docker-compose.yml` file.
    - Runs `python3 manage.py runscript populate`. This command uses the `runscript` extension supplied by installing the pip module `django-extensions`. This is used run the Python script `<project_root>/scripts/populate.py`. This script populates the Trip_Detail, Water_Craft, & Trip_Package tables in the DB. Info about running a script in the Django environment can be found on:
        [https://django-extensions.readthedocs.io/en/latest/](https://django-extensions.readthedocs.io/en/latest/) (see <project_root>/scripts/populate.py` for details).
    - Runs `python3 manage.py runserver 0.0.0.0:8000` to start the Django server.
    
I my opinion, this Docker setup, on top of a Django web server, PostgreSQL database, that also uses JavaScript, makes this more complicated than anything I created for any previous projects. I would also mention that this DB design is at least as complex, if not more so. The Python and JavaScript code used for this was also a lot more complicated in many ways than anything I have done before. There are a lot of possible failure modes for which I had to create error handling code in both JavaScript & Python. I can only hope I have found them all!

Upon opening the home page, the user is presented with a page with a Navigation bar along the top, and three links in the body of the page. These links are the three separate trip categories. The Nav bar also has a drop down list that allows navigation to any of the three categories, from any page. The Nav bar also contains a Home page Icon link on the top left, as well as a "Login" and "Register" link.

Clicking on any of these trip categories, takes you to a page that lists all of the trips from that category, as well as river level recommendations. Clicking on any of these trips takes you to a page that describes the trip, and the various trip packages available for that trip. Each trip package is for a different water craft type (Canoe, Solo Kayak, Tandem Kayak, etc...). Each trip package has a related price. There is a "Book-A-Boat" button at the bottom of this page, but this is not enabled until the user is authenticated.

Clicking on the Nav bar "Register" link, takes you to a registration page. Registration requires a username, first name, last name, email address, password, password confirmation, and telephone number. The telephone number input is checked by the `phonenumbers` module installed with `pip install django-phonenumber-field[phonenumbers]`. Info about a way to handle phone numbers came from:
    [https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models](https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models)  which referenced: 
    [https://github.com/stefanfoulis/django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field)

After registration is complete, the user is left logged in on the home page. One can also login with credentials using the `Login` Nav bar link. Once logged in, the right side Nav bar links change to show a Shopping Cart, and a link used to "Logout". There is a red badge, that shows the number of items that are currently saved in the users Shopping Cart. The users shopping cart uses local storage.

Now if one selects a trip category and specific trip, the "Book-A-Boat" button is enabled. Clicking on it opens a bootstrap modal. This modal allows the user to select the number of boats available for the trip selected. This is done by clicking on the Add and Subtract icons, to the right and left of a boat count. Clicking these icons uses JavaScript to adjust the boat counts. As soon as there are boats selected, a calendar pops up allowing the user to select a date. Once a date is selected, a time picker pops up, as well as a listing of the boat inventories that are currently available for the day selected. A price total is also calculated and displayed as boat counts are changed. Changing the boat count, or date selected, automatically re-calculates the available counts, and prices.

The calendar and time picker are both using the flatpickr datetime picker plugin found on [https://flatpickr.js.org/](https://flatpickr.js.org/) &  [https://github.com/flatpickr/flatpickr](https://github.com/flatpickr/flatpickr). I am using the `https://cdn.jsdelivr.net/npm/flatpickr` CDN rather than installing. The list of boats available for any given date is determined by sending an AJAX POST to one of the views. This view uses previous invoice lines for that date from the DB to do the calculation. There is also JavaScript that will take into account any items that have already been saved to the users Shopping Cart. The price total is also calculated JavaScript using info sent from the DB.

After the user clicks the "Add To Cart" button in the modal, and OK on the alert that notifies of a successful add, you will see that the red badge to the right of the shopping cart now shows an item in the cart. Clicking on "Shopping Cart", takes the user to a list of items in the cart. Clicking on any item will remove it from the list. If the list goes to zero, an alert notifies the user, and the user is redirected to the Home page. Clicking on the "Order" button, submits the order to the DB. This submission creates an invoice in the Invoice table related to the user, and as many invoice lines in the Invoice_Line table as needed. An alert is used to tell the user if the order submission was successful or not.

There are multiple checks used to verify inventory before any item can be submitted successfully. One example is the check that adjusts the quantity of boats selected, and gives an alert, if more than the number of boats available for that day has been selected. There is a separate check that occurs if there are 0 boats available when the date is selected. If there are no other boats selected, the calendar is zeroed out and torn down. If there are other boats are selected, those other boat counts and the calendar, will remain. These are all JavaScript checks, using data supplied by the server from the DB.

Another server side check occurs in `views.py`. This happens when one user selects a boat from inventory for some day, but doesn't immediately check out. Meanwhile another user selects the remaining boats from inventory, and submits the order. Now when the first user submits their order, there will not be enough boats in inventory. The server will see this, back out the invoice, and send a JsonResponse with a 403 status. The JsonResponse also contains a message about the boat type that failed, and the date. I decided to leave the Shopping Cart intact when this happens in case the user has multiple items, but recommended in the alert that the user delete the item that fails, then re-create with either a different boat type, or date.

This page has a few adjustments to make it mobile-responsive. Most of these adjustments are made using @media directives in the `styles.css` file. I use these to do things like adjust the text being displayed in a few strategic areas throughout the site.

Please enjoy this submission.

