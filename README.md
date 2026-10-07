# weekend-app01

Static web front end for the `weekend-lab` cluster. NGINX serves the page and proxies `/api/` to App02 and `/app03/` to App03 using Kubernetes DNS.

## Test

```sh
python3 -m unittest discover -s tests -v
hadolint Dockerfile
```

## Run locally

```sh
podman build -t weekend-app01:dev .
podman run --rm -p 8080:8080 weekend-app01:dev
curl --fail http://localhost:8080/healthz
```

Commits to `main` publish `ghcr.io/phelun/weekend-app01:<full-git-sha>`. Pull requests test, lint, build, and scan without publishing.
