# scrum standup app
sample project for building docker containers, deploying to kubernetes and connection to an AWS RDS instance.

## Clone
git clone https://github.com/BensonsPage/docker-kubernetes-awsrds

## Make Changes.
- make the changes on the flask app container in scrumstandupwebapp directory
- make the needed changes on database init.sql
- Ensure you have created the secrets on gitHub as indicated on .github/workflows/mail.yml

## Checkout changes to a branch in your repository.
- git checkout -b branch-name
- git add * # To include changes in the commit.
- git commit -m "Update my app" # To Commit your changes.
- git push origin branch-name # push the branch to the remote repository.
- Merge your changes to your main branch.
- If you encounter issues refer to this article.
- Check if worflow has run your database sript on RDS.


## Build your container locally and deploy to a single node cluster with K8s.
- navigate into the "docker-kubernetes-awsrds" and run below command
docker compose up 
- If you encounter error, make the changes and run below command to rebuild the image.
docker compose up -d --no-deps --build scrumstandupwebapp
- If all is well, proceed to deploy with kubernetes.
kubectl apply -f scrum-standup-webapp.yaml               
- Check the deployment with below command.
kubectl get deployments
- Check the service with below command.
kubectl get services 
- if you navigate to on your browser, you sould see your app running on http://localhost:30001
- You can as well see your pods running according to how many you launched.                                                                      



