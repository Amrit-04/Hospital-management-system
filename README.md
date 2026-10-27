# City Hospital Management System 🏥

### Relational Database Management System (DBMS) CLI for Patient Registration, Room Allocation & Appointments

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![CLI](https://img.shields.io/badge/Interface-Interactive%20CLI-success?style=flat)](https://github.com/Amrit-04/Hospital-management-system)
[![Tabulate](https://img.shields.io/badge/Reports-Tabulate%20ASCII-blue?style=flat)](https://pypi.org/project/tabulate/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

The City Hospital Management System is an end-to-end relational database application built in Python with a MySQL backend. It streamlines inpatient room assignment, stay billing, doctor appointment scheduling, and patient record management through a structured terminal interface.

---

## 🛠️ Core Features

- **🏨 Inpatient Room Allocation & Stay Billing:**
  - Automated room assignment across room categories (General Ward, Semi-Private, Deluxe).
  - Calculates length of stay (`Check_out - Check_in`) and total bill amount dynamically.
- **👨‍⚕️ Doctor Appointment Booking:**
  - Schedules appointments with specialized physicians (Cardiology, Orthopedics, Pediatrics, General Medicine).
  - Validates and links patient IDs with allocated time slots.
- **📋 Patient Master Records:**
  - Secure patient registration with validated contact numbers, age, and unique Patient IDs.
- **📊 Clean Tabular Reporting:**
  - Formatted ASCII tables using `tabulate` for bills, appointment rosters, and patient manifests.

---

## 🗄️ Relational Database Schema

```mermaid
erDiagram
    Pdetails ||--o{ Bdetails : "bills"
    Pdetails ||--o{ Doc_App : "schedules"

    Pdetails {
        int PatientID PK
        varchar Name
        int Age
        varchar Phone_Number
    }

    Bdetails {
        int Bill_no
        int PatientID PK, FK
        date Check_in
        date Check_out
        int No_of_days
        int No_of_rooms
        varchar Room_type
        int Total
    }

    Doc_App {
        int PatientID FK
        varchar Doctor_Name
        varchar Specialization
        date Appointment_Date
    }
```

---

## 🚀 Setup & Installation

### Prerequisites

- [Python](https://www.python.org/) 3.8+
- [MySQL Server](https://dev.mysql.com/downloads/) installed and running locally

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Amrit-04/Hospital-management-system.git
   cd Hospital-management-system
   ```

2. **Install Python dependencies:**
   ```bash
   pip install mysql-connector-python tabulate
   ```

3. **Configure Database Credentials:**
   Open `hospital management pps.py` and update the MySQL connection parameters if your local MySQL user/password differs:
   ```python
   conobj = mysql.connector.connect(
       host="localhost",
       user="root",
       password="your_mysql_password"
   )
   ```

4. **Launch the Application:**
   ```bash
   python "hospital management pps.py"
   ```
   The application automatically creates the `hospital` database and required tables on its first run.

---

## 💻 CLI Menu Navigation

```
========================== CITY HOSPITAL MANAGEMENT ==========================
                        1. Assign a Room
                        2. Book an Appointment
                        3. Exit
======================================================================
```

---

## 📄 License

This project is licensed under the MIT License.