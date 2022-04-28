# DevOps Practical Project

## Contents

* [Objective](#Objective)
* [Trello Board](#Trello-Board)
* [ERD](#Entity-Relation-Diagram)
* [CI PIPELINE](#CI-PIPELINE)
* [Risk Assessment](#Risk-Assessment)
* [4 Services](#4-Services)
* [Front End](#Front-End)
* [Testing](#Testing)
* [Future Improvements](#Future-Improvements)
* [Acknowledgements](#Acknowledgements)




## Objective

The objective of this project was to produce an application consisting of four microservices, which interact with one another to generate objects using some defined logic. Service one will render templates and communicate with the 3 other services. Both services two and three will generate random objects; service four will also create an object- based on the objects generated from services two and three. 

The following constraints for this project were also set: 

* Kanban Board: Trello Board for project tracking
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX


## Trello Board

To ensure that an agile methodology has been followed, the progress of this project was recorded and tracked on a Trello Board. Trello was utilised for this project because it is a user-friendly and visually attractive approach to present the project tracking. 

The Trello Board for this project can be broken down into the following categories:



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

## 4 Services

## Front End

## Testing 

## Future Improvements

## Acknowledgements

The CI Pipeline template is from QA Community.
