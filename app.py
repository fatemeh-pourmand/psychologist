Class user:
   def__init__(self,name):
      self.name= name
      self.chat_history = []

   def send_message(self, message):
       self.chat_history.append(message)
       
Class patient(user):
    def __init__(self,name)
    suoer().__init__(name)
    self.emptiom_history = []

 def log_emotion(self, emotion):
       self.emotion_history.appened(emotion)
       
Class Psychologist(user):
    def __init__(slef, name):
        super().__init__(name)
        self.patients = []
    
    def add_patient(slef, patient):
        self.patients.append(patient)
        
    def view_alert(slef):
        
        for p in seld.patients:
            print(f"{p.name} has {len(p.emotion_history)} emotion rntries")

Class DailyEmotion

  def __init__(self,patient):
        self.patient = patient
        self.emotions = [] 
        self.alert = []
        self.message = []
    
    def log_emotion(self,sadness,happieness):
        
        entry = {
            "date": date.today(),
            "sadness" : sadness,
            "happiness": happieness
        }
        self.emotions.append(entry)
        print(f"{self.patient.name} logged emotion {entry}")
   if self.is_critical():
self.alert("⚠️ Critical emotional change detected!")

def is_critical(self):

 if len(self.emotions) < 2:
  return False
yesterday = self.emotions[-2]
today = self.emotions[-1]

return yesterday["happiness"] >= 7 and today["sadness"] >= 7

def alert(self, message):
    
 self.alerts.append(message)
print(f"ALERT for {self.patient.name}: {message}")

def get_latest_emotion(self):

 if self.emotions:
   return self.emotions[-1]
 return None

def get_average_emotion(self):

 if not self.emotions:
  return {"average_happiness": 0, "average_sadness": 0}
total_happiness = sum(e["happiness"] for e in self.emotions)
total_sadness = sum(e["sadness"] for e in self.emotions)
count = len(self.emotions)
return {
"average_happiness": total_happiness / count,
"average_sadness": total_sadness / count
}

Class Alert:
    def__init__(self,date,time,send_message):
    self.date = date 
    self.time = time
    self.send_message = send_message
    
    def__str__(self):
        return f"Alert: {self.send_message}\nDate: {self.date}, Time: {self.time}"
Class Message:
    def__init__(self,patient,psychologist,content,timestamp,id):
        self.patient == patient 
        self.psychologist = psychologist
        self.content = content 
        self.timestamp = timestamp
        self.id = id
        
    def__str__(self):
        return f"Message: {self.patient}, Psychologist: {self.psychologist}, Content: {slef.content}, Timestap: {self.timestap}"

Class Message:
    def__init__(self,patient,psychologist,content,timestamp,id):
        self.patient == patient 
        self.psychologist = psychologist
        self.content = content 
        self.timestamp = timestamp
        self.id = id
        
    def__str__(self):
       return f"Message: {self.patient}, Psychologist: {self.psychologist}, Content: {slef.content}, Timestap: {self.timestap}"

Class NlpAnalysis:
    def__init__(self): 
       self.daily_reports = []
       self.alert = []
       self.patient_notes = []
       self.treatment_emergencies = []
       
    def get_summary(self):
return f"Patient Notes: {self.patient_notes}, Alert: {self.alert}, Treatment_emergencies: {self.treatment_emergencies}, Daily_reports: {self.daily_reports}  "
