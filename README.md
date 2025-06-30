This project demonstrates a complete DevOps workflow to deploy a simple Python-based Clients API (Flask) with MongoDB as a datastore on AWS EKS using GitHub Actions CI/CD. The application is exposed over HTTPS using an NGINX ingress controller and TLS certificates managed by Cert-Manager with Let's Encrypt.

✅ Key Features
Clients API: A minimal Flask app with / and /clients endpoints backed by MongoDB.

- MongoDB: Deployed as a Kubernetes Deployment and Service.

- EKS Deployment: Application and services deployed on AWS EKS.

- Ingress + TLS: Exposed via Ingress on clients.api.deltacapita.com with TLS from Let's Encrypt.

- Cert-Manager: Automates certificate provisioning using a ClusterIssuer.

- CI/CD with GitHub Actions:

- Builds and pushes Docker image to Amazon ECR

- Applies Kubernetes manifests to deploy the stack

⚠️ Note
The domain clients.api.deltacapita.com is used as per the assessment requirement but was not configured in DNS, since it is owned by the company. The deployment assumes the DNS is correctly pointed to the EKS Ingress Load Balancer for full HTTPS validation.

Attached some screenshots of EKS Cluster for Reference in screenshot folder in root directoy.

