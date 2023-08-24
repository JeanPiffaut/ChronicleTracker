from datetime import datetime

positive_test_cases = [
    (1, "Valid Description", datetime(2023, 8, 22), True),
    (2, "Another Valid Description", datetime(2023, 8, 23), True),
    (3, "Short Desc", datetime(2023, 8, 24), True),
    (4, "Long Description" * 20, datetime(2023, 8, 25), False),
    (5, "Valid Description", datetime(2023, 8, 26), True),
    (18, "Valid Description", '2023-08-26', True),
]

negative_test_cases = [
    (6, None, datetime(2023, 8, 27), False),  # Null description
    (7, "Valid Description", None, True),     # Null date
    (8, "", datetime(2023, 8, 28), False),     # Empty description
    (9, "Valid Description", datetime(2023, 8, 29), True),  # Extra long description
    (10, "Valid Description", datetime(2023, 8, 30), True), # Invalid date
]

sql_injection_test_cases = [
    (11, "SQL Injection: ' OR 1=1; --", datetime(2023, 9, 1), True),
    (12, "SQL Injection: DROP TABLE milestones;", datetime(2023, 9, 2), True),
]

length_error_test_cases = [
    (13, "A" * 256, datetime(2023, 9, 3), False),  # Exceeding max length for description
    (14, "Valid Description", datetime(2023, 9, 4), True),
]

null_field_test_cases = [
    (15, None, datetime(2023, 9, 5), False),  # Null description
    (16, "Valid Description", None, True),   # Null date
    (17, None, None, False),                  # Null description and date
]

test_params = (
    *positive_test_cases,
    *negative_test_cases,
    *sql_injection_test_cases,
    *length_error_test_cases,
    *null_field_test_cases
)
