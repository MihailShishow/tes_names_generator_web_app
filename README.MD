# Names Generator

This application was initially designed as an attempt to create a tool for names generation for The Elder Scrolls games universe.

> In the future, more settings and universes may be added.

By using slightly modified code from [here](http://www.roguebasin.com/index.php?title=Markov_chains_name_generator_in_Python), this application helps to generate names for the characters of all of the playable races from The Elder Scrolls games, starting from the third chapter.

Base data was taken from the [the UESP](https://en.uesp.net/wiki/Lore:Names), then normalized and processed to generate new names.


# Technical information

This application was built using the following stack of technologies:

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [nginx](https://www.nginx.com/)
* [Docker](https://www.docker.com/)
* [Bootstrap 4](https://getbootstrap.com/)
* [Darkly theme for Bootstrap](https://bootswatch.com/darkly/)


# Setting up and running

In order to run the application, you need the following tools installed on your system:

* Docker
* docker-compose

If you are sure that those tools are present and set up properly, then run the following command in the root directory of the project:

> `docker-compose up --build -d`

Then open your browser and navigate to the following URL:

[localhost:5001](https://localhost:5001)

If you wish to stop the application, simply run the following command in the root directory of the project:

> `docker-compose down`

# Advanced information and setup

If you want to change the port, simply edit the file docker-compose.yml:

* section 'services'
* section 'nginx'
* section 'ports'
* change line `- 5001:80` to `- *your_port_of_choice*:80`


