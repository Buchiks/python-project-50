from gendiff import cli, generate_diff, loading


def main():
    args = cli()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    data1, data2 = loading(path_to_file1, path_to_file2)
    print(generate_diff(data1, data2))
    

if __name__ == "__main__":
    main()
