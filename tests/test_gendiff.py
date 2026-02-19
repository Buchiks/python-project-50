from pathlib import Path
from gendiff import generate_diff, loading


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_loading():
    file1 = str(get_test_data_path("file1.json"))
    file2 = str(get_test_data_path("file2.json"))
    actual1, actual2 = loading(file1, file2)
    actual1 = str(actual1)
    actual2 = str(actual2)
    expected1 = read_file("file1_after_load.txt")
    expected2 = read_file("file2_after_load.txt")
    assert actual1 == expected1
    assert actual2 == expected2
    
    file1 = str(get_test_data_path("file1.yaml"))
    file2 = str(get_test_data_path("file2.yaml"))
    actual1, actual2 = loading(file1, file2)
    actual1 = str(actual1)
    actual2 = str(actual2)
    assert actual1 == expected1
    assert actual2 == expected2

    file1 = str(get_test_data_path("file1_hard.yml"))
    file2 = str(get_test_data_path("file2_hard.yml"))
    actual1, actual2 = loading(file1, file2)
    actual1 = str(actual1)
    actual2 = str(actual2)
    expected1 = read_file("file1_hard_after.txt")
    expected2 = read_file("file2_hard_after.txt")
    assert actual1 == expected1
    assert actual2 == expected2

    file1 = str(get_test_data_path("file1_hard.json"))
    file2 = str(get_test_data_path("file2_hard.json"))
    actual1, actual2 = loading(file1, file2)
    actual1 = str(actual1)
    actual2 = str(actual2)
    assert actual1 == expected1
    assert actual2 == expected2
    

def test_generate_diff():
    file1 = str(get_test_data_path("file1.json"))
    file2 = str(get_test_data_path("file2.json"))
    data1, data2 = loading(file1, file2)
    expected = read_file("result_plain.txt")
    actual = generate_diff(data1, data2)
    assert actual == expected


def test_generate_diff_hard():
    file1 = str(get_test_data_path("file1_hard.json"))
    file2 = str(get_test_data_path("file2_hard.json"))
    data1, data2 = loading(file1, file2)
    expected = read_file("result_hard.txt")
    actual = generate_diff(data1, data2)
    assert actual == expected
