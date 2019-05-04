provider "google" {
  version = "~> 1.19.0"
  project = "${var.project_id}"
  region  = "${var.region}"
}
