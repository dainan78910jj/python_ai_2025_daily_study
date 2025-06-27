CREATE TABLE employee_status (
    employee_status_id INT PRIMARY KEY,
    status_description VARCHAR(64)
)

CREATE TABLE technician (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL,
    email_address VARCHAR(64),
    annual_salary INT,
    special_skill VARCHAR(64),
    employee_status_id INT,
    FOREIGN KEY (employee_status_id) REFERENCES employee_status (employee_status_id)
)

CREATE TABLE city (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(64)
)

CREATE TABLE building (
    building_id INT PRIMARY KEY,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES city (city_id),
    floors INT
)

CREATE TABLE elevator_type (
    elevator_type_id INT PRIMARY KEY,
    type_name VARCHAR(64)
)

CREATE TABLE elevator_model (
    elevator_model_id INT PRIMARY KEY,
    model_name INT,
    speed INT,
    max_weight INT,
    people_limit INT,
    elevator_type_id INT,
    FOREIGN KEY (elevator_type_id) REFERENCES elevator_type (elevator_type_id)
)

CREATE TABLE elevator (
    elevator_id INT PRIMARY KEY,
    elevator_model_id INT,
    FOREIGN KEY (elevator_model_id) REFERENCES elevator_model (elevator_model_id),
    building_id INT,
    FOREIGN KEY (building_id) REFERENCES building (building_id),
    installation_date DATE
)

CREATE TABLE service_status (
    service_status_id INT PRIMARY KEY,
    status_description VARCHAR(64)
)

CREATE TABLE service_activity (
    service_activity_id INT PRIMARY KEY NOT NULL,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES technician (employee_id),
    elevator_id INT,
    FOREIGN KEY (elevator_id) REFERENCES elevator (elevator_id),
    service_date_time DATE,
    service_description VARCHAR(64),
    service_status_id INT,
    FOREIGN KEY (service_status_id) REFERENCES service_status (service_status_id)
)