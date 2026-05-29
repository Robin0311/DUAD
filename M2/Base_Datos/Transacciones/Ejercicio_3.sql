-- Ejercicio 3: Transacción de Retorno de Productos
-- Construya una transacción para procesar la devolución de uno o varios productos. La transacción debe seguir este flujo:
-- Verificar que la factura existe en la base de datos.
-- Aumentar el stock de los productos en la cantidad que se registró en la compra.
-- Modificar la factura original para marcarla con el estado de "Retornada".

DO $$
DECLARE
    v_bill_id     VARCHAR(50) := 'B001';
    v_bill_status VARCHAR(20);
    v_product_id  VARCHAR(50);
    v_quantity    INTEGER;

    cur_items CURSOR FOR
        SELECT product_id, quantity
        FROM bill_items
        WHERE bill_id = v_bill_id;

BEGIN
    -- 1. Verificar que la factura existe (idiomático en PL/pgSQL)
    SELECT status INTO v_bill_status
    FROM bills
    WHERE bill_id = v_bill_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'La factura % no existe en la base de datos.', v_bill_id;
    END IF;

    RAISE NOTICE 'Factura % encontrada. Estado: %.', v_bill_id, v_bill_status;

    -- 2. Verificar que no fue retornada antes
    IF v_bill_status = 'returned' THEN
        RAISE EXCEPTION 'La factura % ya fue retornada anteriormente.', v_bill_id;
    END IF;

    -- 3. Recorrer ítems y restaurar stock
    OPEN cur_items;
    LOOP
        FETCH cur_items INTO v_product_id, v_quantity;
        EXIT WHEN NOT FOUND;

        UPDATE products
        SET stock = stock + v_quantity
        WHERE product_id = v_product_id;

        RAISE NOTICE 'Stock restaurado para %: +% unidades.',
            v_product_id, v_quantity;
    END LOOP;
    CLOSE cur_items;

    -- 4. Marcar factura como retornada
    UPDATE bills SET status = 'returned' WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Factura % marcada como "Retornada".', v_bill_id;
    RAISE NOTICE 'Retorno completado exitosamente.';

END $$;