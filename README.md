# DevOps Practical Project

## Author: Lubna Masood


## Contents

* [Objective](#Objective)
* [Trello Board](#Trello-Board)
* [Four Services Diagram](#Four-Services-Diagram)
* [CI PIPELINE](#CI-PIPELINE)
* [Risk Assessment](#Risk-Assessment)
* [Cloud Server: GCP](#Cloud-Server-GCP)
* [Jenkins Pipeline](#Jenkins-Pipeline)
* [Front End](#Front-End)
* [Testing](#Testing)
* [Future Improvements](#Future-Improvements)
* [Acknowledgements](#Acknowledgements)




## Objective

The objective of this project was to produce an application consisting of four microservices, which interact with one another to create a prize generator app. Service one will render templates and communicate with the three other services. Service two will generate a random number between 1-12; service three will generate a random word. Service four will create a prize amount- based on the information generated from services two and three.

The following constraints for this project were also set: 

* Kanban Board: Trello Board for project tracking
* Version Control: Git - using the feature-branch model via a cloud based CI server 
* CI Server: Jenkins
* Configuration Management: Ansible Playbooks 
* Cloud server: GCP virtual machines
* Containerisation: Docker - all four services are containerised and images are pushed to Dockerhub
* Orchestration Tool: Docker Swarm - the containers must be replicated across two VM's 
* Reverse Proxy: NGINX - the app is accessible to users through a reverse proxy 
* Webhooks: Triggers Jenkins Build When the Code has been altered

## Trello Board

To ensure that an agile methodology has been followed, the progress of this project was recorded and tracked on a Trello Board. Trello was utilised for this project because it is a user-friendly and visually attractive approach to present the project tracking. 

The Trello Board for this project can be broken down into the following categories:

<img width="1440" alt="Screenshot 2022-05-13 at 9 27 30 pm" src="https://user-images.githubusercontent.com/101265654/168384682-67794181-08f6-4515-91b3-4e82f4769d67.png">

* Project Resources: All things that are necessary for the project to be completed 

* User Stories: User stories are statements that exist to demonstrate the functionality of the application. 

* Putting them into stories allows me to follow a step-by-step procedure in creating these functionalities.

* Backlog: Are outstanding tasks that need to be completed for the completion of the project.

* In Progress: Are tasks that are currently being worked on and developed.  

* Done: The tasks that have been completed and added to the project. 

## Four Services Diagram

This project relies on four microservices that work with each other to create a functioning prize generator. Service one is the front-end component of the application. An HTML template (prizegenerator.html) allows users to see the page on their screens. A dice roll, word wheel spin and prize amount are generated for the users and displayed on the screen. 

For users to see their past spins, service two must generate a number randomly. Also, service three must generate a random word. The front-end then utilises GET requests to access the information, which is then sent to service four which performs a POST request from the front-end to display the data from the other services. 

The diagram below illustrates this process: 

<img width="607" alt="Screenshot 2022-05-16 at 2 54 06 pm" src="https://user-images.githubusercontent.com/101265654/168608898-b71cdb11-9d90-4c39-b674-ade77d43a838.png">

## CI PIPELINE

A CI pipeline or continuous integration pipeline diagram consists of associated frameworks, services and tools that have been used during the various development phases. The approach that I have taken for this particular project can be seen below in the diagram: 

<img width="1152" alt="Screenshot 2022-04-28 at 3 29 42 pm" src="https://user-images.githubusercontent.com/101265654/165776029-6618ea65-5c9a-4d77-bf8c-02fad3b86e59.png">

This pipeline allows for a rapid and straightforward process from development, testing and to deployment by automating the integration process. 

* Unit Testing: pytest- unit tests need to be run every time the code is updated to make sure that the microservices function correctly before the deployment stage. 

* Webhooks- automates the running of the CI pipeline in Jenkins whenever new code is pushed to the dev branch in GitHub.  

* Docker Compose: build and push- Jenkin's credentials system is used to handle logging into Docker Hub, the new images are then pushed to the GitHub repository. 

* Ansible: configure- ansible configures various things including reloading nginx with updates to the nginx.config file; setting up the swarm and joining the swarm on all worker nodes and installing docker and docker-compose dependencies.  

## Risk Assessment 

Beneath you can find my detailed risk assessment, which provides a comprehensive evaluation of the risks associated with the development of this project:

Here is the initial risk assessment I conducted at the start of development:

<img width="931" alt="Screenshot 2022-05-16 at 1 27 01 am" src="https://user-images.githubusercontent.com/101265654/168501283-18da6fa5-a011-471a-8b96-59ab9b92bef3.png">

Further risks were discovered and subsequently added as the project developed: 

<img width="916" alt="Screenshot 2022-05-16 at 1 26 19 am" src="https://user-images.githubusercontent.com/101265654/168501421-45a0060d-c493-4beb-868f-124112ce933d.png">

## Cloud Server: GCP

For this project, the cloud server utilised is GCP (Google Cloud Platform). Four medium-sized virtual machines were set to europe-west2-b; this allowed the VMs to work together harmoniously within the network. Each VM had its own role: 

**1. project2-instance:** constructs the application, connects to GitHub and holds the Ansible Playbook to configure the other three VMs.

**2. jenkins:** constructs SSH key pair to run the docker-compose.yaml file, configure nginx and run the Ansible Playbook. 

**3. swarm-manager:** the manager of the Docker Swarm maintains cluster management responsibilities. Allowing multiple containers to be deployed across various host machines. 

**4. swarm-worker:** the worker within the swarm is connected to the manager. The manager node sends tasks to the worker, which it receives and executes.

<img width="417" alt="Screenshot 2022-05-16 at 12 12 00 pm" src="https://user-images.githubusercontent.com/101265654/168580590-e0722aeb-4564-4330-bb23-0c6f7db354ed.png">

## Jenkins Pipeline 

For this project, Jenkins was utilised by creating a Jenkinsfile. Several bash scripts were executed to build the docker images for the four services to log in and push the images up to Dockerhub. My Dockerhub username and password were set as environmental variables; by creating secret text files in Jenkins Credentials to ensure the information is kept private. Once docker had successfully logged in, a command was given to push the newly built images up to Dockerhub.

The final stage in the pipeline was to run the Ansible script via the playbook and inventory files. By assigning the roles and tasks, I could direct the continuous deployment through Docker Swarm. A webhook was also included in the Jenkins pipeline; a git branch was connected to the webhook. Therefore, if a change were made to the application's code, this would trigger a new build- updating the app without causing downtime for users.

The Three Stages In The Pipline were as followed: 

* Testing app
* Build and push images
* Deploy

<img width="639" alt="Screenshot 2022-05-16 at 2 19 24 pm" src="https://user-images.githubusercontent.com/101265654/168601858-2c077de2-d418-4c93-b159-2fc4ad3416ba.png">

The successful build resulted in a functioning web application which produced the following console output:

<img width="639" alt="Screenshot 2022-05-16 at 2 21 09 pm" src="https://user-images.githubusercontent.com/101265654/168602174-6aa45f7e-0ad7-4128-9145-ff00e482344c.png">

## Front End

The entry point for this app is the homepage, navigated with the '/' url suffix. When a user enters the website, they are greeted with the page:

<img width="474" alt="Screenshot 2022-05-16 at 3 55 25 pm" src="https://user-images.githubusercontent.com/101265654/168622187-e8c46179-abd1-41a4-9e47-e059cd81d223.png">

The user sees the greeting message 'Welcome To Your Prize Generator!'. Beneath the greeting message, instructions are also displayed on the screen. Instructions are provided to the user to direct them on navigating the app. The user then clicks on the 'Press Here to Spin!' button.

They are redirected to the next page:

<img width="490" alt="Screenshot 2022-05-16 at 4 02 12 pm" src="https://user-images.githubusercontent.com/101265654/168623619-edbaf435-f3ec-4306-9bb8-b9a0ce5690b6.png">

This is the prizegenerator page, navigated with the '/prizegenerator' url suffix. A user sees the message 'Here Are Your Past Spins!. Below, a dice roll number, word wheel and prize amount are generated. The logic behind this app is that if an individual gets a random word that begins with the letter 'B', they win a random prize from the list. For instance, in the image above, a user landed on the word 'swimming'; hence, they did not win anything.

However, if they land on a word that begins with the letter B, then they win a prize, as seen below: 

<img width="590" alt="Screenshot 2022-05-16 at 4 15 16 pm" src="https://user-images.githubusercontent.com/101265654/168626152-01daefe0-004a-4610-ab2d-d87490a32e73.png">

Below the prize generator are two buttons. The 'Press Here to Spin Again' button allows users to keep spinning the wheel to get a different outcome. Also, there is a 'Go Back' button, which redirects users back to the homepage. 

## Testing 

Since there are four microservices within this application- all services were tested individually. A testing folder is also present within the services folders, consisting of the tests for that specific service. The software used for testing is specified in the 'testing.txt' file. In particular, **pytest-cov** is a package for pytest which allowed me to see the code coverage of the tests. 

Testing is also automated into the Jenkins Pipeline and is the first stage in the build. Therefore, if any of the tests fail, the build will stop and not deploy the failed code.

### Service 1 Tests: 

Two tests were written for Service One: 

 * A mock test which tests post and get requests for the prizegenerator page using patch.
 * An assert test which ensures the prizegenerator page loads. 

<img width="592" alt="Screenshot 2022-05-13 at 10 11 01 pm" src="https://user-images.githubusercontent.com/101265654/168390199-dbc0fe8f-8a6d-4c48-a469-1cdf03d932ec.png">

### Service 2 Tests: 

Three tests were written for Service Two:

* Three assert tests that test the page loads by returning a random number between 1 and 12.

<img width="586" alt="Screenshot 2022-05-13 at 10 17 02 pm" src="https://user-images.githubusercontent.com/101265654/168390784-67238af0-48cc-4d18-adc2-e932bca5b82d.png">

### Service 3 Tests: 

One test was written for Service Three:

* An assert test that tests the page loads by returning a random word choice. In this instance, it was the word 'running'.

<img width="592" alt="Screenshot 2022-05-13 at 10 15 18 pm" src="https://user-images.githubusercontent.com/101265654/168390624-2446e6d7-1cb8-4c49-931f-d53735ec614d.png">

### Service 4 Tests: 

Four tests were written for Service Four: 

* Four assert tests that test the page works correctly, using the information from services two and three. A random number and random word are entered into the test to see whether service four works correctly. 

<img width="584" alt="Screenshot 2022-05-13 at 10 20 09 pm" src="https://user-images.githubusercontent.com/101265654/168391105-d3de9279-b2e7-49ed-a13f-6a5cbfc32018.png">

## Future Improvements 

With more time the improvements that I would implement include:

* Add a database to hold users information.
* Improve testing to include integration testing.
* Using a locally hosted Nexus repository, instead of fetching the images from Dockerhub. 

## Acknowledgements

* Many thanks to the trainer Victoria Sacre for all her help and guidance. 
* The 22MarEnable1 Cohort for their support and advice.
* The CI Pipeline template is from QA Community.
