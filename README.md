# vehicleFactory

This project implements a vehicle factory system using Object Oriented Programming (OOP) principles in Python. The system consists of three main classes: Factory, Car, and Motorcycle.

## Overview

The system simulates a vehicle factory with two departments: the motorcycle department and the car department. Customers can request vehicles with specific requirements, such as fuel type, color, brand, and number of doors. The Factory class manages both the Car and Motorcycle classes, providing methods for creating and managing vehicles.

### User Story

A customer has requested a system for their vehicle factory. They want the system to support the following functionalities:

- Motorcycle Department:
  - Allow customers to request motorcycles with specific fuel types (electric, petrol, diesel).
  - Default number of wheels is 2.
  - Methods to change the model name and fuel type.
  - Print the total number of motorcycles created.

- Car Department:
  - Allow customers to request cars with specific attributes: color, brand, number of doors (2 or 4), and fuel type (electric, petrol, diesel).
  - Default number of wheels is 4.
  - Methods to change the model name, fuel type, color, and number of doors.
  - Print the total number of cars created.

### Technical Requirements

- Car and Motorcycle classes inherit from the Factory class.
- Count the total number of cars and motorcycles created.
- Ensure attributes are protected and accessible via methods.
- Implement `__str__` methods to print object attributes.
- Use abstract methods in the parent class for common functionality.


## Getting Started

1. Clone the repository to your local machine.
2. Set up a virtual environment (optional but recommended).
3. Install necessary dependencies (`pytest` for testing, etc.).
4. Create a new branch (`oop1`) to work on the OOP implementation.
5. Implement the classes according to the user story and technical requirements.
6. Write unit tests in `test_vehicleFactory.py` to ensure functionality.
7. Commit your changes and push to your remote repository.
8. Create a Pull Request from your `oop1` branch to `main` and merge the changes.