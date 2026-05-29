-- Ejercicio 2: Transacción de Compra
-- Construya una transacción para el proceso de compra de múltiples productos. El bloque debe realizar las siguientes validaciones y acciones:
-- Comprobar si hay existencias suficientes de cada uno de los productos dentro de la factura.
-- Confirmar que el usuario que realiza la compra existe en la DB.
-- Insertar la factura con el usuario relacionado.
-- Reducir el stock de los productos según la cantidad comprada.

-- =============================================================
-- Ejercicio 2: Transacción de Compra
-- Usa FOR LOOP + tabla temporal para manejar N productos
-- =============================================================

DO $$
DECLARE
    v_bill_id    VARCHAR(50)   := 'B001';
    v_user_id    VARCHAR(50)   := 'U001';
    v_total      DECIMAL(10,2) := 0;
    v_user_count INTEGER;
    v_product_id VARCHAR(50);
    v_qty        INTEGER;
    v_unit_price DECIMAL(10,2);
    v_stock      INTEGER;

BEGIN
    -- 1. Verificar que el usuario existe y está activo
    SELECT COUNT(*) INTO v_user_count
    FROM users
    WHERE user_id = v_user_id AND status = 'active';

    IF v_user_count = 0 THEN
        RAISE EXCEPTION 'El usuario % no existe o no está activo.', v_user_id;
    END IF;
    RAISE NOTICE 'Usuario % validado.', v_user_id;

    -- 2. Tabla temporal con el carrito (se elimina al finalizar la transacción)
    CREATE TEMP TABLE IF NOT EXISTS cart (
        product_id VARCHAR(50),
        quantity   INTEGER
    ) ON COMMIT DROP;

    INSERT INTO cart VALUES
        ('P001', 2),
        ('P002', 3),
        ('P003', 1);

    -- 3. Insertar la factura (total se actualiza al final)
    INSERT INTO bills (bill_id, user_id, total, status)
    VALUES (v_bill_id, v_user_id, 0, 'active');

    -- 4. FOR LOOP: valida stock, inserta ítem y reduce inventario por cada producto
    FOR v_product_id, v_qty IN SELECT product_id, quantity FROM cart LOOP

        SELECT stock, price INTO v_stock, v_unit_price
        FROM products
        WHERE product_id = v_product_id;

        IF NOT FOUND THEN
            RAISE EXCEPTION 'Producto % no encontrado.', v_product_id;
        END IF;

        IF v_stock < v_qty THEN
            RAISE EXCEPTION
                'Stock insuficiente para %. Disponible: %, Solicitado: %.',
                v_product_id, v_stock, v_qty;
        END IF;

        INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
        VALUES (v_bill_id, v_product_id, v_qty, v_unit_price);

        UPDATE products SET stock = stock - v_qty
        WHERE product_id = v_product_id;

        v_total := v_total + (v_unit_price * v_qty);
        RAISE NOTICE 'Producto % procesado. Stock restante: %.',
            v_product_id, v_stock - v_qty;

    END LOOP;

    -- 5. Actualizar el total real de la factura
    UPDATE bills SET total = v_total WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Factura % completada. Total: $%.', v_bill_id, v_total;
    RAISE NOTICE 'Transacción de compra completada exitosamente.';

END $$;