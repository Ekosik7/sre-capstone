# SRE Capstone Project

## Prerequisites
- Terraform >= 1.5
- kubectl
- helm
- Docker
- Python 3.11+

## Step 1: Infrastructure
```bash
cd terraform/
terraform init
terraform plan
terraform apply
```

## Step 2: CI/CD
Push to main branch — GitHub Actions will build and deploy automatically.

## Step 3: Observability
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
kubectl create namespace monitoring
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --values monitoring/prometheus-values.yaml
kubectl apply -f monitoring/alerts.yaml
```

## Step 4: Deploy App & HPA
```bash
kubectl create namespace production
kubectl apply -f k8s/app.yaml
kubectl apply -f k8s/hpa.yaml
```

## Step 5: Load Testing
```bash
pip install locust
locust -f loadtesting/locustfile.py --host http://YOUR_APP_URL
```

## SLOs
| SLI          | Target  |
|--------------|---------|
| Availability | ≥ 99.5% |
| Latency p95  | ≤ 300ms |
| Error Rate   | ≤ 0.5%  |
| Throughput   | ≥ 100 RPS |
