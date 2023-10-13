from log import timestamp

@timestamp
def hi():
    print('hi')

def main():
    hi()

if __name__ == "__main__":
    main()
