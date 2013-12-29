function [J, grad] = costFunctionReg(theta, X, y, lambda)

%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

% ======================
%
% X columns are j-indexed, and correspond to features (28 in ex2_reg)
% X rows are i-indexed, and represent n training examples
% y is a column vector of training example binary results
% theta is a column vector of coefficients (28 in ex2_reg)
% J is a scalar
%
% ======================

J = 1./m * ( -y' * log( sigmoid(X * theta) ) - ( 1 - y' ) * log ( 1 - sigmoid( X * theta)) );

thetan = [theta];
thetan(1, 1) = 0; % theta0 not regularized
% multiply thetan vectors such that the result is 1x1
J = J + sum(lambda./(2 * m) .* thetan' * thetan);

lambda_vector = lambda .* ones(size(theta));
lambda_vector(1, 1) = 0; % theta0 not regularized

grad = 1./m * X' * (sigmoid(X * theta) - y) + (theta .* lambda_vector./m);


% =============================================================

end
