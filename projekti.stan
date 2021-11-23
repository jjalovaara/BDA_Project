data{
  int<lower=0> N; // number of observations for each month
  int<lower=0> J; // number of months
  vector[J] y[N]; // observations
}

parameters {
  real mu_prior;
  real<lower=0> sigma_prior;
  vector[J] mu;
  real<lower=0> sigma;
}

model {
  // hyperpriors
  mu_prior ~ normal(0,1);
  sigma_prior ~ normal(0,1);
  
  // priors
  for (j in 1:J) {
    mu[j] ~ normal(mu_prior, sigma_prior);
  }
  sigma ~ normal(0,1);
  
  // likelihood
  for (j in 1:J) {
    y[,j] ~ normal(mu[j], sigma);
  }
}

generated quantities {
  real ypred;
  vector[N*J] log_lik;
  
  ypred = normal_rng(mu[6], sigma);
  for (j in 1:J) {
    for (i in 1:N) {
      log_lik[i + (j-1)*N] = normal_lpdf(y[i,j] | mu[j], sigma);
    }
  }
}