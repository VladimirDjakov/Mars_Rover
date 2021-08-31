/*

Изменение направления и частоты вращения двигателя постоянного тока

с использованием чипа L293D, потенциометра и кнопки-переключателя

*/

int enablePin1 = 5;

int in1Pin1 = 2;

int in2Pin1 = 3;

int enablePin2 = 9;

int in1Pin2 = 7;

int in2Pin2 = 6;

//int switchPin = 7;

boolean direct1;
boolean direct2;
int speed1 =0;
int speed2 =0;
//int potPin = 0;
int reverse = 0;
void setup()

{

 
Serial.begin(9600);

pinMode(in1Pin1, OUTPUT);

pinMode(in2Pin1, OUTPUT);

pinMode(enablePin1, OUTPUT);

pinMode(in1Pin2, OUTPUT);

pinMode(in2Pin2, OUTPUT);

pinMode(enablePin2, OUTPUT);

//pinMode(switchPin, INPUT_PULLUP);

}

void loop()

{
if (Serial.available() > 0) {
    reverse = Serial.read()- '0';
    //Serial.println(reverse);
  }



//boolean reverse = data;

setMotor(reverse);

}

void setMotor(int reverse){


switch (reverse) {
case 0:
  speed1 = 0;
  speed2 = 0;
  direct1 = true;
  direct2 = true;
  break;
case 1:
  direct1 = true;
  direct2 = true;
  speed1 = 70;
  speed2 = 70;
  break;
case 2:
  direct1 = false;
  direct2 = false;
  speed1 = 70;
  speed2 = 70;
  break;
case 3:
  direct1 = false;
  direct2 = true;
  speed1 = 0;
  speed2 = 70;
  break;
case 4:
  direct1 = true;
  direct2 = false;
  speed1 = 70;
  speed2 = 0;
  break;
case 5:
  speed1 = 35;
  speed2 = 35;
  break;
case 6:
  speed2 = 45;
  speed2 = 45;
  break;
case 7:
  speed1 = 90;
  speed2 = 90;
  break;
case 8:
  speed1 = 110;
  speed2 = 110;
  break;
case 9:
  speed1 = 200;
  speed2 = 200;
  break;
}



analogWrite(enablePin1, speed1);

digitalWrite(in1Pin1, ! direct1);

digitalWrite(in2Pin1, direct1);

analogWrite(enablePin2, speed2);

digitalWrite(in1Pin2, ! direct2);

digitalWrite(in2Pin2, direct2);

}
