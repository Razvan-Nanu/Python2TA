


import App


def print_app2():
    name = (__name__)
    return name



if __name__ == "__main__":
    # the following is calling code from this script
    print("I a running code from {}".format(print_app2()))

     # the following is calling code from the imported App,py
    print("I a running code from {}".format(App.print_app()))
