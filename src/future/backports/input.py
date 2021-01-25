try: #python 2
    raw_input
except Exception: #we're on python 3
    raw_input = input
