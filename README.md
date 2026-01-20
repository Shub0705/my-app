# my-app/
  ├── app.py
  ├── requirements.txt
  └── Dockerfile 
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
 
