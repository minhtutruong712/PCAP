import os

def find_abs_path(path, target_dir):
    matches = []

    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                # print(full_path)

                if item == target_dir:
                    matches.append(os.path.abspath(full_path))

                # Recursive search
                matches.extend(find_abs_path(full_path, target_dir))

    except PermissionError:
        pass

    return matches


result = find_abs_path('/Users/minhtutruong/Documents/Coding/pcap_test/miscellaneous/os_module', 'python')
print(*result, sep='\n')





        

