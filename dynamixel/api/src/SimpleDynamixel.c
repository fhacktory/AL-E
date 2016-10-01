//##########################################################
//##                      R O B O T I S                   ##
//##          Simple Dynamixel code for Dynamixel.        ##
//##                                           2046.05.23 ##
//##########################################################
#include "SimpleDynamixel.h"

// Print communication result
void PrintCommStatus(int CommStatus)
{
  switch(CommStatus)
    {
    case COMM_TXFAIL:
      printf("COMM_TXFAIL: Failed transmit instruction packet!\n");
      break;

    case COMM_TXERROR:
      printf("COMM_TXERROR: Incorrect instruction packet!\n");
      break;

    case COMM_RXFAIL:
      printf("COMM_RXFAIL: Failed get status packet from device!\n");
      break;

    case COMM_RXWAITING:
      printf("COMM_RXWAITING: Now recieving status packet!\n");
      break;

    case COMM_RXTIMEOUT:
      printf("COMM_RXTIMEOUT: There is no status packet!\n");
      break;

    case COMM_RXCORRUPT:
      printf("COMM_RXCORRUPT: Incorrect status packet!\n");
      break;

    default:
      printf("This is unknown error code!\n");
      break;
    }
}

// Print error bit of status packet
void PrintErrorCode()
{
  if(dxl_get_rxpacket_error(ERRBIT_VOLTAGE) == 1)
    printf("Input voltage error!\n");

  if(dxl_get_rxpacket_error(ERRBIT_ANGLE) == 1)
    printf("Angle limit error!\n");

  if(dxl_get_rxpacket_error(ERRBIT_OVERHEAT) == 1)
    printf("Overheat error!\n");

  if(dxl_get_rxpacket_error(ERRBIT_RANGE) == 1)
    printf("Out of range error!\n");

  if(dxl_get_rxpacket_error(ERRBIT_CHECKSUM) == 1)
    printf("Checksum error!\n");

  if(dxl_get_rxpacket_error(ERRBIT_OVERLOAD) == 1)
    printf("Overload error!\n");

  if(dxl_get_rxpacket_error(ERRBIT_INSTRUCTION) == 1)
    printf("Instruction code error!\n");
}

/*degree between -150 and 150*/
void moveTo(int ID, int degree)
{
  int CommStatus;
 
      int result = (int) (511.5 - (degree * (511.5 / 150)));
      printf("Going to : %d\n", result);
      
      dxl_write_word( ID, 30, result);
	
      CommStatus = dxl_get_result();

      if( CommStatus == COMM_RXSUCCESS )
	{
	  PrintErrorCode();
	}
      else
	{
	  PrintCommStatus(CommStatus);
	  return;
	}
}


/*Speed in %*/
void moveToWithSpeed(int ID, int degree, int speed)
{
  int CommStatus;

  dxl_write_word( ID, 32, (int) ((1023 * speed) / 100));
  
      
  int result = (int) (511.5 - (degree * (511.5 / 150)));
  printf("Going to : %d\n", result);
      
  dxl_write_word( ID, 30, result);
	
  CommStatus = dxl_get_result();

  if( CommStatus == COMM_RXSUCCESS )
    {
      PrintErrorCode();
    }
  else
    {
      PrintCommStatus(CommStatus);
      return;
    }
}


int openDevice()
{

  int baudnum = 1;
  int deviceIndex = 0;
  
  if( dxl_initialize(deviceIndex, baudnum) == 0 )
    {
      
      printf( "Failed to open USB2Dynamixel!\n" );
      
      return 0;
      
    }
  else
    {
      
      printf( "Succeed to open USB2Dynamixel!\n" );

      return 1;
      
    }
  
}


void closeDevice()
{

  printf( "Device closed!\n" );
  dxl_terminate();

}


int isMoving(int ID)
{

  return (dxl_read_byte(ID, 46));

}


int getPosition(int ID)
{
  
  int currentPosition =  dxl_read_word(ID, 36);

  return (int) ((511.5 - currentPosition) / (511.5 / 150));
  
}

int getSpeed(int ID)
{

  int currentSpeed = dxl_read_word(ID, 38);

  return (int) ((currentSpeed * 100) / 1023);

}

void setEndLessOn(int ID, int speed)
{

  int CommStatus;

  dxl_write_word(ID, 6, 0);
  dxl_write_word(ID, 8, 0);
  
  CommStatus = dxl_get_result();

  if( CommStatus == COMM_RXSUCCESS )
    {
      PrintErrorCode();
    }
  else
    {
      PrintCommStatus(CommStatus);
      return;
    }

  setSpeed(ID, speed);

}

void setSpeed(int ID, int speed)
{

  int CommStatus;

  dxl_write_word( ID, 32, (int) ((1023 * speed) / 100));

  CommStatus = dxl_get_result();

  if( CommStatus == COMM_RXSUCCESS )
    {
      PrintErrorCode();
    }
  else
    {

      PrintCommStatus(CommStatus);
      return;
    }

}



void setEndLessOff(int ID)
{

  int CommStatus;

  dxl_write_word(ID, 8, 255);
  //dxl_write_word(ID, 6, 0);
  
  CommStatus = dxl_get_result();

  if( CommStatus == COMM_RXSUCCESS )
    {
      PrintErrorCode();
    }
  else
    {
      PrintCommStatus(CommStatus);
      return;
    }

}

void reset(int ID)
{

  dxl_reset(ID);

  //setId(1, ID);

}

void setId(int ID, int newId)
{
  
  int CommStatus;

  dxl_write_word(ID, 3, newId);
  
  CommStatus = dxl_get_result();

  if( CommStatus == COMM_RXSUCCESS )
    {
      PrintErrorCode();
    }
  else
    {
      PrintCommStatus(CommStatus);
      return;
    }

}
