# DevOps Pipelines

- This is a CI/CD pipeline integrated using GitHub Actions, Amazon ECS and Docker.

- Our workflow consists of 3 jobs : 
    1. Test
        - We have test on python 3.8, 3.9 and 3.10 
    2. Build
        - A docker image is built and pushed to Docker Hub [here](https://hub.docker.com/r/ramikammoun/flaskusersapp)
    3. Deploy
        - The image is deployed to ECS with a service that's exposed on port 5000.
    4. The end result
    ![image](https://github.com/ramiKammoun/DevOps_PipeLine_Trials/blob/main/captureResultat.png)
