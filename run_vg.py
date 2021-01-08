import subprocess
import sys
import os

def main():

    fasta_name_array = [fasta_name[:-3] for fasta_name in os.listdir("each_gene")]
    fasta_name_array.sort()
    vcf_name_array = [vcf_name[:-4] for vcf_name in os.listdir("shifted_vcf")]
    vcf_name_array.sort()

    print("Arrays are same :", fasta_name_array == vcf_name_array)

    subprocess.call(["mkdir", "vg_files"])
    subprocess.call(["cd", "vg_files"], shell=True)
    subprocess.call(["mkdir", "gfa_files"])
    subprocess.call(["mkdir", "sorted_gfa_files"])
    subprocess.call(["cd", ".."], shell=True)

    f = open("make_normed_vg.sh", "w")

    ff = open("make_normed_sorted_gfa.sh", "w")

    command = ""

    for gene_name in fasta_name_array:
        f.write("samtools faidx " + gene_name + ".fa\n" )
        f.flush()
        command_vg = "vg construct -r each_gene/" + gene_name + ".fa -v shifted_vcf/" + gene_name + ".vcf | vg mod -n - > vg_files/" + gene_name + ".norm.vg\n"
        f.write(command_vg)
        command_gfa = "vg view vg_files/" + gene_name + ".norm.vg > gfa_files/" + gene_name + ".norm.gfa\nvg view -Fv gfa_files/" + gene_name + ".norm.gfa | vg ids -s - | vg view - > sorted_gfa_files/" + gene_name + ".gfa\n"
        f.flush()
        ff.write(command_gfa)
        ff.flush()

        cmd = ""

    f.close()
    ff.close()

main()
