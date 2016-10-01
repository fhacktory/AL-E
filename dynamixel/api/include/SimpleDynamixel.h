#include <dynamixel.h>
#include <stdio.h>
#include <termios.h>
#include <unistd.h>

void PrintCommStatus(int CommStatus);
void PrintErrorCode(void);

void moveTo(int ID, int degree);
void moveToWithSpeed(int ID, int degree, int Speed);
int openDevice(void);
void closeDevice(void);
int isMoving(int ID);
int getPosition(int ID);
int getSpeed(int ID);
void setEndLessOn(int ID, int speed);
void setSpeed(int ID, int speed);
void setEndLessOff(int ID);
void reset(int ID);
void setId(int ID, int newId);
