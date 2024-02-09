from datetime import datetime

# Weryfikacja daty
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Weryfikacja kwoty
def is_float(value):
    try:    
        float_value = float(value)        
        return True  
    except ValueError:        
        return False
