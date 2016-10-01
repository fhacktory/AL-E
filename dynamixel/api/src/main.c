#include "SimpleDynamixel.h"

int main() {
  openDevice();
  int i;
  for(i = 0; i < 100; i++) {
    reset(i);
  }
  return 0;
}
