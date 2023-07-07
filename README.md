# NeedABed
The web app implementation based off the NeedABed Android application

Team GDT (G4 Dev Team)
    a student led team at Weber State University in Ogden, Utah. 

Members: 
    Amanda 
    Braden
    Cayden Schroader
    Jaden
    Raven
    Vipen

Professor: Ted Cowan 

Project Advisor: Harrison Smith

This project was requested by and developed for Nomad Alliance in order to help those in need of temporary and eventually long term housing to find nearby locations that they can "Nab a Bed" from.

Nomad Alliance Repos:
https://github.com/Nomad-Alliance/NeedABed/blob/main/README.md


_________________________________________________________________________________________________________________________________________________

#### Environment Setup: ####

Currently, we are utilizing python 3.8 or higher, and Node 18 or higher. Please install those on your own.

The setup/ directory contains scripts to install dependencies and build the project lcoally:
From the setup/ directory, run the commands as follows:

linux:
$ ./linux-setup
$ ./linux-test
$ ./linux-start-servers

windows:
> .\windows-setup.ps1
> .\windows-test.ps1
> .\windows-backend-server.ps1
> .\windows-frontend-server.ps1

### Prior issues with node.js and expo###
please be advised that this currnet build has a bypass code imbedded in the package.json file 
    Depending on Node.js version running on your machines you may need to make a change with the expo start command
    Older Node =>  "expo start ",
    Newer Node =>  "set NODE_OPTIONS=--openssl-legacy-provider && expo start ",
