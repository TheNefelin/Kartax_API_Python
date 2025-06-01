-- --------------------------------------------------------------
-- --------------------------------------------------------------

-- Crear la base de datos
CREATE DATABASE db_testing;
-- Crear el usuario
CREATE USER testing WITH PASSWORD 'testing';
-- Dar privilegios sobre la base de datos
GRANT ALL PRIVILEGES ON DATABASE db_testing TO testing;
-- Dar permisos sobre el esquema 'public'
GRANT USAGE ON SCHEMA public TO testing;
GRANT CREATE ON SCHEMA public TO testing;

-- Tablas -------------------------------------------------------
-- --------------------------------------------------------------

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    img VARCHAR(100) NOT NULL,
    is_enable BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    category_id INTEGER NOT NULL REFERENCES categories(id),
    name VARCHAR(100) NOT NULL,
    is_enable BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    group_id INTEGER NOT NULL REFERENCES groups(id),
    name VARCHAR(100) NOT NULL,
    description VARCHAR(256) NOT NULL,
    img VARCHAR(100) NOT NULL,    
    is_fractional BOOLEAN DEFAULT FALSE,
    base_unit VARCHAR(20) NOT NULL,
    sale_unit NUMERIC DEFAULT NULL,
    stock NUMERIC DEFAULT 0,
    parent_product_id INTEGER REFERENCES products(id),
    waste_percentage NUMERIC(5,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stock_movements (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    movement_type VARCHAR(20) NOT NULL CHECK (movement_type IN ('sale', 'adjustment', 'restock')),
    quantity NUMERIC NOT NULL,
    movement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    note TEXT
);

-- Data ---------------------------------------------------------
-- --------------------------------------------------------------

INSERT INTO categories 
    (name, img, is_enable) 
VALUES
    ('Para Beber', 'grupo_01.jpg', TRUE),
    ('Tablas', 'grupo_03.jpg', TRUE),
    ('Para chanchear', 'grupo_02.jpg', TRUE);

INSERT INTO groups 
    (name, category_id, is_enable) 
VALUES
    ('Cervezas Artesanales', 1, TRUE),
    ('Cervezas Envasadas', 1, TRUE),
    ('De la Casa', 2, TRUE),
    ('Hamburguesas', 3, TRUE),
    ('Completos', 3, TRUE);

-- Barriles (30L)
INSERT INTO products 
    (group_id, name, description, img, is_fractional, base_unit, stock)
VALUES
    (1, 'Pils (Barril 30L)', 'Cerveza artesanal rubia en barril de 30 litros', 'pils_pinta.webp', TRUE, 'litros', 30),
    (1, 'Santa Sed (Barril 30L)', 'Cerveza artesanal ámbar en barril de 30 litros', 'santa_sed_pinta.webp', FALSE, 'litros', 30),
    (1, 'Blood (Barril 30L)', 'Cerveza artesanal roja en barril de 30 litros', 'blood_pinta.webp', TRUE, 'litros', 30);

-- Pintas (0.5L), fraccionadas del barril
INSERT INTO products 
    (group_id, name, description, img, base_unit, sale_unit, stock, parent_product_id)
VALUES
    (1, 'Pinta de Pils', 'Pinta de 0.5L de cerveza rubia artesanal', 'pils_pinta.webp', 'litros', 0.5, 0, 1),
    (1, 'Pinta de Santa Sed', 'Pinta de 0.5L de cerveza ámbar artesanal', 'santa_sed_pinta.webp', 'litros', 0.5, 0, 2),
    (1, 'Pinta de Blood', 'Pinta de 0.5L de cerveza roja artesanal', 'blood_pinta.webp', 'litros', 0.5, 0, 3);

INSERT INTO products 
    (group_id, name, description, img, base_unit, sale_unit, stock)
VALUES
    (2, 'Heineken', 'Cerveza envasada Heineken 330ml', 'heineken.webp', 'unidad', 1, 0),
    (2, 'Kross', 'Cerveza envasada Kross 330ml', 'kross.webp', 'unidad', 1, 0),
    (2, 'Kunstmann', 'Cerveza envasada Kunstmann 330ml', 'kunstmann.webp', 'unidad', 1, 0),
    (2, 'Budweiser', 'Cerveza envasada Budweiser 330ml', 'budweiser.webp', 'unidad', 1, 0),
    (2, 'Royal', 'Cerveza envasada Royal 330ml', 'royal.webp', 'unidad', 1, 0);

INSERT INTO products 
    (group_id, name, description, img, base_unit, sale_unit, stock)
VALUES
    (3, 'Tabla de Carne', 'Tabla con variedad de carnes', 'tabla_carne.webp', 'unidad', 1, 0),
    (3, 'Tabla de Queso', 'Tabla con variedad de quesos', 'tabla_queso.webp', 'unidad', 1, 0),
    (3, 'Tabla Veggie', 'Tabla vegetariana con vegetales y quesos', 'tabla_veggie.webp', 'unidad', 1, 0),
    (3, 'Papas Rústicas', 'Papas fritas rústicas', 'papas_rusticas.webp', 'unidad', 1, 0),
    (3, 'Papas Merken', 'Papas fritas con merken', 'papas_merken.webp', 'unidad', 1, 0),
    (3, 'Papas Cheddar', 'Papas fritas con queso cheddar', 'papas_cheddar.webp', 'unidad', 1, 0);

INSERT INTO products 
    (group_id, name, description, img, base_unit, sale_unit, stock)
VALUES
    (4, 'Hamburguesa de Res', 'Hamburguesa clásica de carne de res', 'hamburguesa_res.webp', 'unidad', 1, 0),
    (4, 'Hamburguesa Pollo Apanado', 'Hamburguesa de pollo apanado', 'hamburguesa_apanado.webp', 'unidad', 1, 0),
    (4, 'Hamburguesa Doble Cheddar', 'Hamburguesa doble con queso cheddar', 'hamburguesa_cheddar.webp', 'unidad', 1, 0),
    (4, 'Hamburguesa Mechada', 'Hamburguesa con carne mechada', 'hamburguesa_mechada.webp', 'unidad', 1, 0),
    (4, 'Hamburguesa Veggie', 'Hamburguesa vegetariana', 'hamburguesa_veggie.webp', 'unidad', 1, 0),
    (4, 'Hamburguesa Veggie Legumbres', 'Hamburguesa de legumbres', 'hamburguesa_veggie_legumbres.webp', 'unidad', 1, 0);

INSERT INTO products 
	(group_id, name, description, img, base_unit, sale_unit, stock)
VALUES
    (5, 'Completo Mexicano', 'Completo con ingredientes mexicanos', 'completo_mexicano.webp', 'unidad', 1, 0),
    (5, 'Completo Tocino', 'Completo con tocino crujiente', 'completo_tocino.webp', 'unidad', 1, 0),
    (5, 'Completo Italiano', 'Completo clásico italiano', 'completo_italiano.webp', 'unidad', 1, 0),
    (5, 'Completo Alemán', 'Completo estilo alemán', 'completo_aleman.webp', 'unidad', 1, 0);

-- Stored Procedure ---------------------------------------------
-- --------------------------------------------------------------

-- Query --------------------------------------------------------
-- --------------------------------------------------------------

SELECT * FROM categories;
SELECT * FROM groups;
SELECT * FROM products;
SELECT * FROM stock_movements;

-- --------------------------------------------------------------
-- --------------------------------------------------------------


