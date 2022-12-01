def RNA_to_protein(RNA):
    pass


with open('.txt', 'r') as f:
    RNA = f.read().strip()

ans = RNA_to_protein(RNA)   
print(ans)