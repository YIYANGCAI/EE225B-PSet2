%%
clc
clear
I=im2double(imread('Berkeley.jpg'));
V = I; % for trichromatic images, we study the hsv's v channel
[m,n]=size(I);
im1=V.^0.35;
%imshow(im1);figure;
%im2 gamma
a=50/255;
index=V<a;
index=double(index);
M=sum(index(:));
N=n*m;
gamma=(N-M)/N;
im2=1-(1-V).^gamma;
%disp(gamma)
%imshow(im2);figure;
%im3 GUM
im3=GUM_function(V);
%imshow(im3);figure;

%weight
sigma = 0.25;
aver = 0.3;
WE1= exp(-(im1 - aver).^2 / (2*sigma^2));
WE2=exp(-(im2 - aver).^2 / (2*sigma^2));
WE3=exp(-(im3 - aver).^2 / (2*sigma^2));
sumW=WE1+WE2+WE3;

% add a normalization part
W1=WE1./sumW;
W2=WE2./sumW;
W3=WE3./sumW;

% Multi-scale fusion
level=4;
G1=gaussian_pyramid(W1,level);
G2=gaussian_pyramid(W2,level);
G3=gaussian_pyramid(W3,level);
L1=laplacian_pyramid(im1,level);
L2=laplacian_pyramid(im2,level);
L3=laplacian_pyramid(im3,level);
for i=1:level
    F{i}=G1{i}.*L1{i}+G2{i}.*L2{i}+G3{i}.*L3{i};
end
Vfinal=pyramid_reconstruct(F);
% imshow(Vfinal);figure;
% hsv=cat(3,H,S,Vfinal);
% rgb=hsv2rgb(hsv);
imshow([I Vfinal]);
imwrite(Vfinal,'Berkeley_Output.jpg');