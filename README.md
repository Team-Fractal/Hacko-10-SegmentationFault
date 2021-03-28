# Axios - Team SegmentationFault

> An integrated dashboard and issue tracker to automate common issues faced in universities, especially regarding the hostel accomodation. It aims to upheave the very inefficient, redundant and cumbersome system of issue tracking using physical notebooks; and replaces it with an elegant modern smart solution that harnesses the power of technology to vastly automate a multitude of aspects of the hostel life

There are two main aspects of the project : one being the student dashboard, where every student can register and have their own account, and file complaints, book laundry services, request room cleaning, and so on. The second part is the admin page, which lets the administrator see everything logged and requested by all the students, and then accept or decline it. Correspondingly, the student gets a notification on their personal account regarding the status of their filed log. Henceforth its a comprehensive and extremely convenient way to log and track issues both for the students as well as for the college/hostel administration.

## Screenshots 

[![Screenshot-20210307-061529.png](https://i.postimg.cc/3r1vY2dt/Screenshot-20210307-061529.png)](https://postimg.cc/grwJKXyh)

[![Screenshot-20210307-061608.png](https://i.postimg.cc/kXDBCzr5/Screenshot-20210307-061608.png)](https://postimg.cc/gnFYqM29)


## How to build and run Axios Sphere from source

> The below commands assume one is running a UNIX based system, such as macOS or any popular GNU/Linux distro

```bash
$ # Get a local copy of the code
$ git clone https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault
$ cd Hacko-10-SegmentationFault/'Axios Sphere'
$
$ # Virtualenv modules installation
$ virtualenv env
$ source env/bin/activate
$
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

## File Structure

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app logic and serve the static assets
   |    |-- settings.py                    # Django app bootstrapper
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                  # Master pages
   |         |    |-- base-fullscreen.html # Used by Authentication pages
   |         |    |-- base.html            # Used by common pages
   |         |
   |         |-- accounts/                 # Authentication pages
   |         |    |-- login.html           # Login page
   |         |    |-- register.html        # Register page
   |         |
   |      index.html                       # The default page
   |     page-404.html                     # Error 404 page
   |     page-500.html                     # Error 404 page
   |       *.html                          # All other HTML pages
   |
   |-- authentication/                     # Handles auth routes (login and register)
   |    |
   |    |-- urls.py                        # Define authentication routes  
   |    |-- views.py                       # Handles login and registration  
   |    |-- forms.py                       # Define auth forms  
   |
   |-- app/                                # A simple app that serve HTML files
   |    |
   |    |-- views.py                       # Serve HTML pages for authenticated users
   |    |-- urls.py                        # Define some super simple routes  
   |
   |-- requirements.txt                    # Development modules - SQLite storage
   |
   |-- .env                                # Inject Configuration via Environment
   |-- manage.py                           # Start the app - Django default start script
   |
   |-- ************************************************************************
```
### Todos

 - Geyser and Lift Integration (Using IoT Devices)
 - **Mess system and queue tracker**
 - *More hardware integrations and facilities*
 - Advance UI


### What Has Been Done

 - Fake data geyser temperature and lift tracking
 - **RSVP Confirm/Reject Requests Feature**
 - *Admin panel to track all the orders/requests made*
 - **Implemented Complains, Laundary System, Medical, Room Request**
 
 ### Tech
Axios uses these source projects to work properly:

* [Creative Tim's Black Dashboard](https://github.com/creativetimofficial/black-dashboard) - Basic dashboard template with login/signup pages!

And of course Axios itself is open source with a [public repository](https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault) on GitHub.




<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Kamalpreet-3223"><img src="https://avatars.githubusercontent.com/u/73851933?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kamalpreet-3223</b></sub></a><br /><a href="https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault/commits?author=Kamalpreet-3223" title="Code">💻</a> <a href="#design-Kamalpreet-3223" title="Design">🎨</a> <a href="#ideas-Kamalpreet-3223" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault/pulls?q=is%3Apr+reviewed-by%3AKamalpreet-3223" title="Reviewed Pull Requests">👀</a> <a href="#projectManagement-Kamalpreet-3223" title="Project Management">📆</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/kanchi-jain-6475881b5"><img src="https://avatars.githubusercontent.com/u/68802268?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kanchi Jain</b></sub></a><br /><a href="https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault/commits?author=kanchi2438" title="Code">💻</a> <a href="#design-kanchi2438" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/Samikmalhotra"><img src="https://avatars.githubusercontent.com/u/72279316?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Samik Malhotra</b></sub></a><br /><a href="https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault/commits?author=Samikmalhotra" title="Code">💻</a> <a href="#design-Samikmalhotra" title="Design">🎨</a> <a href="#ideas-Samikmalhotra" title="Ideas, Planning, & Feedback">🤔</a> <a href="#projectManagement-Samikmalhotra" title="Project Management">📆</a> <a href="#maintenance-Samikmalhotra" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/SupritBehera"><img src="https://avatars.githubusercontent.com/u/17498636?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Suprit Behera</b></sub></a><br /><a href="https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault/commits?author=SupritBehera" title="Code">💻</a> <a href="#design-SupritBehera" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/rohangupta91"><img src="https://avatars.githubusercontent.com/u/74780244?v=4?s=100" width="100px;" alt=""/><br /><sub><b>rohangupta91</b></sub></a><br /><a href="https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault/commits?author=rohangupta91" title="Code">💻</a> <a href="#design-rohangupta91" title="Design">🎨</a> <a href="#talk-rohangupta91" title="Talks">📢</a> <a href="#ideas-rohangupta91" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
