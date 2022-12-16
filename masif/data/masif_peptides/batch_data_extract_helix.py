import os
from multiprocessing import Pool


def div_list(in_list, n):
    len_list = len(in_list)
    j = len_list // n

    ls_return = []
    for i in range(0, (n - 1) * j, j):
        ls_return.append(in_list[i:i + j])
    ls_return.append(in_list[(n - 1) * j:])
    return ls_return


def extract_helices(pdb_ids):
    for pdb_id in pdb_ids:
        os.system(f"./data_extract_helix_one.sh {pdb_id}")


with open("lists/bc-100-list.txt", 'r') as prot_chain_file:
    prot_chain_ids = [pid.strip() for pid in prot_chain_file.readlines()]
print(len(prot_chain_ids))

n_cpu = 8
pdb_id_groups = div_list(prot_chain_ids, n_cpu)
p = Pool(n_cpu)

for pig in pdb_id_groups:
    p.apply_async(extract_helices, (pig,))
p.close()
p.join()

# extract_helices(pdb_id_groups[0][:2])




