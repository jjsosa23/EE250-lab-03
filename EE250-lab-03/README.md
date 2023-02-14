# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Jordan Sosa  
- Yaoyue Wang

## Lab Question Answers

Answer for Question 1: 

RESTful APIs are scalable because they have these features:

Statelessness: Each request has all the info it needs and doesn't rely on previous requests, so any server can handle it.

Cacheability: Requests can be saved, reducing server load and improving performance.

Layered System: The client, network, and server have separate jobs, making it easier to scale each part separately.

Loose Coupling: Changes to one part don't affect others, making it easy to scale as needed.

Standard Interface: The use of standard HTTP methods makes it easy to integrate with other systems and add new features.

Question 2: According to the definition of “resources” provided in the AWS article above,
What are the resources the mail server is providing to clients?

According the the definition of resources, the mail server is providing text and numbers.

Question 3: What is one common REST Method not used in our mail server? How could
we extend our mail server to use this method?

PUT method. Which updates server data. We can do this by creating a method that updates the inbox of the server without going through the get, add methdos

Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!

API keys are widely used because they are easy to implement, althought they are not that secure. Which is why APIs with not so sensitive information use it. API keys are used for authentication, the API key is unique and assigned to a specific client. 

From AWS article.
...