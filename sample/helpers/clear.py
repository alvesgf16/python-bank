from os import system, name


def clear_screen():
    _ = system("cls") if name == "nt" else system("clear")
