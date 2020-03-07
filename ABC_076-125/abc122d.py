AAA = [1] * 101
AAC = [1] * 101
AAG = [1] * 101
AAT = [1] * 101
ACA = [1] * 101
ACC = [1] * 101
ACG = [0] * 101
ACT = [1] * 101
AGA = [1] * 101
AGC = [0] * 101
AGG = [1] * 101
AGT = [1] * 101
ATA = [1] * 101
ATC = [1] * 101
ATG = [1] * 101
ATT = [1] * 101
CAA = [1] * 101
CAC = [1] * 101
CAG = [1] * 101
CAT = [1] * 101
CCA = [1] * 101
CCC = [1] * 101
CCG = [1] * 101
CCT = [1] * 101
CGA = [1] * 101
CGC = [1] * 101
CGG = [1] * 101
CGT = [1] * 101
CTA = [1] * 101
CTC = [1] * 101
CTG = [1] * 101
CTT = [1] * 101
GAA = [1] * 101
GAC = [0] * 101
GAG = [1] * 101
GAT = [1] * 101
GCA = [1] * 101
GCC = [1] * 101
GCG = [1] * 101
GCT = [1] * 101
GGA = [1] * 101
GGC = [1] * 101
GGG = [1] * 101
GGT = [1] * 101
GTA = [1] * 101
GTC = [1] * 101
GTG = [1] * 101
GTT = [1] * 101
TAA = [1] * 101
TAC = [1] * 101
TAG = [1] * 101
TAT = [1] * 101
TCA = [1] * 101
TCC = [1] * 101
TCG = [1] * 101
TCT = [1] * 101
TGA = [1] * 101
TGC = [1] * 101
TGG = [1] * 101
TGT = [1] * 101
TTA = [1] * 101
TTC = [1] * 101
TTG = [1] * 101
TTT = [1] * 101


# AAA[4] は4文字で末尾がAAAの数
for i in range(4, 101):

	AAA[i] = AAA[i-1] + CAA[i-1] + GAA[i-1] + TAA[i-1]
	AAC[i] = AAA[i]
	AAG[i] = AAA[i]
	AAT[i] = AAA[i]
	ACA[i] = AAC[i-1] + CAC[i-1]  + TAC[i-1]
	ACC[i] = ACA[i]
	ACG[i] = 0
	ACT[i] = ACA[i]
	AGA[i] = AAG[i-1] + CAG[i-1] + GAG[i-1] + TAG[i-1]
	AGC[i] = 0
	AGG[i] = AGA[i]
	AGT[i] = AGA[i]
	ATA[i] = AAT[i-1] + CAT[i-1] + GAT[i-1] + TAT[i-1]
	ATC[i] = ATA[i]
	ATG[i] = ATA[i]
	ATT[i] = ATA[i]

	CAA[i] = ACA[i-1] + CCA[i-1] + GCA[i-1] + TCA[i-1]
	CAC[i] = CAA[i]
	CAG[i] = CAA[i]
	CAT[i] = CAA[i]
	CCA[i] = ACC[i-1] + CCC[i-1] + GCC[i-1] + TCC[i-1]
	CCC[i] = CCA[i]
	CCG[i] = CCA[i]
	CCT[i] = CCA[i]
	CGA[i] = 0 + CCG[i-1] + GCG[i-1] + TCG[i-1]
	CGC[i] = CGA[i]
	CGG[i] = CGA[i]
	CGT[i] = CGA[i]
	CTA[i] = ACT[i-1] + CCT[i-1] + GCT[i-1] + TCT[i-1]
	CTC[i] = CTA[i]
	CTG[i] = CTA[i]
	CTT[i] = CTA[i]

	GAA[i] = AGA[i-1] + CGA[i-1] + GGA[i-1] + TGA[i-1]
	GAC[i] = 0 # AGA[i-1] + CGA[i-1] + GGA[i-1] + TGA[i-1]
	GAG[i] = AGA[i-1] + CGA[i-1] + GGA[i-1] + TGA[i-1]
	GAT[i] = AGA[i-1] + CGA[i-1] + GGA[i-1] + TGA[i-1]
	GCA[i] = 0        + CGC[i-1] + GGC[i-1] + TGC[i-1]
	GCC[i] = 0        + CGC[i-1] + GGC[i-1] + TGC[i-1]
	GCG[i] = 0        + CGC[i-1] + GGC[i-1] + TGC[i-1]
	GCT[i] = 0        + CGC[i-1] + GGC[i-1] + TGC[i-1]
	GGA[i] = AGG[i-1] + CGG[i-1] + GGG[i-1] + TGG[i-1]
	GGC[i] = 0        + CGG[i-1] + GGG[i-1] + TGG[i-1]
	GGG[i] = AGG[i-1] + CGG[i-1] + GGG[i-1] + TGG[i-1]
	GGT[i] = AGG[i-1] + CGG[i-1] + GGG[i-1] + TGG[i-1]
	GTA[i] = AGT[i-1] + CGT[i-1] + GGT[i-1] + TGT[i-1]
	GTC[i] = 0        + CGT[i-1] + GGT[i-1] + TGT[i-1]
	GTG[i] = AGT[i-1] + CGT[i-1] + GGT[i-1] + TGT[i-1]
	GTT[i] = AGT[i-1] + CGT[i-1] + GGT[i-1] + TGT[i-1]

	TAA[i] = ATA[i-1] + CTA[i-1] + GTA[i-1] + TTA[i-1]
	TAC[i] = TAA[i]
	TAG[i] = TAA[i]
	TAT[i] = TAA[i]
	TCA[i] = ATC[i-1] + CTC[i-1] + GTC[i-1] +  TTC[i-1]
	TCC[i] = TCA[i]
	TCG[i] = TCA[i]
	TCT[i] = TCA[i]
	TGA[i] = ATG[i-1] + CTG[i-1] + GTG[i-1] + TTG[i-1]
	TGC[i] = 0        + CTG[i-1] + GTG[i-1] + TTG[i-1]
	TGG[i] = TGA[i]
	TGT[i] = TGA[i]
	TTA[i] = ATT[i-1] + CTT[i-1] + GTT[i-1] + TTT[i-1]
	TTC[i] = TTA[i]
	TTG[i] = TTA[i]
	TTT[i] = TTA[i]


n = int(input())
temp = 0 \
 + AAA[n] \
 + AAC[n] \
 + AAG[n] \
 + AAT[n] \
 + ACA[n] \
 + ACC[n] \
 + ACG[n] \
 + ACT[n] \
 + AGA[n] \
 + AGC[n] \
 + AGG[n] \
 + AGT[n] \
 + ATA[n] \
 + ATC[n] \
 + ATG[n] \
 + ATT[n] \
 + CAA[n] \
 + CAC[n] \
 + CAG[n] \
 + CAT[n] \
 + CCA[n] \
 + CCC[n] \
 + CCG[n] \
 + CCT[n] \
 + CGA[n] \
 + CGC[n] \
 + CGG[n] \
 + CGT[n] \
 + CTA[n] \
 + CTC[n] \
 + CTG[n] \
 + CTT[n] \
 + GAA[n] \
 + GAC[n] \
 + GAG[n] \
 + GAT[n] \
 + GCA[n] \
 + GCC[n] \
 + GCG[n] \
 + GCT[n] \
 + GGA[n] \
 + GGC[n] \
 + GGG[n] \
 + GGT[n] \
 + GTA[n] \
 + GTC[n] \
 + GTG[n] \
 + GTT[n] \
 + TAA[n] \
 + TAC[n] \
 + TAG[n] \
 + TAT[n] \
 + TCA[n] \
 + TCC[n] \
 + TCG[n] \
 + TCT[n] \
 + TGA[n] \
 + TGC[n] \
 + TGG[n] \
 + TGT[n] \
 + TTA[n] \
 + TTC[n] \
 + TTG[n] \
 + TTT[n]

print(temp % (1000000007))