def read_single_key():
    try:
        import msvcrt
        key = msvcrt.getch()
        return key.decode("utf-8").lower()

    except ImportError:
        import sys
        import termios
        import tty

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
            return key.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)