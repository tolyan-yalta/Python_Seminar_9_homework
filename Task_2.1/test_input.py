def test_int(a):
    try:
        return isinstance(float(a), float)
    except:
        return False

def test_operations(op, op_codes):
    return op in op_codes