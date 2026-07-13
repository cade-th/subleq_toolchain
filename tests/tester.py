import sys

def run(suite_name, test_data, test_func):
    success = True
    count = 0

    for name, data in test_data.items():
        count += 1  
        try:
            ok = test_func(name, data)
            if not ok:
                success = False
        except Exception as err:
            print(f"Error in test {name}: {err}")
            success = False
        
    if count == 0:
        print(f"{suite_name}: No tests found")
        return False

    if success:
        print(f"Test {suite_name} PASS")
    else:
        print(f"Test {suite_name} FAIL")
        sys.exit(1)

    return success
