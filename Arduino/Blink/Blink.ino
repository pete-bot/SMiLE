// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(43, OUTPUT);
  pinMode(53, OUTPUT);
  pinMode(33, OUTPUT);
  
  //initialise communication at 9600 bits per second
  Serial.begin(9600);  
}

// the loop function runs over and over again forever
void loop() {
  
  int inputVal = analogRead(A0);
  Serial.println(inputVal);
  
  digitalWrite(53, LOW);
  digitalWrite(33, HIGH);
  
  if (inputVal >=  1000) {
    digitalWrite(43, HIGH);
  } else {
    digitalWrite(43, LOW);
  }
  
  //delay(100);
  
}
