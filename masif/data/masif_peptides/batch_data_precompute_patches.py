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


def precompute_patches(p_ids):
    for p_id in p_ids:
        if not os.path.exists(f"/job/save/computation_12A/precomputation/{p_id}") or not os.path.exists(
                f"/job/save/04a-precomputation_9A/precomputation/{p_id}"):
            os.system(f"./data_precompute_patches_one.sh {p_id}")
        else:
            print(p_id, "exists!")


finished_list = os.listdir("data_preparation/01-benchmark_surfaces")
peptide_ids = [p.split('.')[0] for p in finished_list]

#
# with open("lists/all_peptides.txt", 'r') as peptide_file:
#     peptide_ids = [pid.strip() for pid in peptide_file.readlines()]
# print(len(peptide_ids))

n_cpu = 8
pdb_id_groups = div_list(peptide_ids, n_cpu)
p = Pool(n_cpu)

for pig in pdb_id_groups:
    p.apply_async(precompute_patches, (pig,))
p.close()
p.join()

# precompute_patches(pdb_id_groups[0][:2])




