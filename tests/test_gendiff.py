from pathlib import Path
from gendiff import generate_diff, loading


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff():
    file1 = str(get_test_data_path("file1.json"))
    file2 = str(get_test_data_path("file2.json"))
    data1, data2 = loading(file1, file2)
    expected = read_file("result_plain.txt")
    actual = generate_diff(data1, data2)
    assert actual == expected
