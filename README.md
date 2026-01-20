```bash
 my-app/
  ├── app.py
  ├── requirements.txt
  ├── Dockerfile
  └── jenkinsfile 
  ---
  ## Architecture
 ```bash
 Developer
   ↓ git push
GitHub / GitLab
   ↓ webhook (signed)
Jenkins
   ↓
Pipeline executes
```
 # Install required Jenkins plugins
 ```bash
Manage Jenkins → Plugins
```
✅ Git
✅ GitHub Integration
✅ GitHub Branch Source
✅ Pipeline
✅ Credentials Binding
## Restart Jenkins
## Create Jenkins credentials
```bash
Settings → Developer Settings → Personal Access Token
```
Permissions:
repo
admin:repo_hook

# Store token in Jenkins
Manage Jenkins → Credentials
→ Global → Add Credentials

## Configure Git Webhook (MOST IMPORTANT)
```bash
Go to GitHub repo: Settings → Webhooks → Add webhook
```
## Configure Jenkins webhook secret
Manage Jenkins → Configure System
Find GitHub section.
Add:

Credentials → github-token

Enable:
✅ Manage hooks
