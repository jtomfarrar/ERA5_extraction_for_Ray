%  Read ERA5 specific humidity and wind files that were extracted by Tom for Ray's thesis
%
%
% Started: 6/4/2021, jtomfarrar, jfarrar@whoi.edu
%
% 
% 


clear

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Parameters to change:
%var_name='u_component';
%var_name='v_component';
var_name='humidity';

%Try new way using *\* with dir:
dir_str=['C:\Users\jtomf\Documents\Python\ERA5_extraction_for_Ray\data\raw\*' var_name '*.nc'];

files=dir(dir_str)

%Load and plot 1 file for geographic selection:
n=2;
ncdisp([files(n).folder '\' files(n).name])

lat=ncread([files(n).folder '\' files(n).name],'latitude');
lon=ncread([files(n).folder '\' files(n).name],'longitude');
level=ncread([files(n).folder '\' files(n).name],'level');
if strcmp(var_name,'u_component')
	u=ncread([files(n).folder '\' files(n).name],'u');
elseif strcmp(var_name,'v_component')
	v=ncread([files(n).folder '\' files(n).name],'v');
elseif strcmp(var_name,'humidity')
	q=ncread([files(n).folder '\' files(n).name],'q');
end
time=ncread([files(n).folder '\' files(n).name],'time');

%u is x,y,z,t
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

tic

%Initialize vectors larger that I expect to use:
% skip for now

master_ind=1;

for jj=1:length(files)
	if strcmp(var_name,'u_component')
		u_i=ncread([files(n).folder '\' files(n).name],'u');
	elseif strcmp(var_name,'v_component')
		v_i=ncread([files(n).folder '\' files(n).name],'v');
	elseif strcmp(var_name,'humidity')
		q_i=ncread([files(n).folder '\' files(n).name],'q');
	end

	
	time_i=ncread([files(n).folder '\' files(n).name],'time');
	if strcmp(var_name,'u_component')
		u(:,:,:,master_ind:master_ind+length(time_i)-1)=u_i;
	elseif strcmp(var_name,'v_component')
		v(:,:,:,master_ind:master_ind+length(time_i)-1)=v_i;
	elseif strcmp(var_name,'humidity')
		q(:,:,:,master_ind:master_ind+length(time_i)-1)=q_i;
	end
	time(master_ind:master_ind+length(time_i)-1)=time_i;
	master_ind=master_ind+length(time_i);%set 'master index' to value for next iteration
end%main loop

%convert time to matlab time
mday=datenum(1900,1,1,0,0,0)+time./24;

toc

%mission
comment=['Processed in ERA5_Ray_batch_read.m, ' datestr(now)];

if strcmp(var_name,'u_component')
	save(['C:\Users\jtomf\Documents\Python\ERA5_extraction_for_Ray\data\processed\ERA5_output_' var_name '_merged.mat'],'lat','lon','level','mday','u','comment')
elseif strcmp(var_name,'v_component')
	save(['C:\Users\jtomf\Documents\Python\ERA5_extraction_for_Ray\data\processed\ERA5_output_' var_name '_merged.mat'],'lat','lon','level','mday','v','comment')
elseif strcmp(var_name,'humidity')
	save(['C:\Users\jtomf\Documents\Python\ERA5_extraction_for_Ray\data\processed\ERA5_output_' var_name '_merged.mat'],'lat','lon','level','mday','q','comment')
end



