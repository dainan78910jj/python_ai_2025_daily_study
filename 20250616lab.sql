

CREATE TABLE Countries (
	country_id INT PRIMARY KEY,
	country_name VARCHAR(64) NOT NULL,
	region_id VARCHAR(20)
)


CREATE TABLE Dup_Countries (
	country_id INT PRIMARY KEY,
	country_name VARCHAR(64),
	region_id VARCHAR(20),
	capital VARCHAR(64),
	official_language VARCHAR(64),
	currency VARCHAR(5)
)

CREATE TABLE Countries_constraint (
	country_id INT PRIMARY KEY NOT NULL,
	country_name VARCHAR(64) NOT NULL,
	region_id VARCHAR(20) NOT NULL
)

CREATE TABLE Countries_question6 (
	country_id INT,
	country_name VARCHAR(64),
	region_id VARCHAR(20)
)


INSERT INTO Countries (country_id, country_name, region_id)
VALUES (1, "Sweden", "SE");

INSERT INTO Dup_Countries (country_id, country_name, region_id, capital, official_language)
VALUES 
(1, "Sweden", "SE","Stockholm", "Swedish"),
(2, "China", "CN","Beijing", "Chinese"),
(3, "Germany", "DE","Berlin", "FGerman")

UPDATE Dup_Countries
SET official_language = "German"
WHERE country_name = "GERMANY"


INSERT INTO Countries_question6 (country_id, country_name, region_id)
VALUES 
(1, "Sweden", "SE"),
(1, "Sweden", "SE");

INSERT INTO Countries_question6 (country_id, country_name, region_id)
VALUES 
(2, "China", "CN");


#DELETE FROM Countries_question6 where region_id="CN"


## insert should not work
INSERT INTO Countries_question6 (country_id, region_id)
SELECT 2, "CN"
FROM another_table
WHERE NOT EXISTS (
    SELECT 1 FROM Countries_question6 
    WHERE country_id = 2 AND region_id = "CN"
);

## insert okay because CM
INSERT INTO Countries_question6 (country_id, region_id)
SELECT 2, "CM"
FROM another_table
WHERE NOT EXISTS (
    SELECT 1 FROM Countries_question6 
    WHERE country_id = 2 AND region_id = "CM"
);

## inser okay because 3
INSERT INTO Countries_question6 (country_id, region_id)
SELECT 3, "CN"
FROM another_table
WHERE NOT EXISTS (
    SELECT 1 FROM Countries_question6 
    WHERE country_id = 3 AND region_id = "CN"
);


