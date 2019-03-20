import sys


def tracefoo(function_to_trace, *args):
    """
    Tracing function, takes function to trace as an argument.
    Prints function name and local variables when the function is called.
    """

    def tracing(frame, event, *args):
        if function_to_trace.__name__ == frame.f_code.co_name and event == "return":
            print(f"function: {frame.f_code.co_name} , local vars: {list(frame.f_locals.keys())}")
        return tracing

    sys.settrace(tracing)
    function_to_trace(*args)
    sys.settrace(None)
