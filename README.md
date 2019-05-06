## Table of Contents
* Deployment to HPC
   * [About the repo](#about-the-repo)
   * [Repository structure](#repository-structure)
   * [Steps to Run]()
* Deployment to GCP
   * [About the repo](#about-the-repo)
   * [Quick start](#quick-start)
   * [Repository structure](#repository-structure)
     * [terraform-modules](#terraform-modules)
     * [my-cluster](#my-cluster)
     * [Steps to Run]()
* Sample Recommendations

## Deployment to HCP

#### About the repository
We have the application files and the input and output files all moved to HPC  which is provided by San Jose State University.

#### Repository structure
```bash
├── FinalModel-Cosine
│      ├── images
│        ├── query_images
│        ├── Semi_images
│        ├── Semi_trian
│      ├──Pickles
│          ├── features_mnet
│      ├── model_mobilenet_semi.z
│      ├── Baseline_Model_mobilenet.ipynb
│      ├── Category_Prediction_Mobilenet.py
│      ├── Cosine_mobile.py
│      ├── SGD_Model.z
├── KMeans
│     ├── Baseline_Model_mobilenet.ipynb
│     ├── KMeans_Mobile.py
│     ├── Category_Prediction_Mobilenet.py
├── Baseline Model
│      ├── images
│        ├── query_images
│        ├── Semi_images
│        ├── Semi_trian
│      ├──Pickles
│          ├── features_mnet
│      ├── model.h5
│      ├── model_cnn_semi.json
│      ├── Baseline_Model.ipynb
│      ├── Category_Prediction.py
│      ├── MobileNet.py 
│    
├── Graph code
│     ├── Graph_Charts.ipynb

```
#### Steps to Run
#### Steps to run Final Model
   
Go to HPC/FinalModel- Cosine directory
```bash
1. You can pick one of the query image (input image) from the path below and place it in the FinalModel-Cosine/images/query_images folder

2. Download all these folders Semi_images, Semi_train and pickle files from the below link and place all the files in their respective folder paths
    https://drive.google.com/drive/u/1/folders/19lpENmOWaOXnYP8ouwBgf9l68qFrmFKx
    
3. Baseline_Model_mobilenet.ipynb is the main file to be executed. In order to execute this file, following files should be in the same current path
    model_mobilenet_semi.z : model file
    SGD_model.z : SGD model file
    Category_Prediction_Mobilenet.py : category prediction file
    Cosine_mobile.py : image similarity file
    
4. Change all the paths in the Baseline_Model_mobilenet.ipynb with their respective current paths
    model_path  : ./HPC/FinalModel-Cosine/model_mobilenet_semi.z
    image_path  : ./HPC/FinalModel-Cosine/images/Semi_images
    train_path  : ./HPC/FinalModel-Cosine/images/Semi_trian
    query_path  : ./HPC/FinalModel-Cosine/images/query_images
    pickle_path : ./HPC/FinalModel-Cosine/Pickles/features_mnet

5. Run the Baseline_Model_mobilenet.ipynb to retrieve final recommendations for the input query image
```  
#### Steps to run Baseline Model

Go to the HPC/Baseline Model directory
```bash
1. You can pick one of the query image (input image) from the path below and place it in the Baseline Model/images/query_images folder

2. Download all these folders model.h5, model_cnn_semi.json, Semi_images, Semi_train and pickle files from the below link and place all the files in their respective folder paths
    https://drive.google.com/drive/u/1/folders/1A6AtMd0SUnqZkyVsNaWAK6tShWsmmGdV
    
3. Baseline_Model.ipynb is the main file to be executed. In order to execute this file, following files should be in the same current path
     model_cnn_semi.json : model file
     model.h5 : model weights file
     Category_Prediction.py : category prediction file
     MobileNet.py : image similarity file
    
4. Change all the paths in the Baseline_Model_mobilenet.ipynb with their respective current paths
    json_path   : ./HPC/Baseline Model/model_cnn_semi.json
    model_path  : ./HPC/Baseline Model/model.h5
    image_path  : ./HPC/Baseline Model/images/Semi_images
    train_path  : ./HPC/Baseline Model/images/Semi_trian
    query_path  : ./HPC/Baseline Model/images/query_images
    pickle_path : ./HPC/Baseline Model/Pickles/features_mnet

5. Run the Baseline_Model_mobilenet.ipynb to retrieve final recommendations for the input query image

```  
####Steps to run KMeans Model

Go to the HPC/KMeans directory
```bash
Similarly place all the folders and change the paths, and run the Baseline_Model_mobilenet.ipynb
```
Graph codes are in Graph_Charts.ipynb for all the models 

## Deployment to GCP

#### About repository
We have reused the project https://github.com/Artemmkin/terraform-kubernetes
So that cluster can be built easily

This repository contains an example of deploying and managing [Kubernetes](https://kubernetes.io/) clusters to [Google Cloud Platform](https://cloud.google.com/) (GCP) in a reliable and repeatable way.

[Terraform](https://www.terraform.io/) is used to describe the desired state of the infrastructure, thus implementing Infrastructure as Code (IaC) approach.

[Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/) (GKE) service is used for cluster deployment. Since Google announced that [they had eliminated the cluster management fees for GKE](https://cloudplatform.googleblog.com/2017/11/Cutting-Cluster-Management-Fees-on-Google-Kubernetes-Engine.html), it became the safest and cheapest way to run a Kubernetes cluster on GCP, because you only pay for the nodes (compute instances) running in your cluster and Google abstracts away and takes care of the master control plane.  


#### Quick start
```bash
export GOOGLE_APPLICATION_CREDENTIALS="./accounts/account.json"   
#we might have to give full path
cd my-cluster
$ terraform init
$ terraform apply
```

After the cluster is created, run a command from terraform output to configure access to the cluster via `kubectl` command line tool. The command from terraform output will be in the form of:

```bash
$ gcloud container clusters get-credentials my-cluster --zone europe-west1-b --project example-123456
```


#### Repository structure
```bash
├── accounts
│   └── service-accounts
├── my-cluster
│   ├── deploy-app-example
│   └── k8s-config
│       ├── charts
│       │   └── gitlab-omnibus
│       │       ├── charts
│       │       │   └── gitlab-runner
│       │       │       └── templates
│       │       └── templates
│       │           ├── fast-storage
│       │           ├── gitlab
│       │           ├── ingress
│       │           └── load-balancer
│       │               └── nginx
│       ├── env-namespaces
│       ├── kube-lego
│       └── storage-classes
└── terraform-modules
    ├── cluster
    ├── firewall
    │   └── ingress-allow
    ├── node-pool
    └── vpc
```

#### terraform-modules
The folder contains reusable pieces of terraform code which help us manage our configuration more efficiently by avoiding code repetition and reducing the volume of configuration.

The folder contains 4 modules at the moment of writing:

* `cluster` module allows to create new Kubernetes clusters.
* `firewall/ingress-allow` module allows to create firewall rules to filter incoming traffic.
* `node-pool` module is used to create [Node Pools](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools) which is mechanism to add extra nodes of required configuration to a running Kubernetes cluster. Note that nodes which configuration is specified in the `cluster` module become the _default_ node pool.  
* `vpc` module is used to create new Virtual Private Cloud (VPC) networks.

#### my-cluster
Inside the **my-cluster** folder, I put terraform configuration for the creation and management of an example of Kubernetes cluster.
Important files here:

* `main.tf` is the place where we define main configuration such as creation of a network for our cluster, creation of the cluster itself and node pools.
* `firewall.tf` is used to describe the firewall rules regarding our cluster.
* `dns.tf` is used to manage Google DNS service resources (again with regards to the services and applications which we will run in our cluster).
* `static-ips.tf` is used to manage static IP addresses for services and applications which will be running in the cluster.
* `terraform.tfvars.example` contains example terraform input variables which you need to define before you can start creating a cluster.
* `outputs.tf` contains output variables
* `variables.tf` contains input variables

* `k8-confing` folder contains Kubernetes configuration files (**manifests**) which are used to define configuration of the running Kubernetes cluster.
It has 4 subdirectories inside:
    * `env-namespaces` contains manifests for creating [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), or virtual environments within the cluster, for running our services. In this example, `raddit-namespaces.yml` file is used to describe 3 namespaces: `raddit-stage` and `raddit-prod` for running [example application](https://github.com/Artemmkin/kubernetes-gitlab-example) (which is called raddit in this case) in different virtual environments, and `infra` namespace for running services vital to our infrastructure like CI/CD, monitoring, or logging software.
    * `storage-classes` folder is used to create storage classes that could be then used in [dynamic volume provisioning](http://blog.kubernetes.io/2017/03/dynamic-provisioning-and-storage-classes-kubernetes.html) for our applications.
    * `kube-lego` folder has the configuration required to run [kube-lego](https://github.com/jetstack/kube-lego) service which is used for automatic SSL certificates requests for our services running inside the cluster.
    * `charts` contains [Helm](https://github.com/kubernetes/helm) charts for deploying infra services. In this case it only has a chart for deploying [Gitlab CI](https://about.gitlab.com/features/gitlab-ci-cd/) along with a Runner.

* `deploy-app-example` has an bunch of Kubernetes objects definitions which are used to deploy nginx to a Kubernetes cluster. You can use the command below to deploy nginx to the cluster once it is created:

#### Steps to Run

Go to the cluster directory, execute the steps 
1. Bring Up a Cluster : Infrastructure Orchestrator 
   Go to the directory where google sdk is downloaded
    ```bash 
    ./terraform apply -lock=false
    ```
2. Specify to Use my gcp account : Store the ssh key in Path for use by terraform :
   Go the directory where account.json is placed
    ```bash 
    export GOOGLE_APPLICATIONS_CREDENTIALS="./visualsearch-terraform/accounts/account.json"
    ```
3. Validate my Key and get cluster details 
    ```bash 
    gcloud container clusters get-credentials visualsearch-cluster1 --zone us-west1-b --project visualsearch-232720
    ```
4. Ask Kubernetes to orchestrate the docker image
    ```bash 
    kubectl apply -f ./deploy-application/visualsearch.yml
    ```
5. Get my services:
    ```bash  
    kubectl get services
    ```
6. Get my pods:
    ```bash 
    kubectl get pods
    ```

## Sample Recommendations

![C](Top1.png)<br/>


