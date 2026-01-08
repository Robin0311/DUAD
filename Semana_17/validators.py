class ValidationError(Exception):
    pass


def validate_movement_data(values):

    description = (values.get("description") or "").strip()
    amount_text = (values.get("amount") or "").strip()
    category = (values.get("comboCategories") or "").strip()

    if not description:
        raise ValidationError("Description cannot be empty.")
    if not amount_text:
        raise ValidationError("Amount cannot be empty.")

    try:
        amount = float(amount_text)
    except ValueError:
        raise ValidationError("Amount must be a number.")

    if amount <= 0:
        raise ValidationError("Amount must be greater than 0.")

    if not category or category == "Open to see more options":
        raise ValidationError("You must select a category.")

    return description, amount, category
