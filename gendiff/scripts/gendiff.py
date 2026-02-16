from gendiff import cli, generate_diff


def main():
    args = cli()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    print(generate_diff(path_to_file1, path_to_file2))


if __name__ == "__main__":
    main()
