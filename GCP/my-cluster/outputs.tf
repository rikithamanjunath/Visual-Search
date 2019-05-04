//output "raddit_static_ip" {
//  value = "${google_compute_global_address.raddit_static_ip.address}"
//}

output "kubconfig" {
  value = "export GOOGLE_APPLICATIONS_CREDENTIALS=\"/Users/narendrabidari/rikitha-git/visualsearch-terraform/accounts/account.json\"\nRun command to configure access via kubectl:\n$ gcloud container clusters get-credentials ${module.my_cluster.name} --zone ${var.zone} --project ${var.project_id}   \n$ kubectl apply -f ./deploy-application/visualsearch.yml \n$ kubectl get services"
}
