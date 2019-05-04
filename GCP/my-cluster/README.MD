/Users/narendrabidari/Documents/software/terraform apply -lock=false
export GOOGLE_APPLICATIONS_CREDENTIALS="/Users/narendrabidari/rikitha-git/visualsearch-terraform/accounts/account.json"
gcloud container clusters get-credentials visualsearch-cluster1 --zone us-west1-b --project visualsearch-232720
kubectl apply -f ./deploy-application/visualsearch.yml
kubectl get pods
kubectl logs -f visualsearch-deployment-7994f5bdfc-f8qbl


Bring Up a Cluster : Infrastrucurre Orchestrator  /Users/narendrabidari/Documents/software/terraform apply -lock=false
Use my account : Store the ssh key in Path for use by terraform :export GOOGLE_APPLICATIONS_CREDENTIALS="/Users/narendrabidari/rikitha-git/visualsearch-terraform/accounts/account.json"
Validate my Key and get cluster details  :  gcloud container clusters get-credentials visualsearch-cluster1 --zone us-west1-b --project visualsearch-232720
Run my image : Ask Kubernetes to orchestrate : kubectl apply -f ./deploy-application/visualsearch.yml
Get my services: kubectl get services
Get my pods :kubectl get pods

