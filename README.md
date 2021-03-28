# Axios - Team SegmentationFault

> Axios is not just a product but an ecosystem of tools to aid the entire university experience in both the academic and non academic sphere. The Axios ecosystem consists of four major subparts : Axios Sphere, Axios Cube, Axios Square and Axios Circle.

In the sphere of university education, especially in such turbulent times due to covid-19, universities are alternating between online and offline modes of education frequently. This brings in itself a new set of challenges, and we see a lot of potential for technology to bridge these challenges and hurdles in a significant way. In this context, Axios aims to be a bridge many of such challenges.


## Screenshots 

[![image.png](https://i.postimg.cc/4dRPS128/image.png)](https://postimg.cc/8FwLFLSW)
[![image.png](https://i.postimg.cc/9M19YP6w/image.png)](https://postimg.cc/YGGjpFqt)
[![image.png](https://i.postimg.cc/6QVt7tSY/image.png)](https://postimg.cc/R30jy5vH)
[![image.png](https://i.postimg.cc/J4y8Nbvy/image.png)](https://postimg.cc/PPk0h8th)

## Axios Sphere

Axios Sphere is an integrated dashboard and issue tracker to automate common issues faced in universities, especially regarding the hostel accomodation. It aims to upheave the very inefficient, redundant and cumbersome system of issue tracking using physical notebooks; and replaces it with an elegant modern smart solution that harnesses the power of technology to vastly automate a multitude of aspects of the hostel life. It involves automating room cleaning requests, mess feedback, hostel-related complaint portal, laundry requests, booking medical appointments at the university health center, and much more. Combined with a convenient admin dashboard panel, wherein the administrator can see all requests at one central place and then take action, it indeed is a one-stop solution for hostel management.

It is built using HTML/CSS/JS on the frontend and Django on the backend.

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

# Axios Cube

Axios Cube is a social media and blogging tool meant solely for the current students as well as the alumni of the same university. In the times of online education, which has totally changed the dynamic of social and professional interactions as well as networking, it serves as a handy tool to connect, interact and find like-minded batchmates and people with the same interests and skills. Furthermore, it serves as a portal for close interaction with alumni of an institution. Posts can be put up by anyone, with a functioning discussions and comments section to fuel discourse, be it on formal or informal topics, both academic and non-academic. All in all, it serves as a close tightly knit personalised community for an institution, not being as restrictive as professional global networking and recruitment tools such as LinkedIn or as informal and difficult to keep track of as messaging services like WhatsApp.

It is built using React along with Redux for state magement, and Node.js/Express on the backend and MongoDB database

## How to build Axios Cube from Source

[![image.png](https://i.postimg.cc/0Qtfyq24/image.png)](https://postimg.cc/CBqDcX8C)

```bash
$ # Get a local copy of the code
$ git clone https://github.com/Team-Segmentation-Fault/Hacko-10-SegmentationFault
$ cd Hacko-10-SegmentationFault/'Axios Cube'
$
$ # Install node modules
$ npm i
$ cd client
$ npm i
$ cd ..
$ npm run dev
```

# Axios Square

Axios Square aims to be a centralised platform to facilitate intra-college and intra-hostel buying, selling and trading of items and products. It is quite often that products such as old semester books, extra stationery and equipment which are no longer required by one person, are the exact things that people from different years or anyone else might require. It gives the opportunity to the seller to quickly gain extra cash for unwanted things, whilst giving the buyer reduced prices for things they want. It also provides the avenue for trading. 

Axios Square is currently a prototype, with the frontend implemented in HTML/CSS/Bootstrap/JS. The backend to support such a portal is yet to be made, but it is in our immediate future prospect to implement it.

# Axios Circle

Axios Circle is a mobile app that serves as a convenient way to access the services of the Axios ecosystem from handheld mobile devices. 

Axios Circle is also currently a prototye. The App is built using Flutter


### Todos

 - Geyser temperature and lift tracking integration (Using IoT Devices)
 - Mess allocation system using data driven dynamic models
 - Backend and general improvements for Axios Square prototype, the buying, selling, and trading portal
 - Integration with the rest of the ecosystem and the backend for Axios Circle, the prototype Flutter App 


### What Has Been Done

 - Fully functional Hostel Management system Axios Sphere, along with an admin panel 
 - Fully functional Social Media/Blogging platform Axios Cube, with the ability to make posts, comments and discuss, as well as modify your profile to add your details and interests
 - Frontend prototype for buying/selling/trading portal Axios Square
 - Flutter App prototype for the Axios ecosystem, Axios Circle
 
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
