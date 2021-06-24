# -*- coding: utf-8 -*-

global_var = 'global'


def outer_func():
    outer_var = 10
    print(f"outer_var: {outer_var}")

    def inner_func():
        global global_var
        nonlocal outer_var
        print("========== Start Inner =========")
        print(f"global_var: {global_var}")
        global_var = 'global_changed'
        print(f"global_var: {global_var}")

        print(f"outer_var: {outer_var}")
        outer_var = 100
        print(f"outer_var: {outer_var}")
        print("========== End   Inner =========")

    inner_func()
    print(f"outer_var: {outer_var}")
    print(f"global_var: {global_var}")


if __name__ == "__main__":
    print(f"global_var: {global_var}")
    outer_func()
