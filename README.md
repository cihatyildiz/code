# Let’s Create Docker Image

https://docs.google.com/presentation/d/1tJ2E68p2GbasvQNy7-4Faby4pL0avNfJHNSMwkP_9Sc/edit#slide=id.p

# Basics

- What is a Container?
    
    Containers are isolated processes for your app and its components. Each component - the frontend React app, the Python API engine, and the database - runs in its own isolated environment, completely isolated from everything else on your machine.
    
    This isolation ensures they are completely separate from everything else on your machine, thereby reducing the risk of conflicts and enhancing security. 
    
    Furthermore, this setup enhances scalability as each component can be managed and scaled independently. It also improves your software applications' overall efficiency and performance, as each component has its own resources and can be optimized individually.
    
- What is a Container Image?
    
    A container image is a package that includes all of the files, binaries, libraries, and configurations to run a container.
    
    There are two important principles of images:
    
    1. Images are immutable. Once an image is created, it can't be modified. You can only make a new image or add changes on top of it.
    2. Container images are composed of layers. Each layer represented a set of file system changes that add, remove, or modify files.
    
- Container vs Virtual Machine
    
    ![Untitled](Let%E2%80%99s%20Create%20Docker%20Image%208c1ceb71731441d2b18c75a3b17ac237/Untitled.png)
    

### What is a docker base image?

A Docker base image is a container image used as a starting point to create a new image. It typically contains the minimal set of files and dependencies required to run an application or service, such as an operating system, system libraries, and basic tools. From this base image, additional layers are added to include the application code, libraries, and configurations needed for the specific use case.

### What is a Dockerfile?

A Dockerfile is a text document that contains a series of instructions on how to assemble a Docker image. 

It basically defines what goes into your Docker container environment. 

Dockerfiles are used to automate the process of creating Docker images by specifying the base image, installing dependencies, setting environment variables, copying files into the image, and configuring the container's runtime behavior. 

# Creating a Custom Image

Creating a base Docker image have a couple of steps. 

1. **Specify a Base Image**: Choose an appropriate base image for your application. For instance, a minimal OS like Alpine Linux for a lightweight container, or a specific language environment like python:3.8-slim.
2. **Setup the Environment**:
    - **Install Necessary Packages**: Use the `RUN` command to update package lists, install necessary packages, and clean up cache in a single layer to keep the image size down.
    - **Set Environment Variables**: Configure necessary environment variables using the `ENV` command for things like timezone, language settings, or application-specific variables.
3. **Copy Application Files**: Use the `COPY` or `ADD` command to transfer your application files from your local environment into the Docker image.
4. **Configure Network Ports**: Use the `EXPOSE` command to inform Docker that the container listens on specific network ports at runtime. This is crucial for web applications that listen on HTTP or HTTPS ports.
5. **Define Volume Points**: Use the `VOLUME` command to define mounted or shared directories. This is useful for databases or stateful applications that need to persist data.
6. **Execute the Application**: Define the command to run your application using `CMD` or `ENTRYPOINT`. `CMD` provides defaults for executing your container, while `ENTRYPOINT` allows you to configure your container to run as an executable.
7. **Optimize the Image**:
    - **Minimize Layers**: Combine RUN commands where possible to reduce layers, which helps to reduce the overall image size and build time.
    - **Security Scans**: Perform security scans on your image to identify and fix vulnerabilities. Tools like Docker Bench, Clair, or Trivy can be used.
    - **Use Multi-stage Builds**: In cases where your build environment differs from your runtime environment, use multi-stage builds. This allows you to build your application in one stage and copy only the necessary artifacts to a second stage, resulting in a smaller and cleaner final image.
8. **Document Your Dockerfile**: Comment each step in your Dockerfile to explain why certain actions are performed. This documentation is crucial for maintenance and for other team members to understand the build process.
9. **Build and Test the Image**: Use `docker build` to create your Docker image. Test the built image thoroughly to ensure it functions correctly and meets all operational requirements.
10. **Tag and Version Your Image**: Properly tag your Docker image with version numbers or other identifiers before pushing it to a registry. This helps in managing different versions and rollback scenarios.

# Base Images in Enterprise Environment

The application of base images in an enterprise environment opens the door to a host of compelling advantages, significantly improving the application development process:

### Consistency

Base images provide consistency across all applications.

1. All applications originate from an identical base, providing a uniform starting point.
2. The use of base images reduces the time and effort spent on debugging and resolving issues related to incompatible elements.

### Efficiency

The use of base images introduces a high level of efficiency in the process of Docker image creation. Instead of having to start from the very beginning each time, developers are given the opportunity to leverage what already exists.

- Developers can take advantage of the existing base images, saving them from the task of constructing a new image from the ground up every single time. This capitalizes on prior work and avoids wastage.
- Utilizing base images saves time and resources by eliminating redundant work, promoting efficient resource use.
- The methodology accelerates development cycles by enabling quicker startup and rapid iteration. This leads to faster delivery of applications and features, boosting productivity.

### Security

The security aspect of Docker base images offers numerous benefits:

- Pre-configured Security Settings: Base images come with the potential to be pre-configured with specific security settings and parameters. This functionality is a significant advantage, as it negates the need for manual configuration of these settings for each individual container.
- Simplified Security Management: The use of base images greatly simplifies the task of managing and maintaining a secure environment across all containers. This is achieved by establishing a secure baseline that all other containers can adhere to, ensuring uniform security standards throughout.
- Consistent Security Standards: By establishing a secure base for your Docker images, it is far easier to ensure that every subsequent layer added to the image also maintains these security standards. This results in a consistent security profile across all your Docker applications, regardless of the specific layers added on top of the base image.
- Proactive Approach to Security: Using base images promotes a proactive approach to security. By ensuring security in the foundational layer of your Docker images, you reduce the risk of breaches and other security incidents that can occur due to vulnerabilities in the additional layers.
- Peace of Mind and System Robustness: The use of secure base images provides peace of mind to developers, knowing that they have a secure foundation for their applications. Moreover, this contributes to a more robust overall system, as the risk of security incidents is significantly reduced.

### Maintenance

Base images facilitate easier maintenance.

- All Docker images derived from the same base image can be updated together when the base image is updated.
- Applications using these images receive updates simultaneously, ensuring they are always running the most current and secure version.
- This feature simplifies the maintenance process, allowing updates to be rolled out across all applications with minimal effort.
- It ensures no application is left running outdated or potentially insecure software.

In light of these advantages, it is clear that base images are an invaluable tool in an enterprise environment, contributing to a more consistent, efficient, and secure development process.

# Building A Base Image

- use dockerfile to build your image
- use build kit to build a container image
- 

# Using Base Images in Your Project

When using base images in your project, you'll want to start by selecting the right base image that suits your specific needs.

1. **Choosing the Base Image:** Depending on the needs of your application, you might choose a base image that already has certain software or libraries installed. Alternatively, you might choose a very minimal base image if you want to have more control over the specific components that get installed.
2. **Pull the Base Image:** Use the `docker pull` command to pull the base image from a Docker registry to your local machine.
3. **Create a Dockerfile:** In your project, create a Dockerfile. This file will contain the instructions to build your Docker image.
4. **Specify the Base Image:** At the top of your Dockerfile, use the `FROM` command to specify the base image you want to use.
5. **Add Additional Layers:** After specifying the base image, you can add additional layers to your Docker image by using commands like `RUN` (to run a command), `COPY` (to copy files from your local machine to the Docker image), and `CMD` (to specify what command should be run when a container is started from your Docker image).
6. **Build Your Docker Image:** Use the `docker build` command to build your Docker image based on the instructions in your Dockerfile.
7. **Test Your Docker Image:** After building your Docker image, you should test it to make sure it works as expected. You can do this by starting a Docker container from your Docker image and then interacting with it to ensure it behaves as expected.
8. **Push the Docker Image to a Registry:** Once you're satisfied with your Docker image, you can push it to a Docker registry (like Docker Hub) so that other people can pull and use your Docker image.

Remember, the base image is only the starting point. The real power comes from the additional layers you add, which customize the image to match your project's specific needs.

## Example 1

Here's a sample Dockerfile that uses Alpine as a base image, and adds a number of configurations for a Django application:

```sh
# Use the Alpine image as the base
FROM alpine:latest

# Update and add necessary packages
RUN apk update && apk add python3 py3-pip postgresql-dev gcc python3-dev musl-dev

# Create a directory for the application
RUN mkdir /app

# Set the working directory to the application directory
WORKDIR /app

# Copy the requirements file into the Docker image
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the Docker image
COPY . /app/

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV DJANGO_CONFIGURATION=Prod

# Add security settings
ENV SECURE_SSL_REDIRECT=True
ENV SESSION_COOKIE_SECURE=True
ENV CSRF_COOKIE_SECURE=True

# Add logging settings
ENV LOGGING_CONFIG={...}

# Add error settings
ENV DEBUG=False

# Expose the port Django will be served on
EXPOSE 8000

# Run the Django server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

```

This Dockerfile starts with the Alpine base image, installs the necessary Python packages, and sets up the Django application with a number of configurations for security, logging, and error handling.

## Example 2

[Make your own Docker base image from scratch](https://snehabiradar.medium.com/make-your-own-docker-base-image-from-scratch-33780c07e9f4)

[Let’s Create A Custom Docker Image](https://www.notion.so/Let-s-Create-A-Custom-Docker-Image-954ab9eaf92e4bae9781e78a79984895?pvs=21)
