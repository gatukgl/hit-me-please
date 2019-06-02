provider "google" {
  credentials = "${file("hitmebaby.json")}"
  project     = "hit-me-please"
  region      = "asia-southeast1"
  zone        = "asia-southeast1-b"
}

resource "google_compute_instance" "tf_instance" {
  name         = "tf-instance-${count.index}"
  machine_type = "n1-standard-1"
  count        = 3

  boot_disk {
    initialize_params {
      image = "ubuntu-1804-bionic-v20190530"
      size  = 30
    }
  }

  metadata = {
    sshKeys = "gatukgl:${file("~/.ssh/id_rsa.pub")}"
  }

  network_interface {
    network       = "default"
    access_config {}
  }
}

output "ip" {
  value = "${google_compute_instance.tf_instance.*.network_interface.0.access_config.0.nat_ip}"
}
