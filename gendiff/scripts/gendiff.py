from gendiff import cli, loading, generate_diff


def main():
    args = cli()
    data1, data2 = loading(args)
    print(generate_diff(data1, data2))

if __name__ == "__main__":
    main()
