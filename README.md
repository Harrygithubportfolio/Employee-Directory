Here’s the entire `README.md` file, properly formatted with markdown syntax for your project:

```markdown
# **Employee Directory Project**

This is a Flask-based web application that allows users to manage an employee directory. It includes:
- A front-end built with HTML templates.
- A back-end connected to a MySQL database hosted on AWS RDS.
- Deployment on an AWS EC2 instance with Nginx as a reverse proxy.

---

## **Features**

- Add new employees (name, position, department).
- View a list of all employees.
- Data is stored securely in a MySQL database.

---

## **Project Setup**

### **Prerequisites**
- Python 3.8 or later
- MySQL database (AWS RDS or local MySQL)
- AWS EC2 instance (optional for deployment)

---

### **Steps to Run Locally**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Harrygithubportfolio/Employee-Directory.git
   cd Employee-Directory
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Create a MySQL database named `employee_directory`.
   - Use the following SQL script to create the `employees` table:
     ```sql
     CREATE TABLE employees (
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(100),
         position VARCHAR(100),
         department VARCHAR(100)
     );
     ```

5. **Configure Environment Variables**:
   Create a `.env` file in the project root with the following content:
   ```plaintext
   DB_HOST=your-database-host
   DB_USER=your-database-username
   DB_PASSWORD=your-database-password
   DB_NAME=employee_directory
   ```

6. **Run the Application**:
   ```bash
   python3 app.py
   ```

7. **Access the App**:
   Open your browser and visit:
   ```plaintext
   http://127.0.0.1:5000
   ```

---

## **Deployment on AWS**

### **Steps to Deploy on AWS EC2**

1. Launch an **Ubuntu EC2 instance** and connect to it using SSH.

2. Install Python and required packages:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip nginx -y
   ```

3. Set up the project on the EC2 instance:
   ```bash
   git clone https://github.com/Harrygithubportfolio/Employee-Directory.git
   cd Employee-Directory
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Configure Nginx as a reverse proxy:
   - Add a configuration file for the app:
     ```plaintext
     server {
         listen 80;
         server_name your-public-ip;

         location / {
             proxy_pass http://127.0.0.1:5000;
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
         }
     }
     ```
   - Restart Nginx:
     ```bash
     sudo systemctl restart nginx
     ```

5. Access the app using your EC2 public IP:
   ```plaintext
   http://your-public-ip
   ```

---

## **Future Enhancements**
- Add user authentication for secure access.
- Implement search and filtering functionality.
- Deploy with HTTPS using Let’s Encrypt.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Author**

**Harry**  
GitHub: [Harrygithubportfolio](https://github.com/Harrygithubportfolio)
```

