import model
import test_input as ti


def calculation(a, op, b):

    while True:
        if not ti.test_int(a):
            return("not correct input")
        if not ti.test_int(b):
            return("not correct input")

        # op = view.getNumb(f"input operation {model.op_cod}")

        if ti.test_int(a) and ti.test_int(b) and ti.test_operations(op, model.operations.keys()):
            break
        else:
            return("not correct input")

    model.init(a,b)

    result = model.operations[op]()

    return(result)