#include "Hector.h"


void startup()
{

  openDevice();

  moveToWithSpeed(13, 0, 25);
  moveToWithSpeed(16, -10, 25);
  moveToWithSpeed(17, 0, 25);
  moveToWithSpeed(12, 0, 25);
  moveToWithSpeed(18, 0, 25);
  moveToWithSpeed(14, 0, 25);
  moveToWithSpeed(11, 0, 25);
  
  closeDevice();
  
}


void wakeUp()
{

  openDevice();

  moveToWithSpeed(16, -40, 6);
  moveToWithSpeed(17, -50, 8);
  moveToWithSpeed(13, -70, 12);
  moveToWithSpeed(12, 0, 5);

  while(isMoving(16))
    {
      sleep(0.1);
    }

  moveToWithSpeed(14, -90, 50);
  moveToWithSpeed(18, 90, 50);

  while(isMoving(18))
    {
      sleep(0.1);
    }
  
  moveToWithSpeed(11, -40, 12);
  while(isMoving(11))
    {
      sleep(0.1);
    }
  sleep(0.4);
  moveToWithSpeed(11, 40, 12);
  while(isMoving(11))
    {
      sleep(0.1);
    }
  sleep(0.4);
  moveToWithSpeed(11, 0, 12);
  while(isMoving(11))
    {
      sleep(0.1);
    }
  sleep(0.4);

  closeDevice();

}


void sleepTight()
{

  openDevice();

  moveToWithSpeed(11, 0, 25);
  moveToWithSpeed(14, 0, 25);
  moveToWithSpeed(18, 0, 25);

  while(isMoving(18))
    {
      sleep(0.1);
    }

  moveToWithSpeed(13, 0, 12);
  moveToWithSpeed(16, -10, 6);
  moveToWithSpeed(17, 0, 8);
  moveToWithSpeed(12, 0, 5);
  
  closeDevice();

}
