from assembler.src.preprocessor import preprocess
from test_utils import error_log

def preproc_test(test_name, data):
    # print(f"Test {test_name}:")
    success = False


    src_code = data["input"]
    
    out_p = preprocess(src_code)

    expected = data["output"]

    if out_p != expected:
        error_log(test_name, expected, out_p, "src code") 
        return success 
    
    success = True
    return success

