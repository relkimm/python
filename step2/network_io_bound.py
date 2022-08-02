import requests


def network_io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__ == "__main__":
    for i in range(10):
        result = network_io_bound_func()
    print(result)
