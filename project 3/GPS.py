import math,copy;

class GPS_Point:
	Latitude = Longitude = Altitude = ArrivalTimeInMinutes = LeavingTimeInMinutes = None;
	EarthRadius = 6371000.0;
			
	def __init__(self,x):
		self.Latitude = x[0] * math.pi/180.0;
		self.Longitude = x[1] * math.pi/180.0;
		self.Altitude = x[3];
		self.ArrivalTimeInMinutes = self.LeavingTimeInMinutes = x[4]*24*60;
	
	def toString(self):
		return "(" + " ,".join([str(x) for x in [self.Latitude,self.Longitude,self.Altitude,self.ArrivalTimeInMinutes,self.LeavingTimeInMinutes]]) + ")";

	def Haversine(self,other):
		### return distance between self and other in meters ###
		def hav(x): return (1 - math.cos(x))/2.0;
		h = hav(self.Latitude - other.Latitude);
		h += math.cos(self.Latitude)*math.cos(other.Latitude)*hav(self.Longitude - other.Longitude);
		h = max(min(h,1.0),0.0);	
		return 2*self.EarthRadius*math.asin(math.sqrt(h));
		
	def toCartesian(self):
		x = -self.EarthRadius * math.cos(self.Latitude) * math.cos(self.Longitude)
		y =  self.EarthRadius * math.sin(self.Latitude) 
		z =  self.EarthRadius * math.cos(self.Latitude) * math.sin(self.Longitude)
		return [x,y,z];	

	def add(self,other):
		self.Latitude += other.Latitude;
		self.Longitude += other.Longitude;
		self.Altitude += other.Altitude;
	
	def normalize(self,n):	
		self.Latitude /= n;
		self.Longitude/= n;
		self.Altitude /= n;
						

class Trajectory:
	Path = None;
	StayPoints = None;
	Who = None;
	
	def __init__(self,X = []):
		self.Path = X;
	
	def ReadTrajectory(self,path_to_file,id):
		self.Who = id;
		f = file(path_to_file,"r");
		F = [line for line in f];
		self.Path = [GPS_Point(map(float,line.split(",")[:5])) for line in F[6:]];
		
	def Process(self,DistanceThreshold,TimeThreshold,SmoothingParamter):
		i,j,n = 0,0,len(self.Path);
		self.StayPoints = [];
		while i < n:
			StartTime = EndTime = self.Path[i].ArrivalTimeInMinutes;			
			while j < n and self.Path[j].Haversine(self.Path[i]) <= DistanceThreshold: 
				EndTime = self.Path[j].LeavingTimeInMinutes;
				j += 1;
			
			if EndTime - StartTime >= TimeThreshold :
				while i < j :				
					StayPoint = copy.deepcopy(self.Path[i]);
					i += 1; TmpCnt = 1;
					while i < j and TmpCnt < SmoothingParamter:					
						StayPoint.add(self.Path[i]);
						StayPoint.LeavingTimeInMinutes = self.Path[i].LeavingTimeInMinutes;
						i += 1;
						TmpCnt += 1;
					StayPoint.normalize(TmpCnt);
					self.StayPoints.append(StayPoint);
			i = j;
				
