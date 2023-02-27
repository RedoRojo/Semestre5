void setup(){
  for(int i=12; i>6; i--) pinMode(i, OUTPUT); 
}

void loop(){ 
    for(int i=12; i>6; i--) {
      digitalWrite(i, HIGH); 
      if(i!=7) delay(500);
      digitalWrite(i, LOW);
    }
    for(int i=7; i<13; i++) {
      digitalWrite(i, HIGH); 
      if(i!=12)delay(500); 
      digitalWrite(i, LOW); 
    }
}