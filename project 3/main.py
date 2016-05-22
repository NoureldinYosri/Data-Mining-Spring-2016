import GPS,os,random
import scipy.cluster.hierarchy as HC
import matplotlib.pyplot as plt
import Queue

#global varialbes
Dist_Th = 50;
Time_Th = 60;
SmoothingP = 5;
U = []; UID = [];
Levels = []; LID = [];
TBHG = [];


def ReadInput(n,DT,TT,SP):
	print "Start Reading Input"
	def toString(n): return "0"*(3 - len(str(n))) + str(n);
	
	global U,UID;
	U = [GPS.Trajectory() for i in xrange(n)];
	UID = [[] for i in xrange(n)];
	
	for i in xrange(n):
		path = "/home/noureldin/Desktop/College/DataMining/GeolifeTrajectories1.3/Data/%s/Trajectory/";
		path = path%(toString(i));
		while True:		
			nP = path + random.choice(os.listdir(path))			
			try:
				U[i].ReadTrajectory(nP,i);
				U[i].Process(DT,TT,SP);
				break;		
			except Exception as e:
				print e;
				pass;
	print "End Reading Input"

def GetSP():
	print "Start GetSP";
	n = 0;	
	for u in U: n += len(u.StayPoints);
	SP = [GPS.GPS_Point() for i in xrange(n)];
	n = 0;
	for i in xrange(len(U)):
		UID[i] = [0 for j in xrange(len(U[i].StayPoints))]		
		for j in xrange(len(U[i].StayPoints)):
			SP[n] = U[i].StayPoints[j]; 
			UID[i][j] = n;
			n += 1;
	print "End SP";
	return SP;

def HierarchicalClustering(SP):
	print "Start HierarchicalClustering";
	n = len(SP); idx = 0; 
	print "number of Stay points = %d"%n;
	D = [0 for i in xrange(n*(n - 1)/2)];
	for i in xrange(n):
		for j in xrange(i + 1,n):
			D[idx] = SP[i].Haversine(SP[j]);
			idx += 1;
	
	Z = HC.linkage(D);
	HC.dendrogram(Z,100,'level');
	plt.show();	
	print "End HierarchicalClustering"
	return HC.to_tree(Z);


def DFS(H,d,n):
	global Levels
	if H is None : return [];
	if len(Levels) == d: Levels.append([]);
	ret = [];
	if H.get_id() < n: ret.append(H.get_id());
	for x in DFS(H.get_left(),d + 1,n): ret.append(x);	
	for x in DFS(H.get_right(),d + 1,n): ret.append(x);	
	Levels[d].append(ret);
	return ret;

def GetLevels(H,n):
	print "Start GetLevels"
	print "Start DFS";
	DFS(H,0,n);
	print "End DFS"
	for i in xrange(len(Levels)):
		U = set();
		for cluster in Levels[i]:
			for x in cluster:
				U.add(x);		
		for x in xrange(n):
			if x not in U:
				Levels[i].append([x]);
	#for u in UID: print u;	
	#for l in Levels: print l;
	print "End GetLevels"


def InitGraph():
	print "Start InitGraph"
	global TBHG,LID;
	LID = [[] for i in xrange(len(Levels))];
	n = 0;
	for i in xrange(len(Levels)): 
		LID[i] = [0 for j in xrange(len(Levels[i]))];
		for j in xrange(len(Levels[i])):
			LID[i][j] = n; n += 1;
	TBHG = [[] for i in xrange(n)];
	print "End InitGraph"

def addEdges(level,u):
	L = [set(l) for l in Levels[level]];
	p = 0;
	for i in xrange(len(UID[u])):
		x = UID[u][i];	
		if x not in L[p]:
			pre = p;
			for j in xrange(len(L)):
				if x in L[j]:
					p = j;
					break;
			if i: TBHG[LID[level][pre]].append(LID[level][p]);
	
def BuildGraph():
	print "Start BuildGraph"
	InitGraph();
	for i in xrange(len(Levels)):
		for j in xrange(len(UID)):
			addEdges(i,j);
	print "End BuildGraph"

def LocHisModeling():
	print "Start LocHisModeling";
	SP = GetSP();
	H = HierarchicalClustering(SP);
	GetLevels(H,len(SP));
	InitGraph();
	BuildGraph();
	print "End LocHisModeling";


if __name__ == "__main__":
	random.seed(0);
	ReadInput(180,Dist_Th,Time_Th,SmoothingP);
	LocHisModeling();
