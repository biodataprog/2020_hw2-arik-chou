with open('Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3', 'r') as fh:
    lines = fh.readlines()
    count = 0
    total=0
    exon = 0
    for x in lines:
        if '\tgene\t' in x:
            line=list(x.split("\t"))
            count +=1
        if '\tgene\t' in x:
            exon=int(line[4])-int(line[3])
        else:
            continue
        total = total + exon
    print "Total genes:", count
    print "Length of all exons:", total
with open('Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa', 'r') as fa:
    lineseq = fa.readlines()
    seqlen = 0
    genome = 0
    for seq in lineseq:
        if '>' in seq:
            continue
        else:
            seqlen = len(seq)
        genome = genome + seqlen
        
print "Coding percentage:", ((float(total)/float(genome)) * 100), '%'