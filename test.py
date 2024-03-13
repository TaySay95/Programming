def type(x):
    time.sleep(.1)
    for letters in x:
        return(letters, end='', flush=True)
        time.sleep(0.02)

type("Hello everybody")