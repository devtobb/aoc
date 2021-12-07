#include <gmp.h>
#include <stdio.h>

int main(){
  mpz_t nfish[9];
  int flag;

  for(int n=0; n<9; n++){
    mpz_init(nfish[n]);
    mpz_set_ui(nfish[n], 0);
  }

  mpz_set_ui(nfish[1], 1);
  mpz_set_ui(nfish[2], 1);
  mpz_set_ui(nfish[3], 2);
  mpz_set_ui(nfish[4], 1);

  for(int d=0; d<9999999; d++){
    mpz_add(nfish[(d+7)%9], nfish[(d+7)%9], nfish[d%9]);
  }

  mpz_t result;
  mpz_init(result),
  mpz_set_ui(result, 0);

  for(int n=0; n<9; n++){
    mpz_add(result, result, nfish[n]);
  }

  mpz_out_str(stdout, 10, result);
}
