pp = pprint.PrettyPrinter(indent = 2)
import subprocess
import sys
import os

def main():
    snp_dir_path = "./snp_in_each_gene/"
    filenames = subprocess.check_output(["ls" , "-1", "each_gene"]).decode().split()
    for each_filename in filenames:
        print(each_filename)
        chrom = each_filename.split("_")[0].replace("chr", "")
        start, end = each_filename.split("_")[1].split("-")
        end = end[:-2]
        gene_name = each_filename.split("_")[-1]
        print(each_filename.split("_"))
        print(f"🍌{sys.argv[0]}: processing {gene_name} at chromosome {chrom}, {start}-{end}", file = sys.stderr)
        print(f"🍌{sys.argv[0]}: mkdir -p {snp_dir_path + gene_name}", file = sys.stderr)
        subprocess.call(["mkdir", "-p", snp_dir_path + gene_name])
        vcftools_cmd_list = []
        vcftools_cmd_list.append("vcftools")
        vcftools_cmd_list.append("--gzvcf")
        vcftools_cmd_list.append("tommo-8.3kjpn-20200831-af_snvall-autosome_out.vcf")
        vcftools_cmd_list.append("--recode")
        vcftools_cmd_list.append("--out")
        vcftools_cmd_list.append(snp_dir_path + gene_name + "/" + gene_name)
        vcftools_cmd_list.append("--chr")
        vcftools_cmd_list.append(str(chrom))
        vcftools_cmd_list.append("--from-bp")
        vcftools_cmd_list.append(str(int(start) - 1000))
        vcftools_cmd_list.append("--to-bp")
        vcftools_cmd_list.append(str(int(end) + 1000))
        subprocess.call(vcftools_cmd_list)

        header_list = []
        record_list = []
        print(f"🍌{sys.argv[0]}: reading {snp_dir_path + gene_name + '/' + gene_name + '.recode.vcf'}", file = sys.stderr)
        with open(snp_dir_path + gene_name + '/' + gene_name + '.recode.vcf', "r") as f:
            for line in f:
                if line.strip().startswith("#"):
                    pass

                else:
                    CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO = line.split()
                    POS = int(POS) - int(start) - 999 #since vcf is 1 origin
                    record_list.append("\t".join([CHROM, str(POS), ID, REF, ALT, QUAL, FILTER, INFO]))
            
            head = "##contig=<ID=" + str(chrom) + ",length=" + str(int(end) + 1000 - int(start) + 1000 + 1) +">"
            header_list.append(head)

        print(f"🍌{sys.argv[0]}: writing {snp_dir_path + gene_name + '/' + gene_name + '.recode.shifted.vcf'}", file = sys.stderr)
        with open(snp_dir_path + gene_name + '/' + gene_name + '.recode.shifted.vcf', "w") as f:
            f.write('\n'.join(header_list))
            f.write('\n'.join(record_list))
        sys.exit()

if __name__ == "__main__":
    main()

