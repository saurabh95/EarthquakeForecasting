clc;
clear all;

fileID = fopen('agartalax.txt','r');
x= fscanf(fileID,'%f %f\n',[1,Inf]);
x=x';
fclose(fileID);

fileID = fopen('agartalay.txt','r');
y= fscanf(fileID,'%f %f\n',[1,Inf]);
y=y';
fclose(fileID);

for i=1:8  
    for j=1:2000
        tx(j)=x((2000*(i-1))+j);
        ty(j)=y((2000*(i-1))+j);
    end
    figure,plot(tx,ty);
end