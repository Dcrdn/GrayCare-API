from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'user': self.user,
            'password': self.password,
        }

class Familiar(db.Model):
    __tablename__ = 'familiar'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    user = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, idPersona, user, password):
        self.idPersona= idPersona
        self.user = user
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'user': self.user,
            'password': self.password,
        }

class Persona(db.Model):
    __tablename__ = 'persona'

    id = db.Column(db.Integer, primary_key=True)
    idFamiliar = db.Column(db.Integer)
    user = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, idFamiliar, user, password):
        self.idFamiliar= idFamiliar
        self.user = user
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idFamiliar': self.idFamiliar, 
            'user': self.user,
            'password': self.password,
        }

class HeartRate(db.Model):
    __tablename__ = 'hr'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    currentHeartRate = db.Column(db.String())

    def __init__(self, idPersona, currentHeartRate):
        self.idPersona= idPersona
        self.currentHeartRate = currentHeartRate

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'currentHeartRate': self.currentHeartRate
        }

class HistoricHeartRate(db.Model):
    __tablename__ = 'hhr'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    heartRate = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, idPersona, heartRate, date):
        self.idPersona= idPersona
        self.heartRate = heartRate
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'heartRate': self.heartRate,
            'date': self.date,  
        }

class Stress(db.Model):
    __tablename__ = 'stress'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    currentStressLevel = db.Column(db.String())

    def __init__(self, idPersona, currentStressLevel):
        self.idPersona= idPersona
        self.currentStressLevel = currentStressLevel

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'currentStressLevel': self.currentStressLevel
        }

class HistoricStress(db.Model):
    __tablename__ = 'hs'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    stressLevel = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, idPersona, stressLevel, date):
        self.idPersona= idPersona
        self.stressLevel = stressLevel
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'stressLevel': self.stressLevel,
            'date': self.date,  
        }

class Motionless(db.Model):
    __tablename__ = 'motionless'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    currentMotionlessTime = db.Column(db.String())

    def __init__(self, idPersona, currentMotionlessTime):
        self.idPersona= idPersona
        self.currentMotionlessTime = currentMotionlessTime

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'CurrentmotionlessTime': self.currentMotionlessTime
        }


class HistoricMotionless(db.Model):
    __tablename__ = 'hm'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    motionlessTime = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, idPersona, motionlessTime, date):
        self.idPersona= idPersona
        self.motionlessTime = motionlessTime
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'motionlessTime': self.motionlessTime,
            'date': self.date,  
        }

class Sleep(db.Model):
    __tablename__ = 'sleep'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    sleepTime = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, idPersona, sleepTime, date):
        self.idPersona= idPersona
        self.sleepTime = sleepTime
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'sleepTime': self.sleepTime,
            'date': self.date,  
        }

class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    exerciseTime = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, idPersona, exerciseTime, date):
        self.idPersona= idPersona
        self.exerciseTime = exerciseTime
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'exerciseTime': self.exerciseTime,
            'date': self.date,  
        }

class Mood(db.Model):
    __tablename__ = 'mood'

    id = db.Column(db.Integer, primary_key=True)
    idPersona = db.Column(db.Integer)
    happy = db.Column(db.String())
    sad = db.Column(db.String())
    neutro = db.Column(db.String())

    def __init__(self, idPersona, happy, sad, neutro):
        self.idPersona= idPersona
        self.happy = happy
        self.sad = sad
        self.neutro = neutro

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'idPersona': self.idPersona, 
            'happy': self.happy,
            'sad': self.sad,
            'neutro': self.neutro,
        }

"""
Familiar
    id 
    idPersona
    user
    password

Persona
    id
    idFamiliar

HeartRate
    id
    idPersona
    currentHeartRate

HistoricHeartRate:
    id
    idPersona
    heartRate
    date

Stress:
    id
    idPersona
    currentStress

HistoricStress
    id 
    idPersona
    stressLevel
    date
Motionless:
    id
    idPersona
    CurrentmotionlessTime
    date

HistoricMotionless:
    id
    idPersona
    motionlessTime
    date

Sleep:
    id
    idPersona
    sleepTime
    date

Exercise:
    id
    idPersona
    exerciseTime
    date

Mood:
    id
    idPersona
    moodStatus
    date
"""