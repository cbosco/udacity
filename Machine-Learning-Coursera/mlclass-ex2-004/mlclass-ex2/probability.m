% Raw probability utility to check assumptions
function p = probability(theta, X)
    p = sigmoid(theta' * X')';
end
