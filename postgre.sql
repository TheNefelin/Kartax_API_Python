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
    parent_product_id INTEGER REFERENCES products(id),
    name VARCHAR(100) NOT NULL,
    description VARCHAR(256) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    img VARCHAR(100) NOT NULL,    
    is_fractional BOOLEAN DEFAULT FALSE,
    base_unit VARCHAR(20) NOT NULL,
    sale_unit NUMERIC DEFAULT NULL,
    stock NUMERIC DEFAULT 0,
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
    (group_id, name, description, price, img, is_fractional, base_unit, stock, is_enable)
VALUES
    (1, 'Pils (Barril 30L)', 'Cerveza artesanal rubia en barril de 30 litros', 270000, 'barril_pils.webp', TRUE, 'litros', 30, TRUE),
    (1, 'Santa Sed (Barril 30L)', 'Cerveza artesanal ámbar en barril de 30 litros', 270000, 'barril_santa_sed.webp', TRUE, 'litros', 30, TRUE),
    (1, 'Blood (Barril 30L)', 'Cerveza artesanal roja en barril de 30 litros', 270000, 'barril_blood.webp', TRUE, 'litros', 30, TRUE);

-- Pintas (0.5L), fraccionadas del barril
INSERT INTO products 
    (group_id, parent_product_id, name, description, price, img, base_unit, sale_unit, stock, is_enable)
VALUES
    (1, 1, 'Pinta de Pils', 'Pinta de 500ml de cerveza rubia artesanal', 4500, 'schop_pils.webp', 'litros', 0.5, 0, TRUE),
    (1, 2, 'Pinta de Santa Sed', 'Pinta de 500ml de cerveza ámbar artesanal', 4500, 'schop_santa_sed.webp', 'litros', 0.5, 0, TRUE),
    (1, 3, 'Pinta de Blood', 'Pinta de 500ml de cerveza roja artesanal', 4500, 'schop_blood.webp', 'litros', 0.5, 0, TRUE);

INSERT INTO products 
    (group_id, name, description, price, img, base_unit, sale_unit, stock, is_enable)
VALUES
    (2, 'Heineken', 'Cerveza envasada Heineken 330ml', 4000, 'heineken.webp', 'unidad', 1, 0, TRUE),
    (2, 'Kross', 'Cerveza envasada Kross 330ml', 4000, 'kross.webp', 'unidad', 1, 0, TRUE),
    (2, 'Kunstmann', 'Cerveza envasada Kunstmann 330ml', 4000, 'kunstmann.webp', 'unidad', 1, 0, TRUE),
    (2, 'Budweiser', 'Cerveza envasada Budweiser 330ml', 4000, 'budweiser.webp', 'unidad', 1, 0, TRUE),
    (2, 'Royal', 'Cerveza envasada Royal 330ml', 4000, 'royal.webp', 'unidad', 1, 0, TRUE),
    (3, 'Tabla de Carne', 'Tabla con variedad de carnes', 9000, 'tabla_carne.webp', 'unidad', 1, 0, TRUE),
    (3, 'Tabla de Queso', 'Tabla con variedad de quesos', 9000, 'tabla_queso.webp', 'unidad', 1, 0, TRUE),
    (3, 'Tabla Veggie', 'Tabla vegetariana con vegetales y quesos', 9000, 'tabla_veggie.webp', 'unidad', 1, 0, TRUE),
    (3, 'Papas Rústicas', 'Papas fritas rústicas', 7000, 'papas_rusticas.webp', 'unidad', 1, 0, TRUE),
    (3, 'Papas Merken', 'Papas fritas con merken', 7000, 'papas_merken.webp', 'unidad', 1, 0, TRUE),
    (3, 'Papas Cheddar', 'Papas fritas con queso cheddar', 9000, 'papas_cheddar.webp', 'unidad', 1, 0, TRUE),
    (4, 'Hamburguesa de Res', 'Hamburguesa clásica de carne de res', 7000, 'hamburguesa_res.webp', 'unidad', 1, 0, TRUE),
    (4, 'Hamburguesa Pollo Apanado', 'Hamburguesa de pollo apanado', 7000, 'hamburguesa_apanado.webp', 'unidad', 1, 0, TRUE),
    (4, 'Hamburguesa Doble Cheddar', 'Hamburguesa doble con queso cheddar', 7000, 'hamburguesa_cheddar.webp', 'unidad', 1, 0, TRUE),
    (4, 'Hamburguesa Mechada', 'Hamburguesa con carne mechada', 7000, 'hamburguesa_mechada.webp', 'unidad', 1, 0, TRUE),
    (4, 'Hamburguesa Veggie', 'Hamburguesa vegetariana', 7000, 'hamburguesa_veggie.webp', 'unidad', 1, 0, TRUE),
    (4, 'Hamburguesa Veggie Legumbres', 'Hamburguesa de legumbres', 7000, 'hamburguesa_veggie_legumbres.webp', 'unidad', 1, 0, TRUE),
    (5, 'Completo Mexicano', 'Completo con ingredientes mexicanos', 3000, 'completo_mexicano.webp', 'unidad', 1, 0, TRUE),
    (5, 'Completo Tocino', 'Completo con tocino crujiente', 3000, 'completo_tocino.webp', 'unidad', 1, 0, TRUE),
    (5, 'Completo Italiano', 'Completo clásico italiano', 3000, 'completo_italiano.webp', 'unidad', 1, 0, TRUE),
    (5, 'Completo Alemán', 'Completo estilo alemán', 3000, 'completo_aleman.webp', 'unidad', 1, 0, TRUE);

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
