def compare_version(version1, version2):
    version1 = list(map(int, version1.split('.')))
    version2 = list(map(int, version2.split('.')))
    if version1 < version2:
        return -1
    elif version1 > version2:
        return 1
    else:
        return 0


print(compare_version("0.1", "0.2"))
print(compare_version("0.2", "0.1"))
print(compare_version("4.2", "4.2"))
