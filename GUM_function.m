function [ v2 ] = GUM_function( x1 )
x1=im2double(x1);
[ m, n, k ] = size( x1 );
x = x1;%
mask = ( 1 / 25 ) * ones( 5, 5 );%
y1 = conv2( x, double( mask ), 'same' );%
d = x - y1;%
g = 3 .* d;%
v1 = y1 + g;%
y2 = medfilt2( x, [ 3, 3 ] );%
%disp(y2(3,3))
max_1 = max( x, 0.01 );%
%disp(max_1(666,666));
X = ( 1 - x ) ./ max_1;%
%disp(X(3,3))
Y = ( 1 - y2 ) ./ max( y2, 0.01 );%
%disp(Y(4,3))
I = ones( m, n );%
d1 = I ./ ( 1 + ( X ./ Y ) );%
%disp(d1(3,3))
h = adapthisteq( y2, 'clipLimit', 0.005 );%
%disp(h(3,3))
c = ( 2 .* d1 ) - 1;
Gmax = 5;Gmin = 1;eta = 0.5;
beta = ( Gmax - Gmin ) / ( 1 - exp(  - 1 ) );
alpha = ( Gmax - beta );
%disp(alpha)
%disp(beta)
gama = alpha + ( beta * exp(  - 1 .* abs( c ) .^ eta ) );%
disp(gama(3,3))
D = ( 1 - d1 ) ./ max( d1, 0.01 );
g = I ./ ( 1 + D .^ gama );
G = ( 1 - g ) ./ max( g, 0.01 );
H = ( 1 - h ) ./ max( h, 0.01 );
v2 = I ./ max( 0.1, ( 1 + ( H .* G ) ) );
t = v2 > 1;
v2( t ) = x( t );
end
