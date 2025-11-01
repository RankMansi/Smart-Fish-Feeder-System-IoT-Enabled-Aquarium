#include <Servo.h>
Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(9); // change pin if needed
}

void loop() {
  if (Serial.available() > 0) {
    int count = Serial.parseInt(); // read the number sent
    if (count > 0) {
      Serial.print("Received count: ");
      Serial.println(count);
      for (int i = 0; i < count; i++) {
        myservo.write(0);
        delay(500);
        myservo.write(90);  // rotate
        delay(1000);
        myservo.write(0);   // reset
        delay(1000);
      }
    }
  }
}