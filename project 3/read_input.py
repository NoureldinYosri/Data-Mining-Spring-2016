import GPS;

path = "/home/noureldin/Desktop/College/Data Mining/project 3/Geolife Trajectories 1.3/Data/000/Trajectory/20081023025304.plt";

Traj = GPS.Trajectory();
Traj.ReadTrajectory(path,0);
Traj.Process(15,1,7);

y = Traj.StayPoints[0];
for x in Traj.StayPoints:
	print y.Haversine(x);
	y = x;
