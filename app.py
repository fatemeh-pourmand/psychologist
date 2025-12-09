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
