function r=controlling(NR)
%CONTROLLING determine the array of indices of Bounding boxes of interest.
%   R=CONTROLLING(NR) outputs the row vector R containing the indices of
%   the bounding boxes of interest from the matrix NR. NR is the matrix of
%   order numberofregionsx4. Numberofregions are the total number of
%   regions extracted from the function regionprops with the property
%   'BoundingBox'. To ensure the order cat(1,...) function could be used.
%   The code for this function emphasize on obtaining the indices of
%   Bounding boxes whose width along the y-dimension is nearly same. If
%   the approach of y-width doesn't work then Bounding Boxes with nearly
%   same y-coordinates are obtained.

[Q,W]=hist(NR(:,4)); % Histogram of the y-dimension widths of all boxes.
ind=find(Q==6); % Find indices from Q corresponding to frequency '6'.
% Since the number plates of cars in Karachi have six characters so
% find(Q==6) is used. If the code is to be implemented for some other plates
% the argument to the function 'find' has to be changed accordingly.
% Q is a row vector of frequency and W is the row vector of all the mid
% points of bins. Hist automatically selects the range of W from its input
% argument.

for k=1:length(NR)            % Taking the advantage of uniqueness of y-co
    C_5(k)=NR(k,2) * NR(k,4); % ordinate and y-width.
end
NR2=cat(2,NR,C_5');           % Appending new coloumn in NR.
[E,R]=hist(NR2(:,5),20);
Y=find(E==6);                 % Searching for six characters.
if length(ind)==1 % If six boxes of interest are succesfully found record
    MP=W(ind);    %  the midpoint of corresponding bin.
    binsize=W(2)-W(1); % Calculate the container size.
    container=[MP-(binsize/2) MP+(binsize/2)]; % Calculating the complete container size.
    r=takeboxes(NR,container,2);
elseif length(Y)==1
    MP=R(Y);
    binsize=R(2)-R(1);
    container=[MP-(binsize/2) MP+(binsize/2)]; % Calculating the complete container size.
    r=takeboxes(NR2,container,2.5); % Call to function takeboxes.
elseif isempty(ind) || length(ind)>1 % If there is no vlaue of '6' in the Q vector.
    [A,B]=hist(NR(:,2),20); % Use y-coordinate approach only.
    ind2=find(A==6);
    if length(ind2)==1
        MP=B(ind2);
        binsize=B(2)-B(1);
        container=[MP-(binsize/2) MP+(binsize/2)]; % Calculating the complete container size.
        r=takeboxes(NR,container,1);
    else
        container=guessthesix(A,B,(B(2)-B(1))); % Call of function guessthesix.
        if ~isempty(container) % If guessthesix works succesfully.
            r=takeboxes(NR,container,1); % Call the function takeboxes.
        elseif isempty(container)
            container2=guessthesix(E,R,(R(2)-R(1)));
            if ~isempty(container2)
                r=takeboxes(NR2,container2,2.5);
            else
                r=[]; % Otherwise assign an empty matrix to 'r'.
            end
        end
    end
end
end

function container=guessthesix(Q,W,bsize)
%GUESSTHESIX guesses the container for six interested Bounding boxes.
%   CONTAINER=GUESSTHESIX(Q,W,BSIZE) outputs the container for the desired
%   Bounding boxes from the frequency row vector Q, row vector of mid
%   points of bins  in W and binsize in BSIZE.

for l=5:-1:2 % This condition has to be changed accordingly if number plates are other than six characters.
    val=find(Q==l); % Find the indices corresponding the value of frequency equals 'l'.
    var=length(val); % Check how many indices are found.
    if isempty(var) || var == 1 % If no index or one index is found.
        if val == 1
            index=val+1; % Since zero index is not allowed in MATLAB.
        else
            index=val; % Assign that value to 'index'.
        end
        if length(Q)==val % In case if the last index value is reached,
            index=[];     % then index+1 will be out of Q.
        end
        if Q(index)+Q(index+1) == 6 % If the sum of frequencies with the subsequent bin equals six.
            container=[W(index)-(bsize/2) W(index+1)+(bsize/2)]; % Calculae container and break looping
            break;                                               % for more values.
        elseif Q(index)+Q(index-1) == 6 % If the sum of frequencies with the previous bin equals six.
            container=[W(index-1)-(bsize/2) W(index)+(bsize/2)]; % Calculate container and break looping
            break;                                               % for more values.
        end
    else % If more than one index are found.
        for k=1:1:var % Repeat the analysis for every value of the bin and checks for the same condition
            if val(k)==1
                index=val(k)+1; % Since zero index is not allowed in MATLAB.
            else
                index=val(k); % that where the sum of frequencies equals six.
            end
            if length(Q)==val(k) % In case if the last index value is reached,
                index=[];        % then index+1 will be out of Q.
            end
            if Q(index)+Q(index+1) == 6
                container=[W(index)-(bsize/2) W(index+1)+(bsize/2)]; % Calculate the value of container and break.
                break;
            elseif Q(index)+Q(index-1) == 6
                container=[W(index-1)-(bsize/2) W(index)+(bsize/2)];
                break;
            end
        end
        if k~=var % If for any value of index bins frequencies sum to six then just break.
            break;
        end
    end
end
if l==2 % If looping is done and no frequencies sum to six then assign container the empty matrix.
    container=[];
end
end

function letter=readLetter(snap)
%READLETTER reads the character fromthe character's binary image.
%   LETTER=READLETTER(SNAP) outputs the character in class 'char' from the
%   input binary image SNAP.

load NewTemplates % Loads the templates of characters in the memory.
snap=imresize(snap,[42 24]); % Resize the input image so it can be compared with the template's images.
comp=[ ];
for n=1:length(NewTemplates)
    sem=corr2(NewTemplates{1,n},snap); % Correlation the input image with every image in the template for best matching.
    comp=[comp sem]; % Record the value of correlation for each template's character.
end
vd=find(comp==max(comp)); % Find the index which correspond to the highest matched character.
%*-*-*-*-*-*-*-*-*-*-*-*-*-
% Accodrding to the index assign to 'letter'.
% Alphabets listings.
if vd==1 || vd==2
    letter='A';
elseif vd==3 || vd==4
    letter='B';
elseif vd==5
    letter='C';
elseif vd==6 || vd==7
    letter='D';
elseif vd==8
    letter='E';
elseif vd==9
    letter='F';
elseif vd==10
    letter='G';
elseif vd==11
    letter='H';
elseif vd==12
    letter='I';
elseif vd==13
    letter='J';
elseif vd==14
    letter='K';
elseif vd==15
    letter='L';
elseif vd==16
    letter='M';
elseif vd==17
    letter='N';
elseif vd==18 || vd==19
    letter='O';
elseif vd==20 || vd==21
    letter='P';
elseif vd==22 || vd==23
    letter='Q';
elseif vd==24 || vd==25
    letter='R';
elseif vd==26
    letter='S';
elseif vd==27
    letter='T';
elseif vd==28
    letter='U';
elseif vd==29
    letter='V';
elseif vd==30
    letter='W';
elseif vd==31
    letter='X';
elseif vd==32
    letter='Y';
elseif vd==33
    letter='Z';
    %*-*-*-*-*
% Numerals listings.
elseif vd==34
    letter='1';
elseif vd==35
    letter='2';
elseif vd==36
    letter='3';
elseif vd==37 || vd==38
    letter='4';
elseif vd==39
    letter='5';
elseif vd==40 || vd==41 || vd==42
    letter='6';
elseif vd==43
    letter='7';
elseif vd==44 || vd==45
    letter='8';
elseif vd==46 || vd==47 || vd==48
    letter='9';
else
    letter='0';
end
end

function r=takeboxes(NR,container,chk)
%TAKEBOXES helps in determining the values of indices of interested Bounding boxes.
% R=TAKEBOXES(NR,CONTAINER,CHK) outputs the value of indices corresponding
% the desired Bounding boxes. NR is the numberofregionsx4 matrix of all the
% regions' Bounding boxes. CONTAINER is the width of the bin that contain
% all the six bounding boxes of interest. CHK will determine whether
% bounding boxes are y-dimension widht's wise grouped or y-coordinate wise
% grouped. CHK=2 considers y-dimension width grouping and CHK=1 considers
% y-coordinate grouping.

takethisbox=[]; % Initialize the variable to an empty matrix.
for i=1:size(NR,1)
    if NR(i,(2*chk))>=container(1) && NR(i,(2*chk))<=container(2) % If Bounding box is among the container plus tolerence.
        takethisbox=cat(1,takethisbox,NR(i,:)); % Take that box and concatenate along first dimension.
    end
end
r=[];
for k=1:size(takethisbox,1)
    var=find(takethisbox(k,1)==reshape(NR(:,1),1,[])); % Finding the indices of the interested boxes among NR
    if length(var)==1                                  % since x-coordinate of the boxes will be unique.
        r=[r var];
    else                                               % In case if x-coordinate is not unique
        for v=1:length(var)                            % then check which box fall under container condition.
            M(v)=NR(var(v),(2*chk))>=container(1) && NR(var(v),(2*chk))<=container(2);
        end
        var=var(M);
        r=[r var];
    end
end
end
