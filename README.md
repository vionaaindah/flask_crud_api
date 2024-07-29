# flask_crud_api
 
# 🖥️ Deploy to Server with Available Port

## 📌Set up the Application on the Server

**1. Open Terminal**

**2. Navigate to the Directory to Clone the Project**


**3. Create Database and Database Table**

**4. Set Up Python Environment, including Python, `pip`, and `virtualenv`**

   - Linux/macOs
     ```bass
     sudo apt-get update
     sudo apt-get install python3-pip
     sudo pip3 install virtualenv
     ```
   - Windows
     ```bass
     python --version
     pip --version
     pip install virtualenv
     ```

**5. Clone Project from Repository GitHub and Navigate to the Directory**

```bass
git clone https://github.com/vionaaindah/flask_crud_api.git
cd flask_crud_api
```

**6. Create an Isolated Python Environment**
   - Linux/macOs
     ```bass
     virtualenv env
     ```
   - Windows
     ```bass
     python -m venv env
     ```

**7.Activate an Isolated Python Environment**
   - Linux/macOs
     ```bass
     source env/bin/activate
     ```
   - Windows
     ```bass
     env\scripts\activate
     ```

**8. Install dependencies**

```bass
pip install -r requirements.txt
```

**9. Open **`.env`** File**
   - Linux/macOs
     ```bass
     sudo vim .env
     ```
     <b>Note : </b> To **`editing file`**  type **`i`** and to **`save file`** click Esc and type **`:wq`**
   - Windows
     
     Open .env


**10. Configuring **`.env`****

Set all requirements needed

```
USERNAME_POSTGRE=
PASSWORD_POSTGRE=
DATABASE_POSTGRE=
HOST_POSTGRE=
USERNAME_MYSQL=
PASSWORD_MYSQL=
DATABASE_MYSQL=
HOST_MYSQL=
```

Save **`.env`**

**11. Run Application**
   - Start on Local Machine
     ```bass
     python run.py
     ```
     <b>Note:</b> use **`screen -r`** to enter screen already exist and **`ctrl+a d`** to exit from screen
