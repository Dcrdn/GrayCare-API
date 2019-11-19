import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Familiar, Persona, HeartRate, HistoricHeartRate, Stress, HistoricStress, Motionless, HistoricMotionless, Sleep, Exercise, Mood

def agregarFamiliar(idPersona, user, password):
    try:
        familiar=Familiar(
            idPersona=idPersona,
            user=user,
            password=password
        )
        db.session.add(familiar)
        db.session.commit()
        return "Familiar added. user id={}".format(familiar.id)
    except Exception as e:
        return(str(e))

def agregarPersona(idFamiliar, user, password):
    try:
        persona=Persona(
            idFamiliar=idFamiliar,
            user=user,
            password=password
        )
        db.session.add(persona)
        db.session.commit()
        return "Persona added. person id={}".format(persona.id)
    except Exception as e:
        return(str(e))

def agregarHR(idPersona, currentHeartRate):
    try:
        query=HeartRate(
            idPersona=idPersona,
            currentHeartRate=currentHeartRate
            )
        db.session.add(query)
        db.session.commit()
        return "HR added. hr id={}".format(query.id)
    except Exception as e:
        print("entra exception")
        return(str(e))

def agregarHRR(idPersona, heartRate, date):
    try:
        query=HistoricHeartRate(
                idPersona=idPersona,
                heartRate=heartRate,
                date=date
            )
        db.session.add(query)
        db.session.commit()
        return "hrr added. hrr id={}".format(query.id)
    except Exception as e:
        return(str(e))

def agregarStress(idPersona, currentStressLevel):
    try:
        query=Stress(
                idPersona=idPersona,
                currentStressLevel=currentStressLevel,
            )
        db.session.add(query)
        db.session.commit()
        return "stress added. stress id={}".format(query.id)
    except Exception as e:
        return(str(e))

def agregarHS(idPersona, stressLevel, date):
    try:
        query=HistoricStress(
                idPersona=idPersona,
                stressLevel=stressLevel,
                date=date
            )
        db.session.add(query)
        db.session.commit()
        return "HS added. HS id={}".format(query.id)
    except Exception as e:
        return(str(e))

def agregarMotionless(idPersona, currentMotionlessTime):
    print("entrando a funcion")
    try:
        query=Motionless(
                idPersona=idPersona,
                currentMotionlessTime=currentMotionlessTime
            )
        db.session.add(query)
        db.session.commit()
        return "Motionless added. Motionless id={}".format(query.id)
    except Exception as e:
        return(str(e))

def agregarHM(idPersona, motionlessTime, date):
    print("entra funcion")
    try:
        query=HistoricMotionless(
                idPersona=idPersona,
                motionlessTime=motionlessTime,
                date=date
            )
        db.session.add(query)
        db.session.commit()
        return "HM added. HM id={}".format(query.id)
    except Exception as e:
        return(str(e))

def agregarSleep(idPersona, sleepTime, date):
    print("entra funcion")
    try:
        query=Sleep(
                idPersona=idPersona,
                sleepTime=sleepTime,
                date=date
            )
        db.session.add(query)
        db.session.commit()
        return "sleep added. sleep id={}".format(query.id)
    except Exception as e:
        return(str(e))

def agregarExercise(idPersona, exerciseTime, date):
    try:
        query=Exercise(
                idPersona=idPersona,
                exerciseTime=exerciseTime,
                date=date
            )
        db.session.add(query)
        db.session.commit()
        return "exercise added. exercise id={}".format(query.id)
    except Exception as e:
        return(str(e))

def agregarMood(idPersona, happy, sad, neutro):
    try:
        query=Mood(
                idPersona=idPersona,
                happy=happy,
                sad=sad,
                neutro=neutro
            )
        db.session.add(query)
        db.session.commit()
        return "mood added. mood id={}".format(query.id)
    except Exception as e:
        return(str(e))


def generateDB():
    with open('data.json') as file:
        data = json.load(file)
        familiar=data["familiar"]
        persona=data["persona"]
        heartRate=data["heartRate"]
        historicHeartRate=data["historicHeartRate"]
        stress=data["stress"]
        historicStress=data["historicStress"]
        motionless=data["motionless"]
        historicMotionless=data["historicMotionless"]
        sleep=data["sleep"]
        exercise=data["exercise"]
        mood=data["mood"]
        
        try:
            for individuo in familiar:
                print(agregarFamiliar(individuo["idPersona"], individuo["user"], individuo["password"]))

            for individuo in persona: 
                print(agregarPersona(individuo["idFamiliar"], individuo["user"], individuo["password"]))

            for hr in heartRate: 
                print(agregarHR(hr["idPersona"],hr["currentHeartRate"]))

            for hr in historicHeartRate: 
                print(agregarHRR(hr["idPersona"],hr["heartRate"],hr["date"]))

            for s in stress:
                print(agregarStress(s["idPersona"],s["currentStressLevel"]))

            for s in historicStress:
                print(agregarHS(s["idPersona"],s["stressLevel"],s["date"]))

            for m in motionless:
                print(agregarMotionless(m["idPersona"],m["currentMotionlessTime"]))

            for m in historicMotionless:
                print(agregarHM(m["idPersona"],m["motionlessTime"],m["date"]))
            #hasta aqui jala
            for s in sleep:
                print(agregarSleep(s["idPersona"],s["sleepTime"],s["date"]))

            for s in exercise:
                print(agregarExercise(s["idPersona"],s["exerciseTime"],s["date"]))

            for s in mood:
                print(agregarMood(s["idPersona"],s["happy"],s["sad"],s["neutro"]))
            return True
        except Exception as e:
            return False

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_book():
    user=request.args.get('user')
    password=request.args.get('password')
    try:
        user=User(
            user=user,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        return "User added. user id={}".format(user.id)
    except Exception as e:
	    return(str(e))

@app.route("/generateDB")
def genDB():
    success=generateDB()
    if(success):
        return str("exito")
    else:
        return str("se pudo")

@app.route("/getHeartRate")
def getHeartRate():
    hr=HeartRate.query.all()
    hhr=HistoricHeartRate.query.all()
    hhrQty=[]
    hrQty=[]
    for i in range(len(hhr)-1, -1, -1):
        iH=hhr[i].serialize()
        print(iH)
        hhrQty.append(iH["heartRate"])
    for i in range(len(hr)-1, -1, -1):
        iH=hr[i].serialize()
        hrQty.append(iH["currentHeartRate"])
        break
    res={"value": hrQty[0], "data":hhrQty}
    return jsonify(res)

@app.route("/getStress")
def getStress():
    current=0
    data=[]
    stress=HistoricStress.query.all()

    for i in range(len(stress)-1, -1, -1):
        s=stress[i].serialize()
        if(i==len(stress)-1):
            current=int(s["stressLevel"])
        data.append(int(s["stressLevel"]))
    res={"value": current, "data":data}
    return jsonify(res)

@app.route("/getSleep")
def getSleep():
    current=0
    data=[]
    sleep=Sleep.query.all()

    for i in range(len(sleep)-1, -1, -1):
        s=sleep[i].serialize()
        if(i==len(sleep)-1):
            current=int(s["sleepTime"])
        data.append(int(s["sleepTime"]))
    res={"value": current, "data":data}
    return jsonify(res)


if __name__ == '__main__':
    app.run()