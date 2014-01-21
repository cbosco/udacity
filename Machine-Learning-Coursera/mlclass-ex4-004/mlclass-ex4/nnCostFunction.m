function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

% Part 1: cost function

% compute h_theta(x)...
% Add ones to the X data matrix (bias input)
a1 = [ones(m, 1) X];

% hidden layer
z2 = (Theta1 * a1')';
a2 = sigmoid(z2);
a2 = [ones(m,1) a2]; % bias input
% output layer
z3 = (Theta2 * a2')';
a3 = sigmoid(z3);

% recode y labels as vectors
y_vec = zeros(m, num_labels);
for c = 1:num_labels
    y_vec(:,c) = (y==c);
end

J = 1/m * sum(sum(-1*y_vec.*log(a3) - (1 - y_vec).*log(1-a3)));


% add Regularization
J = J + lambda/(2*m) * (sum(sum(Theta1(:,2:end).^2)) + sum(sum(Theta2(:,2:end).^2)));

% Part 2: gradient
for t = 1:m
    % transpose all to make column vectors
    a1_t = a1(t,:)';
    z2_t = z2(t,:)';
    z2_t = [1; z2_t]; % bias input
    a2_t = a2(t,:)';
    z3_t = z3(t,:)';
    a3_t = a3(t,:)';

    y_t = y_vec(t,:)';

    delta3_t = a3_t - y_t;

    delta2_t = Theta2' * delta3_t .* sigmoidGradient(z2_t);
    delta2_t = delta2_t(2:end); % skip delta2_t_0

    % accumulate
    Theta1_grad = Theta1_grad + (delta2_t * a1_t');
    Theta2_grad = Theta2_grad + (delta3_t * a2_t');
end

% average out

Theta1_grad = 1/m * Theta1_grad;
Theta2_grad = 1/m * Theta2_grad;

% regularization, add lambda coefficient to all but first terms
Theta1_grad += [zeros(size(Theta1_grad)(:,1),1) ((lambda/m) * Theta1(:,2:end))];
Theta2_grad += [zeros(size(Theta2_grad)(:,1),1) ((lambda/m) * Theta2(:,2:end))];


% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
