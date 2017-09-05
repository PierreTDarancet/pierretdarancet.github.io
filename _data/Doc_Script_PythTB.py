from pythtb import *
alat=6.1756941056860493
lat=[[1.0*alat,0.0,0.0],[0.0, 1.0*alat,0.0],[0.0,0,30.8784705284302454]]


orb=[[0.00000000,0.00000000,0.19882748],[-0.00000000,0.00000000,0.40117252],[-0.00000000,0.50000000,0.09539268],[0.00000000,0.50000000,0.30000000],[0.00000000,0.50000000,0.50460732],[0.50000000,-0.00000000,0.09539268],[0.50000000,-0.00000000,0.30000000],[0.50000000,0.00000000,0.50460732],[0.50000000,0.50000000,0.19882748],[0.50000000,0.50000000,0.40117252],[0.25000000,0.25000000,0.24926945],[0.25000000,0.25000000,0.45232231],[0.75000000,0.75000000,0.24926945],[0.75000000,0.75000000,0.45232231],[0.75000000,0.25000000,0.14767769],[0.75000000,0.25000000,0.35073055],[0.25000000,0.75000000,0.14767769],[0.25000000,0.75000000,0.35073055],[0.50000000,-0.00000000,0.04033715],[-0.00000000,0.50000000,0.04033715],[0.50000000,0.00000000,0.55966285],[-0.00000000,0.50000000,0.55966285]]

# set model parameters

EsCd=4.3707
EsSe=-9.0819
EsH=0.0
sssigma=-1.3225
sCdsSe=sssigma
sCdsH=0.1
sHsCd=0.1
sSesCd=sssigma
# only first two lattice vectors repeat, so k-space is 2D
my_model=tb_model(2,3,lat,orb)
my_model.set_onsite( [EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsSe,EsSe,EsSe,EsSe,EsSe,EsSe,EsSe,EsSe,EsH,EsH,EsH,EsH] )


my_model.set_hop(sCdsSe,0 ,10 ,[0,0,0] )
my_model.set_hop(sCdsSe,0 ,12 ,[1,1,0] )
my_model.set_hop(sCdsSe,0 ,14 ,[1,0,0] )
my_model.set_hop(sCdsSe,0 ,16 ,[0,1,0] )



(fig,ax)=my_model.visualize(0,1)
fig.tight_layout()
fig.savefig("visualize_bulkxy.pdf")
(fig,ax)=my_model.visualize(0,2)
fig.tight_layout()
fig.savefig("visualize_bulkxz.pdf")
(fig,ax)=my_model.visualize(1,2)
fig.savefig("visualize_bulkyz.pdf")




from pythtb import *
alat=6.1756941056860493
lat=[[1.0*alat,0.0,0.0],[0.0, 1.0*alat,0.0],[0.0,0,30.8784705284302454]]
#lat=[[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0,30.8784705284302454]]


#head -31 POSCAR | tail -n 22 | awk '{printf "\[%4.8f,%4.8f,%4.8f\],\n", $1,$2,$3  }'

# all s orbitals
orb=[[0.00000000,0.00000000,0.19882748],[-0.00000000,0.00000000,0.40117252],[-0.00000000,0.50000000,0.09539268],[0.00000000,0.50000000,0.30000000],[0.00000000,0.50000000,0.50460732],[0.50000000,-0.00000000,0.09539268],[0.50000000,-0.00000000,0.30000000],[0.50000000,0.00000000,0.50460732],[0.50000000,0.50000000,0.19882748],[0.50000000,0.50000000,0.40117252],[0.25000000,0.25000000,0.24926945],[0.25000000,0.25000000,0.45232231],[0.75000000,0.75000000,0.24926945],[0.75000000,0.75000000,0.45232231],[0.75000000,0.25000000,0.14767769],[0.75000000,0.25000000,0.35073055],[0.25000000,0.75000000,0.14767769],[0.25000000,0.75000000,0.35073055],[0.50000000,-0.00000000,0.04033715],[-0.00000000,0.50000000,0.04033715],[0.50000000,0.00000000,0.55966285],[-0.00000000,0.50000000,0.55966285]]
# set model parameters
EsCd=4.3707
EsSe=-9.0819
EsH=0.0
sssigma=-1.3225
sCdsSe=sssigma
sCdsH=0.1
sHsCd=0.1
sSesCd=sssigma
# only first two lattice vectors repeat, so k-space is 2D
my_model=tb_model(2,3,lat,orb)
my_model.set_onsite( [EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsCd,EsSe,EsSe,EsSe,EsSe,EsSe,EsSe,EsSe,EsSe,EsH,EsH,EsH,EsH] )

# set hoppings (one for each connected pair of orbitals)
# (amplitude, i, j, [lattice vector to cell containing j])
#~/src/ScriptsPython/symmetry/periodica.py supa='2 0 0 0 2 0 0 0 1' -dist cut=3.5 POSCAR.tmp |grep - | sed 's/ //g' | cut -d '|' -f 1  | sed 's/---/ /g' | sed 's/H/sH  /g' | sed 's/Cd/sCd /g' | sed 's/Se/sSe /g' | awk '{printf "%4.1f\t%4.1f\t%s-%s\n",($2-1.0)/4.0, ($4-1.0)/4.0, $1, $3}' | sed "s/\.0/ \[0,0,0\]/g" | sed "s/\.5/ \[1,0,0\]/g" | sed "s/\.2/ \[0,1,0\]/g" | sed "s/\.8/ \[1,1,0\]/g" | grep "\[0,0,0\]" | awk '{print $2,$1,$3,$4,$5}' | grep -e "^\[0,0" | awk '{printf "my_model.set_hop\(%s,%s ,%s ,%s )\n", $5,$2,$3,$4}' | sed 's/-//g'
my_model.set_hop(sCdsSe,0 ,10 ,[0,0,0] )
my_model.set_hop(sCdsSe,0 ,12 ,[1,1,0] )
my_model.set_hop(sCdsSe,0 ,14 ,[1,0,0] )
my_model.set_hop(sCdsSe,0 ,16 ,[0,1,0] )
my_model.set_hop(sCdsSe,1 ,15 ,[1,0,0] )
my_model.set_hop(sCdsSe,1 ,17 ,[0,1,0] )
my_model.set_hop(sCdsSe,1 ,11 ,[0,0,0] )
my_model.set_hop(sCdsSe,1 ,13 ,[1,1,0] )
my_model.set_hop(sCdsH,2 ,19 ,[0,0,0] )
my_model.set_hop(sCdsSe,2 ,14 ,[1,0,0] )
my_model.set_hop(sCdsSe,2 ,16 ,[0,0,0] )
my_model.set_hop(sCdsSe,3 ,10 ,[0,0,0] )
my_model.set_hop(sCdsSe,3 ,12 ,[1,0,0] )
my_model.set_hop(sCdsSe,3 ,15 ,[1,0,0] )
my_model.set_hop(sCdsSe,3 ,17 ,[0,0,0] )
my_model.set_hop(sCdsH,4 ,21 ,[0,0,0] )
my_model.set_hop(sCdsSe,4 ,11 ,[0,0,0] )
my_model.set_hop(sCdsSe,4 ,13 ,[1,0,0] )
my_model.set_hop(sCdsH,5 ,18 ,[0,0,0] )
my_model.set_hop(sCdsSe,5 ,14 ,[0,0,0] )
my_model.set_hop(sCdsSe,5 ,16 ,[0,1,0] )
my_model.set_hop(sCdsSe,6 ,10 ,[0,0,0] )
my_model.set_hop(sCdsSe,6 ,12 ,[0,1,0] )
my_model.set_hop(sCdsSe,6 ,17 ,[0,1,0] )
my_model.set_hop(sCdsSe,6 ,15 ,[0,0,0] )
my_model.set_hop(sCdsH,7 ,20 ,[0,0,0] )
my_model.set_hop(sCdsSe,7 ,11 ,[0,0,0] )
my_model.set_hop(sCdsSe,7 ,13 ,[0,1,0] )
my_model.set_hop(sCdsSe,8 ,10 ,[0,0,0] )
my_model.set_hop(sCdsSe,8 ,12 ,[0,0,0] )
my_model.set_hop(sCdsSe,8 ,14 ,[0,0,0] )
my_model.set_hop(sCdsSe,8 ,16 ,[0,0,0] )
my_model.set_hop(sCdsSe,9 ,15 ,[0,0,0] )
my_model.set_hop(sCdsSe,9 ,17 ,[0,0,0] )
my_model.set_hop(sCdsSe,9 ,11 ,[0,0,0] )
my_model.set_hop(sCdsSe,9 ,13 ,[0,0,0] )
my_model.set_hop(sSesCd,10 ,0 ,[0,0,0] )
my_model.set_hop(sSesCd,10 ,8 ,[0,0,0] )
my_model.set_hop(sSesCd,10 ,3 ,[0,0,0] )
my_model.set_hop(sSesCd,10 ,6 ,[0,0,0] )
my_model.set_hop(sSesCd,11 ,9 ,[0,0,0] )
my_model.set_hop(sSesCd,11 ,1 ,[0,0,0] )
my_model.set_hop(sSesCd,11 ,4 ,[0,0,0] )
my_model.set_hop(sSesCd,11 ,7 ,[0,0,0] )
my_model.set_hop(sSesCd,12 ,0 ,[1,1,0] )
my_model.set_hop(sSesCd,12 ,8 ,[0,0,0] )
my_model.set_hop(sSesCd,12 ,3 ,[1,0,0] )
my_model.set_hop(sSesCd,12 ,6 ,[0,1,0] )
my_model.set_hop(sSesCd,13 ,1 ,[1,1,0] )
my_model.set_hop(sSesCd,13 ,9 ,[0,0,0] )
my_model.set_hop(sSesCd,13 ,4 ,[1,0,0] )
my_model.set_hop(sSesCd,13 ,7 ,[0,1,0] )
my_model.set_hop(sSesCd,14 ,0 ,[1,0,0] )
my_model.set_hop(sSesCd,14 ,8 ,[0,0,0] )
my_model.set_hop(sSesCd,14 ,2 ,[1,0,0] )
my_model.set_hop(sSesCd,14 ,5 ,[0,0,0] )
my_model.set_hop(sSesCd,15 ,1 ,[1,0,0] )
my_model.set_hop(sSesCd,15 ,9 ,[0,0,0] )
my_model.set_hop(sSesCd,15 ,3 ,[1,0,0] )
my_model.set_hop(sSesCd,15 ,6 ,[0,0,0] )
my_model.set_hop(sSesCd,16 ,0 ,[0,1,0] )
my_model.set_hop(sSesCd,16 ,8 ,[0,0,0] )
my_model.set_hop(sSesCd,16 ,5 ,[0,1,0] )
my_model.set_hop(sSesCd,16 ,2 ,[0,0,0] )
my_model.set_hop(sSesCd,17 ,1 ,[0,1,0] )
my_model.set_hop(sSesCd,17 ,9 ,[0,0,0] )
my_model.set_hop(sSesCd,17 ,6 ,[0,1,0] )
my_model.set_hop(sSesCd,17 ,3 ,[0,0,0] )
my_model.set_hop(sHsCd,18 ,5 ,[0,0,0] )
my_model.set_hop(sHsCd,19 ,2 ,[0,0,0] )
my_model.set_hop(sHsCd,20 ,7 ,[0,0,0] )
my_model.set_hop(sHsCd,21 ,4 ,[0,0,0] )





(fig,ax)=my_model.visualize(0,1)
fig.tight_layout()
fig.savefig("visualize_bulkxy.pdf")
(fig,ax)=my_model.visualize(0,2)
fig.tight_layout()
fig.savefig("visualize_bulkxz.pdf")
(fig,ax)=my_model.visualize(1,2)
fig.savefig("visualize_bulkyz.pdf")

#~/src/ScriptsPython/symmetry/periodica.py supa='2 0 0 0 1 0 0 0 1' -dist cut=3.5 POSCAR.tmp |grep - | sed 's/ //g' | cut -d '|' -f 1  | sed 's/---/ /g' | sed 's/H/H  /g' | sed 's/Cd/Cd /g' | sed 's/Se/Se /g' | awk '{printf "%4.1f\t%4.1f\t%s-%s\n",($2-1.0)/2.0, ($4-1.0)/2.0, $1, $3}' | sed "s/\.0/ \[0 0 0\]/g" | sed "s/\.5/ \[1 0 0\]/g" | grep "\[0 0 0\]" | grep "\[1 0 0\]"
#~/src/ScriptsPython/symmetry/periodica.py -dist cut=3.5 POSCAR | grep -v 1.7 | grep T | sed 's/T//g' | sed 's/---/g'| awk '{printf "my_model.set_hop(sssigma,%i,%i,\[ 0, 0\])\n "  , $1-1,$2-1}'
# ~/src/ScriptsPython/symmetry/periodica.py supa='1 0 0 0 2 0 0 0 1' -dist cut=3.5 POSCAR.tmp |grep - | sed 's/ //g' | cut -d '|' -f 1  | sed 's/---/ /g' | sed 's/H/H  /g' | sed 's/Cd/Cd /g' | sed 's/Se/Se /g' | awk '{printf "%4.1f\t%4.1f\t%s-%s\n",($2-1.0)/2.0, ($4-1.0)/2.0, $1, $3}' | sed "s/\.0/ \[0 0 0\]/g" | sed "s/\.5/ \[0 1 0\]/g" | grep "\[0 0 0\]" | grep "\[0 1 0\]"
#~/src/ScriptsPython/symmetry/periodica.py supa='1 0 0 0 2 0 0 0 1' -dist cut=3.5 POSCAR.tmp |grep - | sed 's/ //g' | cut -d '|' -f 1  | sed 's/---/ /g' | sed 's/H/H  /g' | sed 's/Cd/Cd /g' | sed 's/Se/Se /g' | awk '{printf "%4.1f\t%4.1f\t%s-%s\n",($2-1.0)/2.0, ($4-1.0)/2.0, $1, $3}' | sed "s/\.0/ \[0 0 0\]/g" | sed "s/\.5/ \[0 1 0\]/g" | grep "\[0 0 0\]" | grep "\[0 1 0\]"

# visualize infinite model