clc
clear
close all
%%
%%
%Read Data
id = 'P14.txt';

data=readtable(id); %read file replace id with new file
t = data{:,1}; %time
Lf = data{:,2}; %lidar front
Lr = data{:,3}; %lidar right
gyro = data{:,4}; %gyro
compassx = data{:,5}; %compass x
compassy = data{:,6}; %compass y
x = data{:,7};
y = data{:,8};
theta = data{:,9};

cx = compassy;
cy = compassx;
th = theta*-1+deg2rad(90);

A = [t Lf Lr gyro cx cy x y th];

fid = fopen('test.txt','wt');
for ii = 1:size(A,1)
    fprintf(fid,'%8.6f \t',A(ii,:));
    fprintf(fid,'\n');
end
fclose(fid);

%Fid = fopen('test.txt','w');
%fprintf(Fid, '%8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f \r\n',array);


