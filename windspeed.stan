data {
  int<lower=0> N;           
  vector[N] y;  
  vector[N] x;
  real xpred;               
}
parameters {
  real<lower=0> sigma;
  real theta;
}
transformed parameters {
  vector[N] theta_E;
  for (n in 1:N)
    theta_E[n] = 0.5*x[n]^theta;
}
model {
  theta ~ normal(3, 1);     
  y ~ normal(theta_E, 80);          
}
generated quantities {
  real ypred = normal_rng(0.5*xpred^theta, 80); 
}
