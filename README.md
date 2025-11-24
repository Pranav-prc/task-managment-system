
Task Management System – RESTful API

A production-ready Task Management System built using **FastAPI**, **PostgreSQL**, **Docker**, and **Nginx**.
The project supports **user authentication (JWT)**, **task CRUD operations**, **task assignment**, and **status management**, all documented using **OpenAPI/Swagger**.


Features
 1) User Authentication

* Register users
* Login with JWT
* Protected routes using OAuth2 Bearer tokens

 2) Task Management

* Create tasks
* View tasks
* Update tasks
* Delete tasks
* Filter tasks by `status` or `assigned user`
* Task statuses: `todo`, `in_progress`, `done`

 3) DevOps & Deployment

* Fully containerized using **Docker**
* Reverse proxy using **Nginx**
* Automated setup using PowerShell deployment script
* Works on **Windows** and **Linux**
  
4) Documentation

* API documented using Swagger
* Available at:

  * [http://localhost/docs](http://localhost/docs) (via Nginx)
  * [http://localhost:8000/docs](http://localhost:8000/docs) (direct backend)



Architecture Overview

```
Client → NGINX (Reverse Proxy) → Backend (FastAPI) → PostgreSQL DB
```

 Components

* FastAPI Backend – main RESTful API
* PostgreSQL** – relational database
* Nginx – reverse proxy, forwarding traffic to backend
* Docker Compose – orchestration


* Folder Structure
 
task-management-system/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── db/
│   └── main.py
│
├── nginx/
│   └── default.conf
│
├── scripts/
│   └── deploy.ps1
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


Setup & Installation

1) Clone the Repository

```bash
git clone <your-github-repo-url>
cd task-management-system
```

 2) Install Docker

Ensure Docker Desktop is running.

3)  Build & Start Services

```powershell
docker compose up -d --build
```

4)  Access the API
  Swagger via Nginx:
  [http://localhost/docs](http://localhost/docs)

  Swagger via FastAPI directly:
  [http://localhost:8000/docs](http://localhost:8000/docs)

---

5)  Docker Services

| Service | Port | Description         |
| ------- | ---- | ------------------- |
| nginx   | 80   | Reverse proxy       |
| backend | 8000 | FastAPI application |
| db      | 5432 | PostgreSQL database |

---

6) Authentication
   Registration (POST)

   ```
    /auth/register
  ```

   ### Login (POST)
  
```
/auth/login
```

Returns:

```json
{
  "access_token": "<JWT>",
  "token_type": "bearer"
}
```
7) Testing the API

After logging in:

Create a Task (POST)

```
/tasks/
```

Example body:

```json
{
  "title": "Finish API",
  "description": "Write full documentation",
  "due_date": "2025-12-10T00:00:00"
}
```

---

8) ![Uploading Folder Structure.png…]()
Deployment Script (Windows)

The script located at:

```
scripts/deploy.ps1
```

Performs:

* Stops running containers
* Builds backend
* Starts Nginx, Backend, and DB
* Displays service URLs

Run:

```powershell
./scripts/deploy.ps1

```

---

Agile Workflow (Jira) 
A Jira board was created with Epics and User Stories:

1) Epics

* User Authentication
* Task Management
* DevOps & Deployment
* Documentation

2) User Stories

* As a user, I can register
* As a user, I can log in
* As a user, I can create tasks
* As an admin, I can view all tasks
* As a user, I can update task status

3) Sprint Workflow

* Sprint Planning
* Assigning tasks
* Daily standups
* Updating statuses (To Do → In Progress → Done)
* Sprint Retrospective

Screenshots & Walkthrough (Anti-AI / Anti-Copy Verification)
link = https://drive.google.com/drive/folders/15ggnOhESPt9O5WjYryY0lZHSPlHi7tbb?usp=sharing

#Technology Choices

 1) FastAPI

* Fast, modern
* Automatic API docs

2) PostgreSQL

* Reliable relational database

 3) Docker + Docker Compose

* Easy deployment
* Same environment everywhere

 4) Nginx

* Production-grade reverse proxy

---

Troubleshooting

Nginx restarting?

Fix default.conf
(proxy_set_header must have 2 arguments)

Backend won’t start?

Check logs:

```
docker compose logs backend
```

Database connection error?

Check env variable:

```
DATABASE_URL
```

Docker not starting?

Run PowerShell as Administrator:

```
net start com.docker.service
```

---

Git Workflow

### Initialize

```
git init
git add .
git commit -m "Initial commit"
```

### Push to Github

```
git remote add origin <repo-url>
git push -u origin main
```

---

 **Project Completed Successfully**

✔ Backend
✔ Database
✔ Nginx Reverse Proxy
✔ Docker Deployment
✔ Agile Documentation
✔ Video/Screenshot Ready
✔ Fully Working API




