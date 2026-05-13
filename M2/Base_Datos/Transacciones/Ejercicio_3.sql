-- Ejercicio 3: Transacción de Retorno de Productos
-- Construya una transacción para procesar la devolución de uno o varios productos. La transacción debe seguir este flujo:
-- Verificar que la factura existe en la base de datos.
-- Aumentar el stock de los productos en la cantidad que se registró en la compra.
-- Modificar la factura original para marcarla con el estado de "Retornada".


DO $$
DECLARE
    v_bill_id     VARCHAR(50) := 'B001'; -- Factura a retornar

    v_bill_status VARCHAR(20);
    v_bill_exists INTEGER;

    -- Variables para iterar sobre los ítems de la factura
    v_item_product_id VARCHAR(50);
    v_item_quantity   INTEGER;

    -- Cursor para recorrer los ítems de la factura
    cur_items CURSOR FOR
        SELECT product_id, quantity
        FROM bill_items
        WHERE bill_id = v_bill_id;

BEGIN
-- 1. Verificar que la factura existe en la base de datos
    SELECT COUNT(*), MAX(status)
    INTO v_bill_exists, v_bill_status
    FROM bills
    WHERE bill_id = v_bill_id;

    IF v_bill_exists = 0 THEN
        RAISE EXCEPTION 'La factura % no existe en la base de datos.', v_bill_id;
    END IF;

    RAISE NOTICE 'Factura % encontrada. Estado actual: %.', v_bill_id, v_bill_status;

    -- 2. Verificar que la factura no haya sido ya retornada
    IF v_bill_status = 'returned' THEN
        RAISE EXCEPTION 'La factura % ya fue retornada anteriormente.', v_bill_id;
    END IF;

-- 3. Recorrer cada ítem de la factura y restaurar el stock
    OPEN cur_items;

    LOOP
        FETCH cur_items INTO v_item_product_id, v_item_quantity;
        EXIT WHEN NOT FOUND;

        -- Aumentar el stock del producto en la cantidad que se compró
        UPDATE products
        SET stock = stock + v_item_quantity
        WHERE product_id = v_item_product_id;

        RAISE NOTICE 'Stock restaurado para producto %: +% unidades.',
            v_item_product_id, v_item_quantity;
    END LOOP;

    CLOSE cur_items;

-- 4. Marcar la factura original con el estado "Retornada"
    UPDATE bills
    SET status = 'returned'
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Factura % marcada como "Retornada".', v_bill_id;
    RAISE NOTICE 'Proceso de retorno completado exitosamente.';

END $$;