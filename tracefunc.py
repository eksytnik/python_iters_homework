import sys

def tracefunc(frame, event, arg):
    if event == "return":
        print(f"function: {frame.f_code.co_name} , local vars: {list(frame.f_locals.keys())}")
    return tracefunc
