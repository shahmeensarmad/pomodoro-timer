// Pomodoro Timer
  // Skills/Components Used: Piezo, LCD, LED, Pushbutton switches
  
  /*
    GOAL: 
      - Timer of 25 minutes that counts down (or up)
      - When one pomodoro is done, it makes a beep sound, and the LED goes from the red light being on to the green light being on
      - Then, you click a switch to make a 5 minute timer go off (there are two switches, one for 5 minutes, one for 25 minutes)
      - During the 5 minute rest timer, there is a yellow LED blinking, it makes a sound of a different frequence after 
      - Tracks the pomodoro count until you reset it
    */

// set up LiquidCrystal library (initialize and import)
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);	// which pins to communicate with

// ** CONSTANTS AND VARIABLES **

/*
// INTERVALS - TESTING ----------------------------- !!
const unsigned long pomodoroInterval = 5 * 1000UL;
const unsigned long restInterval = 3 * 1000UL;
*/

// Intervals 
// Note: unsigned long - non-negative integers, prevents possible error with large time values
const unsigned long pomodoroInterval = 25 * 60 * 1000UL;
const unsigned long restInterval = 5 * 60 * 1000UL;

// Pomodoro Switch
const int switchPinP = 6;
int switchStateP = 0;
int prevSwitchStateP = LOW;

// Rest Switch
const int switchPinR = 10;
int switchStateR = 0;
int prevSwitchStateR = LOW;

// LEDs (Pins)
int redLed = 7;
int yellowLed = 8;
int greenLed = 9;

// Piezo
int piezoPin = A4;
int pomodoroDoneNotes[] = {659, 523};
int restDoneNotes[]     = {440, 330};

// States/bools
bool initiatePomodoro = false;
bool initiateRest = false;
bool errorShown = false;

// Timing
unsigned long previousTime = 0;
unsigned long lastDisplayedSecond = 0;

// Counts
int pomodoroCount = 0;
int restCount = 0;

// ** FUNCTIONS **

void setLEDs(bool redState, bool yellowState, bool greenState) {
  digitalWrite(redLed, redState);
  digitalWrite(yellowLed, yellowState);
  digitalWrite(greenLed, greenState);
}

void displayCountdown(unsigned long secondsRemaining) {
  int mins = secondsRemaining / 60;	// integer division, rounds down
  int secs = secondsRemaining % 60;	// remainder = num seconds

  lcd.setCursor(0, 1);
  lcd.print("        ");	// clears remaining numbers from countdown
  lcd.setCursor(0, 1);
  lcd.print(mins);
  lcd.print(":");
  if (secs < 10) lcd.print("0");	// Ex. 09
  lcd.print(secs);
}

// two note chime
void playChime(int notes[]) {
  tone(piezoPin, notes[0]);
  delay(400);
  noTone(piezoPin);
  tone(piezoPin, notes[1]);
  delay(400);
  noTone(piezoPin);
}

// const char* = constant string, read only, pointer stores memory address of first character
void showDoneScreen(const char* label, int count) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(label);
  lcd.setCursor(0, 1);
  lcd.print(count);
}

void handleError() {
  if (!errorShown) {	// if no error message shown
    lcd.clear();
    setLEDs(HIGH, HIGH, HIGH);	// turn on all LEDs
    lcd.setCursor(0, 0);
    lcd.print("Error! Press");
    lcd.setCursor(0, 1);
    lcd.print("a Button");
    errorShown = true;	// error message has been shown
  }

  // || means or
  // if pomodoro or rest button have been pressed
  if ((switchStateP != prevSwitchStateP && switchStateP == HIGH) ||
      (switchStateR != prevSwitchStateR && switchStateR == HIGH)) {
    initiatePomodoro = false;
    initiateRest = false;
    errorShown = false;
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Pomodoro Ready");
  }
}

// ** SETUP **

void setup() {
  lcd.begin(16, 2);	// 16 columns, 2 rows

  // switch pins are inputs
  pinMode(switchPinP, INPUT);
  pinMode(switchPinR, INPUT);

  // LEDs are outputs
  pinMode(redLed, OUTPUT);
  pinMode(yellowLed, OUTPUT);
  pinMode(greenLed, OUTPUT);

  // turn off all LEDs
  setLEDs(LOW, LOW, LOW);

  lcd.setCursor(0, 0);
  lcd.print("Pomodoro Ready");
}

// ** LOOP **

void loop() {
  unsigned long currentTime = millis();	// start tracking time

  // Read if either button has been pressed
  switchStateP = digitalRead(switchPinP);
  switchStateR = digitalRead(switchPinR);

  // ERROR STATE - if a button is pressed and interrupts an already existing timer
  if (initiatePomodoro && initiateRest) {
    handleError();
    // skip the rest of the loop, essentially reset
    prevSwitchStateP = switchStateP;
    prevSwitchStateR = switchStateR;
    return;
  }

// ** POMODORO **
  
  // if pomodoro button is pressed
  if (switchStateP != prevSwitchStateP && switchStateP == HIGH) {
    initiatePomodoro = true;
    previousTime = currentTime;	// set elapsed time to 0
    lastDisplayedSecond = 0;

    setLEDs(HIGH, LOW, LOW);	// turn on red LED

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Focus Timer:");
  }

  if (initiatePomodoro) {
    unsigned long elapsed = currentTime - previousTime;	// find elapsed time

    if (elapsed >= pomodoroInterval) {
      initiatePomodoro = false;
      pomodoroCount++;	// increase pomodoro count by 1

      setLEDs(LOW, LOW, HIGH);	// turn on green light to indicate timer is done
      lcd.setCursor(0, 1);
      lcd.print("Done!        ");	// helps clear leftover digits

      playChime(pomodoroDoneNotes);	// plays two note chime
      delay(2000);	// wait 2 seconds

      showDoneScreen("Pomodoro Count:", pomodoroCount);
    } 
    
    else {
   	  unsigned long secondsRemaining = (pomodoroInterval - elapsed) / 1000;
      
      if (secondsRemaining != lastDisplayedSecond) {	// if seconds number is actually different - helps solve flickering/glitching
        lastDisplayedSecond = secondsRemaining;
        displayCountdown(secondsRemaining);
      }
    }
  }

 // ** REST **

  // if rest button is pressed
  if (switchStateR != prevSwitchStateR && switchStateR == HIGH) {
    initiateRest = true;
    previousTime = currentTime;	// reset elapsed time
    lastDisplayedSecond = 0;

    setLEDs(LOW, HIGH, LOW);	// turn on yellow LED

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Rest Timer:");
  }

  if (initiateRest) {
    unsigned long elapsed = currentTime - previousTime;	// start tracking elapsed time

    if (elapsed >= restInterval) {
      initiateRest = false;
      restCount++;	// increase rest count by 1

      setLEDs(LOW, LOW, HIGH);	// turn on green LED to indicate timer is done
      lcd.setCursor(0, 1);
      lcd.print("Done!        ");

      playChime(restDoneNotes);
      delay(2000);

      showDoneScreen("Breaks Taken:", restCount);
    } 
    
    else {
      unsigned long secondsRemaining = (restInterval - elapsed) / 1000;
    
      if (secondsRemaining != lastDisplayedSecond) {
        lastDisplayedSecond = secondsRemaining;
        displayCountdown(secondsRemaining);
      }
    }
  }

  // reset states of switches
  prevSwitchStateP = switchStateP;
  prevSwitchStateR = switchStateR;
}
