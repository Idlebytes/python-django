Installation instructions:

1. Install python3 (instructions based on Fedora 25)

# sudo dnf install python3

2. Install PIP package manager for python and upgrade PIP to latest version

# sudo dnf install python3-pip
# sudo pip install --upgrade pip

3. Install django framework

# sudo pip install django

4. Clone the repository and run the application

# git clone git@github.com:Idlebytes/python-django.git
# cd python-django
# python3 manage.py runserver

5. Access server using URL http://localhost:8000/


$$ Build Docker image

# docker build -t ubuntu_django_manual:latest .
# docker images

# docker run -itd <img name> 	=> this will run without binding host machine port, so you have to access with container ip
# docker run -p 8000:8000 -itd <img name> 	=> this will run with binding host machine port, so you can access as http://localhost:8000/ from host 

# docker exec -it <container id> bash	=> SSH to container
