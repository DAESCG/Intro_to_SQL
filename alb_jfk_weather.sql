CREATE TABLE alb (
    date TIMESTAMP PRIMARY KEY,
    temperature FLOAT,
    precipitation FLOAT,
    max_t BOOL,
    min_t BOOL,
    wind_speed FLOAT,
    wind_direction TEXT
);

CREATE TABLE jfk (
    date TIMESTAMP PRIMARY KEY,
    temperature FLOAT,
    precipitation FLOAT,
    max_t BOOL,
    min_t BOOL,
    wind_speed FLOAT,
    wind_direction TEXT
);
