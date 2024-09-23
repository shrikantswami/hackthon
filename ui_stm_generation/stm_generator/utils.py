"""
This file is used for commonly used functions
"""


def handle_uploaded_file(file, location="some/file/name.txt"):
    """
    :param file: request file object
    :param location: "some/file/name.txt"
    :return:
    """
    with open(location, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
