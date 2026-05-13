-- Ejercicio 2: Transacción de Compra
-- Construya una transacción para el proceso de compra de múltiples productos. El bloque debe realizar las siguientes validaciones y acciones:
-- Comprobar si hay existencias suficientes de cada uno de los productos dentro de la factura.
-- Confirmar que el usuario que realiza la compra existe en la DB.
-- Insertar la factura con el usuario relacionado.
-- Reducir el stock de los productos según la cantidad comprada.


DO $$
DECLARE
    v_bill_id   VARCHAR(50)    := 'B001';
    v_user_id   VARCHAR(50)    := 'U001';

    v_user_count  INTEGER;
    v_total       DECIMAL(10,2) := 0;

    v_p1_id    VARCHAR(50)   := 'P001';
    v_p1_qty   INTEGER       := 2;
    v_p1_price DECIMAL(10,2);
    v_p1_stock INTEGER;

    v_p2_id    VARCHAR(50)   := 'P002';
    v_p2_qty   INTEGER       := 3;
    v_p2_price DECIMAL(10,2);
    v_p2_stock INTEGER;

BEGIN
-- 1. Verificar que el usuario existe y está activo
    SELECT COUNT(*) INTO v_user_count
    FROM users
    WHERE user_id = v_user_id AND status = 'active';

    IF v_user_count = 0 THEN
        RAISE EXCEPTION 'El usuario % no existe o no está activo.', v_user_id;
    END IF;

    RAISE NOTICE 'Usuario % validado correctamente.', v_user_id;

-- 2. Comprobar existencias del Producto 1
    SELECT stock, price INTO v_p1_stock, v_p1_price
    FROM products
    WHERE product_id = v_p1_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Producto % no encontrado.', v_p1_id;
    END IF;

    IF v_p1_stock < v_p1_qty THEN
        RAISE EXCEPTION
            'Stock insuficiente para %. Disponible: %, Solicitado: %.',
            v_p1_id, v_p1_stock, v_p1_qty;
    END IF;

    RAISE NOTICE 'Stock de % OK. Disponible: %.', v_p1_id, v_p1_stock;

-- 3. Comprobar existencias del Producto 2
    SELECT stock, price INTO v_p2_stock, v_p2_price
    FROM products
    WHERE product_id = v_p2_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Producto % no encontrado.', v_p2_id;
    END IF;

    IF v_p2_stock < v_p2_qty THEN
        RAISE EXCEPTION
            'Stock insuficiente para %. Disponible: %, Solicitado: %.',
            v_p2_id, v_p2_stock, v_p2_qty;
    END IF;

    RAISE NOTICE 'Stock de % OK. Disponible: %.', v_p2_id, v_p2_stock;

-- 4. Calcular total
    v_total := (v_p1_price * v_p1_qty) + (v_p2_price * v_p2_qty);

-- 5. Insertar la factura
    INSERT INTO bills (bill_id, user_id, total, status)
    VALUES (v_bill_id, v_user_id, v_total, 'active');

    RAISE NOTICE 'Factura % creada. Total: $%.', v_bill_id, v_total;

-- 6. Insertar ítems (tabla cruzada)
    INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
    VALUES (v_bill_id, v_p1_id, v_p1_qty, v_p1_price);

    INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
    VALUES (v_bill_id, v_p2_id, v_p2_qty, v_p2_price);

-- 7. Reducir stock
    UPDATE products
    SET stock = stock - v_p1_qty
    WHERE product_id = v_p1_id;

    UPDATE products
    SET stock = stock - v_p2_qty
    WHERE product_id = v_p2_id;

    RAISE NOTICE 'Stock actualizado para % y %.', v_p1_id, v_p2_id;
    RAISE NOTICE 'Transacción de compra completada .';

END $$;