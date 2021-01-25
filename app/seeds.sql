DROP TABLE IF EXISTS trainers;

CREATE TABLE trainers (
    id serial PRIMARY KEY,
    brand VARCHAR NOT NULL,
    country VARCHAR
);

INSERT INTO trainers
    (id, brand, country)
VALUES
    (1, 'Nike', 'USA'),
    (2, 'Adidas', 'Germany'),
    (3, 'Mizuno', 'Japan');

