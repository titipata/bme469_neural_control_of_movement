%% data for problem #2a

clear
dat1 = [normrnd(6,2,100,1) normrnd(2,1,100,1)];   % create the input data
dat2 = [normrnd(2,3,100,1) normrnd(8,1,100,1)];
dat = [dat1; dat2];

y = [ones(100,1); -1*ones(100,1)];   % these are the labels for the classes

% plot the data
ind1 = find(y == 1);
ind2 = find(y == -1);
plot(dat(ind1,1),dat(ind1,2),'r.')
hold on
plot(dat(ind2,1),dat(ind2,2),'b.')
hold off

%% data for problem #2b

clear
dat1 = [normrnd(6,2,100,1) normrnd(2,2,100,1)];  % create the input data
dat2 = [normrnd(2,3,100,1) normrnd(8,2,100,1)];
dat = [dat1; dat2];

y = [ones(100,1); 0*ones(100,1)];  % labels for classes

% plot the data
ind1 = find(y == 1);
ind2 = find(y == 0);
plot(dat(ind1,1),dat(ind1,2),'r.')
hold on
plot(dat(ind2,1),dat(ind2,2),'b.')
hold off

%% data for problem #2c

clear
dat1 = [normrnd(6,1,100,1) normrnd(2,1,100,1)];      % create the input data
dat2 = [normrnd(2,1,100,1) normrnd(8,1,100,1)];
dat3 = [normrnd(-2,1,100,1) normrnd(-2,1,100,1)];
dat = [dat1; dat2; dat3];

y(:,1) = [ones(100,1); zeros(100,1); zeros(100,1)];   % the class labels as three dimensional outputs
y(:,2) = [zeros(100,1); ones(100,1); zeros(100,1)]';
y(:,3) = [zeros(100,1); zeros(100,1); ones(100,1)]';
    
% plot the data
ind1 = find(y(:,1) == 1);
ind2 = find(y(:,2) == 1);
ind3 = find(y(:,3) == 1);
plot(dat(ind1,1),dat(ind1,2),'r.')
hold on
plot(dat(ind2,1),dat(ind2,2),'b.')
plot(dat(ind3,1),dat(ind3,2),'g.')
hold off

%% data for problem 3

clear
sd = .85;

x1 = [normrnd(0,sd,50,1); normrnd(0,sd,50,1);  normrnd(0,sd,50,1)];   % the input data
x2 = [normrnd(0,sd,50,1); normrnd(5,sd,50,1);   normrnd(10,sd,50,1)];
x3 = [ones(150,1)];
dat = [x1 x2 x3];
y = [ones(50,1) zeros(50,1) zeros(50,1);  zeros(50,1) ones(50,1) zeros(50,1); zeros(50,1) zeros(50,1) ones(50,1) ];  % the labels

% plot the data
ind1 = find(y(:,1) == 1);
ind2 = find(y(:,2) == 1);
ind3 = find(y(:,3) == 1);
plot(dat(ind1,1),dat(ind1,2),'r.')
hold on
plot(dat(ind2,1),dat(ind2,2),'b.')
plot(dat(ind3,1),dat(ind3,2),'g.')
hold off

% set up the starting parameters for the 2 layer network and weights
nsamp = length(x1);
ninput = 3;
nhidden = 4;
noutput = 3;

W = unifrnd(-1,1,ninput,nhidden);  % initialize weight matrices
V = unifrnd(-1,1,nhidden,noutput);

mu = .05; p = .9;   % a suggested step and momentum size

lastdW = 0*W;  lastdV = 0*V;   % initialize the previous weight change variables, to be used for the momentum

% now do back prop
