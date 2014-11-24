

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  // print out the value you read:
  Serial.println(analogRead(A8));
  /*delay (500);
  Serial.println(analogRead(A2));
  delay (500);
  Serial.println(analogRead(A3));
  delay (500);
  Serial.println(analogRead(A4));
  delay (2000);*/        // delay in between reads for stability
}
