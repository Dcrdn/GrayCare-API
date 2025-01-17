import os
import json
import random
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Familiar, Persona, HeartRate, HistoricHeartRate, Stress, HistoricStress, Motionless, HistoricMotionless, Sleep, Exercise, Mood

def agregarUser(firstName, lastName, email, password, address, city, state, cp):
    try:
        familiar=User(
            firstName=firstName,
            lastName=lastName, 
            email=lastName, 
            password=password, 
            address=address, 
            city=city, 
            state=state, 
            cp=cp
        )
        db.session.add(familiar)
        db.session.commit()
        return "User added. user id={}".format(familiar.id)
    except Exception as e:
        return(str(e))

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

            for s in range(0,60):
                exTime=random.randint(4000,10000)
                print(agregarExercise(1,exTime,1))

            for s in mood:
                print(agregarMood(s["idPersona"],s["happy"],s["sad"],s["neutro"]))
            print(agregarUser("Sandra", "Alcaraz", "sandra@gmail.com", "sandra", "Calle ITESM", "Zapopan", "Jalisco", "45418"))
            return True
        except Exception as e:
            return False

@app.route("/")
def hello():
    return "Hello World!"

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
    for i in range(len(hhr)-1, -1, -1):
        iH=hhr[i].serialize()
        print(iH)
        hhrQty.append(int(iH["heartRate"]))

    
    res={"value": hhrQty[0], "data":hhrQty}
    return json.dumps(res)

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
    return json.dumps(res)

@app.route("/getSleep")
def getSleep():
    current=0
    data=[]
    sleep=Sleep.query.all()

    for i in range(len(sleep)-1, -1, -1):
        s=sleep[i].serialize()
        if(i==len(sleep)-1):
            current=s["sleepTime"]
        data.append(int(s["sleepTime"]))
    res={"value": current+" hr", "data":data}
    return json.dumps(res)


@app.route("/getMotionless")
def getMotionless():
    current=0
    data=[]
    motion=HistoricMotionless.query.all()

    for i in range(len(motion)-1, -1, -1):
        s=motion[i].serialize()
        if(i==len(motion)-1):
            current=s["motionlessTime"]
        data.append(int(s["motionlessTime"]))

    res={"value": current+" hr", "data":data}
    return json.dumps(res)

@app.route("/getExercise")
def getExercise():

    current=0
    dataCurrent=[]
    dataPast=[]

    motion=Exercise.query.all()
    if(len(motion)<60):
        size=len(motion)//2
        for i in range(0, size):
            s=motion[i].serialize()
            dataPast.append(int(s["exerciseTime"]))
        for i in range(size, len(motion)):
            s=motion[i].serialize()
            dataCurrent.append(int(s["exerciseTime"]))
        if(len(dataPast)<len(dataCurrent)):
            dataPast.append(dataPast[-1])
        res={"dataPast":dataPast, "dataCurrent":dataCurrent}
    else:
        stop=len(motion)-31
        for i in range(len(motion)-1, stop-1, -1):
            s=motion[i].serialize()
            dataCurrent.append(int(s["exerciseTime"]))
        for i in range(stop, stop-31, -1):
            s=motion[i].serialize()
            dataPast.append(int(s["exerciseTime"]))
        res={"dataPast": dataPast, "dataCurrent":dataCurrent}
    return json.dumps(res)

@app.route("/getPasos")
def getPasos():
    current=0
    dataCurrent=[]
    dataPast=[]
    motion=Exercise.query.all()
    size=len(motion)//2
    s=motion[-1].serialize()
    r=int(s["exerciseTime"])
    res={"data":r}
    return json.dumps(res)


@app.route("/getMood")
def getMood():

    current=0
    data=[]
    motion=Mood.query.all()
    s=motion[0].serialize()
    suma=int(s["happy"])+int(s["sad"])+int(s["neutro"])
    q=(100*int(s["happy"]))/suma
    a = "%.2f" % q
    a=float(a)
    data.append(a)
    q=(100*int(s["sad"]))/suma
    a = "%.2f" % q
    a=float(a)
    data.append(a)
    q=(100*int(s["neutro"]))/suma
    a = "%.2f" % q
    a=float(a)
    data.append(a)
    res={"data":data}
    return json.dumps(res)

@app.route("/sendHeartRate", methods = ['POST'])
def sendHeartRate():
    print("que pedo")
    dic = json.loads(request.get_data())
    print(dic)
    hr=dic["data"]
    print("por agregar: "+ str(hr))
    print(agregarHRR(1, str(hr), "1"))
    res={"data":"success"}
    return json.dumps(res)

@app.route("/sendExercise", methods = ['POST'])
def sendExercise():
    dic = json.loads(request.get_data())
    hr=dic["data"]    
    print(agregarExercise(1, str(hr), "1"))
    res={"data":"success"}
    return json.dumps(res)

@app.route("/updateProfile", methods = ['POST'])
def updateProfile():
    dic = json.loads(request.get_data())
    firstName=dic["firstName"]
    lastName=dic["lastName"]    
    email=dic["email"]    
    password=dic["password"]    
    address=dic["address"]    
    city=dic["city"]    
    state=dic["state"]    
    cp=dic["zip"]    
    print(agregarUser(firstName, lastName, email, password, address, city, state, cp))
    res={"data":"success"}
    return json.dumps(res)


@app.route("/deleteEverything")
def deleteEverything():
    User.query.delete()
    Familiar.query.delete()
    Persona.query.delete()
    HeartRate.query.delete()
    HistoricHeartRate.query.delete()
    Stress.query.delete()
    HistoricStress.query.delete()
    Motionless.query.delete()
    HistoricMotionless.query.delete()
    Sleep.query.delete()
    Exercise.query.delete()
    Mood.query.delete()
    res={"borrado":"success"}
    return json.dumps(res)

@app.route("/getProfile")
def getProfile():
    motion=User.query.all()
    res=motion[-1].serialize()
    return json.dumps(res)


if __name__ == '__main__':
    app.run()
"""
        firstName: "Sandra",
        lastName: "Alcaraz",
        email: "sandra@gmail.com",
        password: "sandra",
        address: "1234 Main St.",
        city: "",
        state: "",
        zip: ""
"""