//constants

#define threshold 900

//initialise the variables
int D1;
int D2; //these are our binary digits
int D3;
int D4;

int i;

//here are my functions
int binToDec (int, int, int, int); //returns the decimal value from the boolean looking input
void flash2 (int, int, int, int);


// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(43, OUTPUT);
  pinMode(47, OUTPUT);
  pinMode(53, OUTPUT);
  
  //initialise communication at 9600 bits per second
  Serial.begin(9600);  
}

// the loop function runs over and over again forever
void loop() {
  
  digitalWrite(53, LOW);
  digitalWrite(43, HIGH);
  digitalWrite(47, LOW);
  
  D1 = analogRead(A1);
  D2 = analogRead(A2);
  D3 = analogRead(A3);
  D4 = analogRead(A4);
  
  if (analogRead(A7) >= threshold) {
    flash2(D1, D2, D3, D4);
  }
  
}

void flash2(int D1, int D2, int D3, int D4) {
 int outputNum = binToDec(D1, D2, D3, D4);
  
  for (i=0; i < outputNum; i++) {
    digitalWrite(47, HIGH);
    delay(100);
    digitalWrite(47, LOW);
    delay(100);
  } 
}

int binToDec (int D1, int D2, int D3, int D4) {
  int val = 0;
  
  if (D1 >= threshold) val += 8;
  if (D2 >= threshold) val += 4;
  if (D3 >= threshold) val += 2;
  if (D4 >= threshold) val += 1;
  
  return val;
}


  // this prints out our input values
  // a bit more morse codey
 /* 
  Serial.println(D1);
  delay(100);
  Serial.println(D2);
  delay(100);
  Serial.println(D3);
  delay(100);
  Serial.println(D4);
  delay(100);
  */
  
  
// here is another thing I did
/*
if ((D1 >= threshold)) digitalWrite(47, HIGH);
  delay(250);
  digitalWrite(47, LOW);
  delay(100);

  if ((D2 >= threshold)) digitalWrite(47, HIGH);
  
  delay(250);
  digitalWrite(47, LOW);
  delay(100);
  

  if (D3 >= threshold) digitalWrite(47, HIGH);
  delay(250);
  digitalWrite(47, LOW);
  delay(100);


  if ((D4 >= threshold)) digitalWrite(47, HIGH);
  delay(250);
  digitalWrite(47, LOW);
  delay(100);
  
  delay(1000);
  */
