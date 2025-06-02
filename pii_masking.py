import re

def mask_pii(email_body):
    # Define regex patterns for PII
    patterns = {
        "full_name": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",  # Simple name pattern
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "phone_number": r"\b\d{10}\b",  # 10 digit phone number
        "dob": r"\b\d{2}/\d{2}/\d{4}\b",  # Date of birth format
        "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",  # Aadhar number format
        "credit_debit_no": r"\b\d{16}\b",  # 16 digit card number
        "cvv_no": r"\b\d{3}\b",  # 3 digit CVV
        "expiry_no": r"\b\d{2}/\d{2}\b"  # Expiry date format
    }

    masked_email = email_body
    masked_entities = []

    for entity, pattern in patterns.items():
        for match in re.finditer(pattern, email_body):
            masked_entities.append({
                "position": [match.start(), match.end()],
                "classification": entity,
                "entity": match.group()
            })
            masked_email = masked_email.replace(match.group(), f"[{entity}]")

    return masked_email, masked_entities
