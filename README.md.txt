# MobilidadeUC - Campus Mobility System 🚲🛴

## Overview

This project is a comprehensive **Object-Oriented Management System** developed in **Java** for the *Programming* course. It simulates a shared mobility network for the University of Coimbra (UC), managing a fleet of vehicles (Bicycles, E-Bikes, and Scooters) and a diverse user base (Students, Professors, and Staff).

The system demonstrates core Software Engineering principles, including **Polymorphism**, **Data Persistence**, and **Robust Input Validation**, wrapped in a user-friendly Command Line Interface (CLI).

## ⚙️ Key Features

### Advanced OOP Architecture
* **Polymorphic Behavior:** A robust hierarchy of classes (`Veiculo` -> `Bicicleta`, `Trotinete`, `Ebike`) where each vehicle type calculates its own hourly cost dynamically based on specific attributes (e.g., battery type, passenger capacity).
* **User Profiling:** Distinct logic for different actors (`Estudante`, `Docente`, `NaoDocente`), applying automatic discounts and specific pricing tables via method overriding.

### Data Persistence & Serialization
* **Text Parsing:** Custom parser to load initial configurations (`users` and `fleet`) from structured `.txt` files, featuring error handling for corrupt data lines.
* **Binary Serialization:** Implementation of the `Serializable` interface to save and load the full history of rentals (`alugueres.obj`), ensuring data persistence between execution sessions.

### Robust Logic & Validation
* **Real-time Availability:** Automatic synchronization between the rental history and the fleet list to lock/unlock vehicles based on active timestamps.
* **Business Rules Engine:** Complex cost calculation algorithm that considers duration caps (max 8h chargeable/day), extra equipment fees (Helmets/Lights), and user-specific discounts.
* **Fault-Tolerant CLI:** A menu-driven interface protected against invalid inputs (e.g., trying to input letters in numeric fields) using `try-catch` blocks and validation loops.

### Professional Documentation
* **Javadoc:** Full code documentation utilizing HTML tags for structured descriptions of classes and methods, adhering to industry standards.

## 🛠️ Tech Stack

* **Language:** Java (JDK 21+)
* **Paradigm:** Object-Oriented Programming (OOP)
* **Concepts:** Inheritance, Encapsulation, Polymorphism, File I/O, Serialization, Exception Handling.
* **Tools:** VS Code, Git, Javadoc.

## 🚀 How to Run

### 1. Compile the Project
Navigate to the root folder and compile all Java files located in the source package:

```bash
javac -d bin src/ProjetoJAVA/*.java