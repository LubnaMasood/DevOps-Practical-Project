# DevOps Practical Project

## Author: Lubna Masood


## Contents

* [Objective](#Objective)
* [Trello Board](#Trello-Board)
* [ERD](#Entity-Relation-Diagram)
* [CI PIPELINE](#CI-PIPELINE)
* [Risk Assessment](#Risk-Assessment)
* [Front End](#Front-End)
* [Testing](#Testing)
* [Future Improvements](#Future-Improvements)
* [Acknowledgements](#Acknowledgements)




## Objective

The objective of this project was to produce an application consisting of four microservices, which interact with one another to generate objects using some defined logic. Service one will render templates and communicate with the 3 other services. Both services two and three will generate random objects; service four will also create an object- based on the objects generated from services two and three. 

The following constraints for this project were also set: 

* Kanban Board: Trello Board for project tracking
* Version Control: Git - using the feature-branch model via a cloud based CI server 
* CI Server: Jenkins
* Configuration Management: Ansible Playbooks 
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
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

## Entity Relation Diagram 


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

## Front End


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


## Acknowledgements

* Many thanks to the trainer Victoria Sacre for all her help and guidance. 
* The 22MarEnable1 Cohort for their support and advice 
* The CI Pipeline template is from QA Community.
