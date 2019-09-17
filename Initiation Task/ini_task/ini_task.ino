int Red = 13;
int Blue = 12;
char input;

void setup() {
  pinMode(Red,OUTPUT);
  pinMode(Blue,OUTPUT);
  Serial.begin(9600);
  Serial.println("Which LED do you want on?");
  Serial.println("Type 'R' for Red and 'B' for Blue and 'O' for neither and 'T' for both");
}

void loop() {
  while(Serial.available()){
    input = Serial.read();
    Serial.print(input);
  }

  if(input == 'R'){
     digitalWrite(Red,HIGH);
     digitalWrite(Blue,LOW);
  }

  else if(input == 'B'){
    digitalWrite(Blue,HIGH);
    digitalWrite(Red,LOW);
  }

  else if(input == 'O'){
    digitalWrite(Blue,LOW);
    digitalWrite(Red,LOW);
  }

    else if(input == 'T'){
    digitalWrite(Blue,HIGH);
    digitalWrite(Red,HIGH);
  }
}
